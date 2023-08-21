import random
import numpy as np

class Simulador:
    """Representa la simulación del modelo SIR y agregados.

    Atributos:
        poblacion_inicial (int): [Población inicial]
        recursos_iniciales (int): [Recursos iniciales]
        recursos_iniciales (list): [Eventos catastroficos]
        num_anios (int): [Número de años a simular]
    """
    
    def __init__(self, poblacion_inicial, recursos_iniciales, eventos_catastroficos, num_anios=365):
        # Parámetros iniciales
        self.poblacion_inicial = poblacion_inicial
        self.recursos_iniciales = recursos_iniciales
        self.num_anios = num_anios
        self.eventos_catastroficos = eventos_catastroficos

        # Listas para almacenar resultados
        self.poblacion = [self.poblacion_inicial]
        self.recursos = [self.recursos_iniciales]
        self.susceptibles = []
        self.infectados = []
        self.recuperados = []
        self.muertes = []

        # Valores actuales
        self.poblacion_actual = self.poblacion_inicial
        self.recursos_disponibles = self.recursos_iniciales
        
    def expedicion_de_recursos(self, poblacion_actual, recursos_disponibles, recursos_encontrados, probabilidad_exito):
        if poblacion_actual == 0:
            return poblacion_actual, recursos_disponibles

        exito = random.random() <= probabilidad_exito
        print(exito)

        if exito:
            recursos_disponibles += recursos_encontrados
        else:
            muertes_expedicion = round(0.01 * poblacion_actual)
            poblacion_actual -= muertes_expedicion

        # Asegurarse de que la población no sea negativa
        poblacion_actual = max(0, poblacion_actual)

        return poblacion_actual, recursos_disponibles

    def calcular_muertes_por_recursos(self, poblacion_actual, recursos_disponibles, consumo_recursos_por_persona):
        muertes_por_recursos = 0

        if recursos_disponibles == 0:
            muertes_por_recursos = round(poblacion_actual)
        elif recursos_disponibles < (consumo_recursos_por_persona * poblacion_actual):

            muertes_por_recursos = round(poblacion_actual) - (recursos_disponibles / consumo_recursos_por_persona)
            recursos_disponibles = recursos_disponibles - recursos_disponibles* consumo_recursos_por_persona

        return muertes_por_recursos
    
    def ajustar_recursos(self, poblacion_actual, recursos_disponibles, consumo_recursos_por_persona, muertes_por_recursos):
        recursos_disponibles -= muertes_por_recursos * consumo_recursos_por_persona
            
        # ajustar recursos basados en el consumo de la poblacion
        if recursos_disponibles <= 0:
            recursos_disponibles = 0
        else:
            recursos_disponibles -= round(poblacion_actual) * consumo_recursos_por_persona

        return recursos_disponibles

    def simular_evento_catastrofico(self, eventos_catastroficos,poblacion_actual):
        evento_muertes1=0
        for evento in eventos_catastroficos:
            if np.random.rand() < evento["probabilidad"]:
                evento_muertes1= evento_muertes1+ round(evento["muertes_aprox"]*poblacion_actual)
        return evento_muertes1

    def simular_modelo_sir_mortalidad(self, poblacion_actual, proporcion_individuos_infectados, beta, gamma, tasa_mortalidad_enfermedad,anio):
        
        self.susceptibles.append(round(poblacion_actual*(1-proporcion_individuos_infectados)))
        self.infectados.append(round(poblacion_actual*(proporcion_individuos_infectados)))

        nuevas_infecciones = round(beta * self.susceptibles[-1] * self.infectados[-1] / poblacion_actual)
        
        nuevas_recuperaciones = int(gamma * self.infectados[-1])
        nuevas_muertes = int(tasa_mortalidad_enfermedad * self.infectados[-1])

        self.susceptibles.append(self.susceptibles[anio-1] - nuevas_infecciones)
        self.infectados.append(self.infectados[anio-1] + nuevas_infecciones - nuevas_recuperaciones - nuevas_muertes)
        self.recuperados.append((nuevas_recuperaciones))
        self.muertes.append(( nuevas_muertes))

        return self.muertes[-1]

    def simular(self, tasa_natalidad, tasa_mortalidad, consumo_recursos_por_persona, recursos_por_expedicion, probabilidad_exito_expedicion, proporcion_individuos_infectados, beta, gamma, tasa_mortalidad_enfermedad):
        for anio in range(self.num_anios):
            # Asegurarse de que la población no sea negativa
            self.poblacion_actual = max(0, round(self.poblacion_actual))

            # Nacimientos solo si la poblacion actual es mayor a 0
            if self.poblacion_actual > 0:

                # muertes por falta de recursos
                muertes_por_recursos = self.calcular_muertes_por_recursos(self.poblacion_actual, self.recursos_disponibles, consumo_recursos_por_persona)

                # Ajustar los recursos de la poblacion
                self.recursos_disponibles = self.ajustar_recursos(self.poblacion_actual, self.recursos_disponibles, consumo_recursos_por_persona, muertes_por_recursos)
                
                #Ajustar el numero de personas que fallecieron por falta de recursos
                self.poblacion_actual -= muertes_por_recursos
                #Calcular el numero de personas nacidas
                nacimientos = round(self.poblacion_actual * tasa_natalidad)
                #Calcular el numero de personas fallecidas
                muertes_por_edad = round(self.poblacion_actual * tasa_mortalidad)
                
                # poblacion actual de ese año
                self.poblacion_actual += nacimientos - muertes_por_edad
                
                #Muertes por enfermedad
            if self.poblacion_actual > 0:
                total_muertes = self.simular_modelo_sir_mortalidad(self.poblacion_actual, proporcion_individuos_infectados, beta, gamma, tasa_mortalidad_enfermedad,anio)
                self.poblacion_actual -= total_muertes

                # probabilidad de evento catastrofico
            if self.poblacion_actual > 0:    
                evento_muertes = self.simular_evento_catastrofico(eventos_catastroficos,self.poblacion_actual)
                self.poblacion_actual -= evento_muertes

            # Realizar expedición de recursos solo si hay población disponible
            if self.poblacion_actual > 0:
                self.poblacion_actual, self.recursos_disponibles = self.expedicion_de_recursos(
                    self.poblacion_actual, self.recursos_disponibles, recursos_por_expedicion, probabilidad_exito_expedicion
                )

            # guardar los valores por año en sus respectivas listas
            self.poblacion.append(max(0, round(self.poblacion_actual)))
            self.recursos.append(max(0, self.recursos_disponibles))


    def mostrar_resultados(self):
        print(self.poblacion)
        print(self.recursos)
        print(self.susceptibles)
        print(self.infectados)
        print(self.recuperados)
        print(self.muertes)


# Usar la clase:
eventos_catastroficos = [
    {"nombre": "Exposición a la radiación", "muertes_aprox": 0.3, "probabilidad": 0.3},
    {"nombre": "Conflictos internos", "muertes_aprox": 0.02, "probabilidad": 0.5},
    {"nombre": "Lluvia de Metoritos", "muertes_aprox": 0.1, "probabilidad": 0.2}
]

# Inicialización
sim = Simulador(10000, 20000000, eventos_catastroficos)
sim.simular(0.3, 0.1, 2, 10000, 0, 0.2, 0.04, 0.03, 0.02)
sim.mostrar_resultados()