import tkinter as tk
from tkinter import font
from tkinter import Spinbox
from results import SimuladorVentana
import sim 
class ColonosSimulator(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuraciones de ventana
        self.title("Simulador Colonos")
        self.geometry("1200x600")

        # Estilos y configuraciones
        self.initialize_styles()

        # Creación de componentes
        self.create_widgets()

        # Inicializar atributos
    def initialize_styles(self):
        self.slider_style = {
            "troughcolor": "#E0E0E0",
            "sliderlength": 20,
            "sliderrelief": "flat",
            "highlightthickness": 0,
            "background": "white",
        }
        self.blue_color = "#051C3E"
        self.white_color = "white"
        self.font_path = "fonts/Fredoka-Regular.ttf"
        self.custom_font = font.Font(family="Fredoka", size=14)

    def create_widgets(self):
        # Frames
        self.blue_bar = tk.Frame(self, bg=self.blue_color)
        self.left_frame = tk.Frame(self, bg=self.white_color)
        self.right_frame = tk.Frame(self, bg=self.white_color)

        # Pack Frames
        self.blue_bar.pack(side="top", fill="x")
        self.left_frame.pack(side="left", fill="both", expand=True)
        self.right_frame.pack(side="right", fill="both", expand=True)

        # Barra Azul
        self.title_label = tk.Label(self.blue_bar, text="Colonos del Horizonte", font=self.custom_font, bg=self.blue_color, fg="white")
        self.title_label.pack(pady=5, padx=10, anchor="w")

        # Sección Izquierda
        self.create_left_section()

        # Sección Derecha
        self.create_right_section()

        # Botones Empezar y Volver
        self.create_bottom_buttons()

    def create_left_section(self):
        self.section_left = tk.Frame(self.left_frame, bg=self.white_color)
        self.section_left.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.section_left_1 = tk.Frame(self.section_left, bg=self.white_color)
        self.section_left_2 = tk.Frame(self.section_left, bg=self.white_color)
        self.section_left_1.pack(side="left", fill="both", expand=True, padx=(0, 10))
        self.section_left_2.pack(side="right", fill="both", expand=True, padx=(10, 0))

        # Elementos de section_left_1 y section_left_2

    def create_right_section(self):
        self.section_right = tk.Frame(self.right_frame, bg=self.white_color)
        self.section_right.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Elementos de section_right

    def create_bottom_buttons(self):
        self.empezar_button = tk.Button(self.right_frame, text="Empezar simulación", font=self.custom_font, bg="#5762D5", fg="white", borderwidth=0)
        self.empezar_button.pack(side="bottom", anchor="center", pady=(0, 20))
        
        self.spacer = tk.Label(self.left_frame, bg=self.white_color)
        self.spacer.pack(side="top", pady=5)
        
        self.volver_button = tk.Button(self.left_frame, text="Volver", font=self.custom_font, bg="#932025", fg="white", borderwidth=0)
        self.volver_button.pack(side="top", padx=20, pady=10, anchor="center")

    def create_left_section(self):
        self.section_left = tk.Frame(self.left_frame, bg=self.white_color)
        self.section_left.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.section_left_1 = tk.Frame(self.section_left, bg=self.white_color)
        self.section_left_2 = tk.Frame(self.section_left, bg=self.white_color)
        
        self.section_left_1.pack(side="left", fill="both", expand=True, padx=(0, 10))
        self.section_left_2.pack(side="right", fill="both", expand=True, padx=(10, 0))
        
        self.create_section_left_1_elements()
        self.create_section_left_2_elements()

    def create_section_left_1_elements(self):
        # Población inicial
        label1 = tk.Label(self.section_left_1, text="Población inicial", font=self.custom_font, bg=self.white_color, anchor="w")
        label1.pack(fill="x")
        self.label2 = tk.Label(self.section_left_1, text="Número inicial de colonos:", font=self.custom_font, bg=self.white_color, anchor="w")
        self.label2.pack(fill="x")
        self.input_entry1 = tk.Entry(self.section_left_1, width=15)
        self.input_entry1.pack(fill="x")

        # Tasa de Natalidad
        label3 = tk.Label(self.section_left_1, text="Tasa de Natalidad", font=self.custom_font, bg=self.white_color, anchor="w")
        label3.pack(fill="x")
        label4 = tk.Label(self.section_left_1, text="Natalidad diaria por individuo:", font=self.custom_font, bg=self.white_color, anchor="w")
        label4.pack(fill="x")
        self.input_entry2 = tk.Entry(self.section_left_1, width=15)
        self.input_entry2.pack(fill="x")

        # Tasa de Mortalidad
        label5 = tk.Label(self.section_left_1, text="Tasa de Mortalidad", font=self.custom_font, bg=self.white_color, anchor="w")
        label5.pack(fill="x")
        label6 = tk.Label(self.section_left_1, text="Mortalidad diaria por individuo:", font=self.custom_font, bg=self.white_color, anchor="w")
        label6.pack(fill="x")
        self.input_entry3 = tk.Entry(self.section_left_1, width=15)
        self.input_entry3.pack(fill="x")

        # Recursos Encontrados
        label7 = tk.Label(self.section_left_1, text="Recursos Encontrados", font=self.custom_font, bg=self.white_color, anchor="w")
        label7.pack(fill="x")
        self.label8 = tk.Label(self.section_left_1, text="Recursos encontrados en cada evento exitoso:", font=self.custom_font, bg=self.white_color, anchor="w")
        self.label8.pack(fill="x")
        self.input_entry4 = tk.Entry(self.section_left_1, width=15)
        self.input_entry4.pack(fill="x")


        # Probabilidad de encontrar recursos
        label9 = tk.Label(self.section_left_1, text="Probabilidad de encontrar recursos", font=self.custom_font, bg=self.white_color, anchor="w")
        label9.pack(fill="x")
        self.range_slider = tk.Scale(self.section_left_1, from_=0.0, to=1.0, resolution=0.1, orient="horizontal", **self.slider_style)
        self.range_slider.pack(fill="x")

    def create_section_left_2_elements(self):
        # Recursos iniciales
        label10 = tk.Label(self.section_left_2, text="Recursos iniciales", font=self.custom_font, bg=self.white_color, anchor="w")
        label10.pack(fill="x")
        label11 = tk.Label(self.section_left_2, text="Cantidad inicial de recursos disponibles:", font=self.custom_font, bg=self.white_color, anchor="w")
        label11.pack(fill="x")
        self.input_entry5 = tk.Entry(self.section_left_2, width=15)
        self.input_entry5.pack(fill="x")


        # Consumo por persona
        label12 = tk.Label(self.section_left_2, text="Consumo por persona", font=self.custom_font, bg=self.white_color, anchor="w")
        label12.pack(fill="x")
        label13 = tk.Label(self.section_left_2, text="Cantidad de recursos consumidos por persona por día:", font=self.custom_font, bg=self.white_color, anchor="w")
        label13.pack(fill="x")
        self.input_entry6 = tk.Entry(self.section_left_2, width=15)
        self.input_entry6.pack(fill="x")


        # Duración de la simulación
        label14 = tk.Label(self.section_left_2, text="Duración de la simulación", font=self.custom_font, bg=self.white_color, anchor="w")
        label14.pack(fill="x")
        label15 = tk.Label(self.section_left_2, text="Duración de la simulación en años:", font=self.custom_font, bg=self.white_color, anchor="w")
        label15.pack(fill="x")
        self.input_entry7 = tk.Entry(self.section_left_2, width=15)
        self.input_entry7.pack(fill="x")


    def create_right_section(self):
        self.section_right = tk.Frame(self.right_frame, bg=self.white_color)
        self.section_right.pack(fill="both", expand=True, padx=20, pady=20)

        self.desastres_checkbox_var = tk.IntVar()
        self.enfermedades_checkbox_var = tk.IntVar()

        # Desastres Naturales
        label15 = tk.Label(self.section_right, text="Desastres Naturales", font=self.custom_font, bg=self.white_color, anchor="w")
        label15.pack(fill="x")
        checkbox1 = tk.Checkbutton(self.section_right, text="Activar desastres", font=self.custom_font, bg=self.white_color, variable=self.desastres_checkbox_var, command=self.update_slider_visibility)
        checkbox1.pack(fill="x")
        self.slider1 = tk.Scale(self.section_right, from_=0.0, to=1.0,resolution=0.1 ,orient="horizontal", label="Probabilidad de desastres naturales", **self.slider_style)
        self.slider1.pack(side="top", fill="x", padx=10, pady=5)  # Empaquetar al principio, pero oculto
        self.update_slider_visibility()

        # Enfermedades
        label17 = tk.Label(self.section_right, text="Enfermedades", font=self.custom_font, bg=self.white_color, anchor="w")
        label17.pack(fill="x")
        checkbox2 = tk.Checkbutton(self.section_right, text="Activar enfermedades", font=self.custom_font, bg=self.white_color, variable=self.enfermedades_checkbox_var, command=self.update_enfermedades_visibility)
        checkbox2.pack(fill="x")
        self.label18 = tk.Label(self.section_right, text="Tasa de Transmisión", font=self.custom_font, bg=self.white_color, anchor="w")
        self.label18.pack(fill="x")
        self.entry8 = tk.Entry(self.section_right, font=self.custom_font)
        self.entry8.pack(fill="x")
        self.label20 = tk.Label(self.section_right, text="Tasa de mortalidad por enfermedad", font=self.custom_font, bg=self.white_color, anchor="w")
        self.label20.pack(fill="x")
        self.entry9 = tk.Entry(self.section_right, font=self.custom_font)
        self.entry9.pack(fill="x")
        self.label21 = tk.Label(self.section_right, text="Tasa de recuperación", font=self.custom_font, bg=self.white_color, anchor="w")
        self.label21.pack(fill="x")
        self.entry10 = tk.Entry(self.section_right, font=self.custom_font)
        self.entry10.pack(fill="x")
        self.label22 = tk.Label(self.section_right, text="Número de infectados", font=self.custom_font, bg=self.white_color, anchor="w")
        self.label22.pack(fill="x")
        self.entry11 = tk.Entry(self.section_right, font=self.custom_font)
        self.entry11.pack(fill="x")
        self.update_enfermedades_visibility()

    def update_slider_visibility(self):
        if self.desastres_checkbox_var.get():
            self.slider1.pack(side="top", fill="x", padx=10, pady=5)
        else:
            self.slider1.pack_forget()

    def update_enfermedades_visibility(self):
        if self.enfermedades_checkbox_var.get()==True:
            self.label18.pack(side="top", fill="x", padx=10, pady=5)
            self.entry8.pack(side="top", fill="x", padx=10, pady=5)
            self.label20.pack(side="top", fill="x", padx=10, pady=5)
            self.entry9.pack(side="top", fill="x", padx=10, pady=5)
            self.label21.pack(side="top", fill="x", padx=10, pady=5)
            self.entry10.pack(side="top", fill="x", padx=10, pady=5)
            self.label22.pack(side="top", fill="x", padx=10, pady=5)
            self.entry11.pack(side="top", fill="x", padx=10, pady=5)

        else:
            self.slider1.pack_forget()
      

    def create_bottom_buttons(self):
        # Botón Empezar Simulación
        self.empezar_button = tk.Button(self.right_frame, text="Empezar simulación", font=self.custom_font, bg="#5762D5", fg="white", borderwidth=0, command=self.transition_to_simulation, cursor="hand2", activebackground="#244164")
        self.empezar_button.pack(side="bottom", anchor="center", pady=(0, 20))

        # Imagen Frame.png en la esquina inferior derecha
        self.image_path = "images/Frame.png"
        self.image = tk.PhotoImage(file=self.image_path)
        self.image_label = tk.Label(self.right_frame, image=self.image, bg=self.white_color)
        self.image_label.pack(side="bottom", anchor="se", padx=10, pady=10)

        # Botón Volver
        self.spacer = tk.Label(self.left_frame, bg=self.white_color)
        self.spacer.pack(side="top", pady=5)
        self.volver_button = tk.Button(self.left_frame, text="Volver", font=self.custom_font, bg="#932025", fg="white", borderwidth=0, command=self.return_to_main, cursor="hand2", activebackground="#FE8B14")
        self.volver_button.pack(side="top", padx=20, pady=10, anchor="center")
    
    def return_to_main(self):
        self.destroy()
        from main import App # importación tardia, solo hace la importación hasta que se necesite.
        app = App("Simulador Colonos", (1000, 600))
        app.mainloop()

    def obtenerValores(self):
                #para iniciar la Clase simulador del backend
        poblacion = self.input_entry1.get()  # Obtener el valor del campo de entrada
        recursos = self.input_entry5.get()  # Obtener el valor del campo de entrada
        years = self.input_entry7.get()  # Obtener el valor del campo de entrada
       
       #funcion simular
        natalidad = self.input_entry2.get()
        mortalidad = self.input_entry3.get()
        recursos_encontrados = self.input_entry4.get()
        consumo_persona = self.input_entry6.get()
        probabilidad_recursos = self.range_slider.get()
        transmicion = self.entry8.get()
        mortalidad_enfermedad = self.entry9.get()
        recuperacion = self.entry10.get()
        infectados = self.entry11.get()

        if poblacion:  # Verificar si el valor no está vacío
            poblacion_inicial = int(poblacion)  # Convertir el valor a entero si es válido
        
        if recursos:  # Verificar si el valor no está vacío
            recursos_iniciales = int(recursos)  # Convertir el valor a entero si es válido
        
        if years:  # Verificar si el valor no está vacío
            años = int(years)  # Convertir el valor a entero si es válido

        if natalidad:  # Verificar si el valor no está vacío
            tasa_natalidad = float(natalidad)  # Convertir el valor a entero si es válido
        
        if mortalidad:  # Verificar si el valor no está vacío
            tasa_mortalidad = float(mortalidad)  # Convertir el valor a entero si es válido
        
        if recursos_encontrados:  # Verificar si el valor no está vacío
            recursos_por_expedicion = int(recursos_encontrados)  # Convertir el valor a entero si es válido
        
        if probabilidad_recursos:  # Verificar si el valor no está vacío
            probabilidad_exito_expedicion = float(probabilidad_recursos)  # Convertir el valor a entero si es válido

        if consumo_persona:  # Verificar si el valor no está vacío
            consumo_recursos_por_persona = int(consumo_persona)  # Convertir el valor a entero si es válido
        
        #Enfermedad
        if transmicion:  # Verificar si el valor no está vacío
            beta = float(transmicion)  # Convertir el valor a entero si es válido
        else: 
            beta=0.00
        if mortalidad_enfermedad:  # Verificar si el valor no está vacío
            tasa_mortalidad_enfermedad = float(mortalidad_enfermedad)  # Convertir el valor a entero si es válido
        else: 
            tasa_mortalidad_enfermedad=0.00
        if recuperacion:  # Verificar si el valor no está vacío
            gamma = float(recuperacion)  # Convertir el valor a entero si es válido
        else: 
            gamma=0.00
        if infectados:  # Verificar si el valor no está vacío
            proporcion_individuos_infectados = float(infectados)  # Convertir el valor a entero si es válido
        else: 
            proporcion_individuos_infectados=0.00

        valores_simulacion = {
            'poblacion_inicial': poblacion_inicial,
            'recursos_iniciales': recursos_iniciales,
            'num_anios':años,
            'tasa_natalidad': tasa_natalidad,
            'tasa_mortalidad': tasa_mortalidad,
            'consumo_recursos_por_persona': consumo_recursos_por_persona ,
            'recursos_por_expedicion': recursos_por_expedicion ,
            'probabilidad_exito_expedicion': probabilidad_exito_expedicion,
            'proporcion_individuos_infectados': proporcion_individuos_infectados,
            'beta': beta,
            'gamma': gamma,
            'tasa_mortalidad_enfermedad': tasa_mortalidad_enfermedad,
        }
        return valores_simulacion

    def transition_to_simulation(self):
        valores_simulacion = self.obtenerValores()
        sim.ejecutar_simulacion(valores_simulacion)
        self.destroy()  # Cierra la ventana actual
        ventana = SimuladorVentana()  # Crea una instancia de SimuladorVentana
        ventana.mainloop()  # Comienza el ciclo de eventos de la ventana

   