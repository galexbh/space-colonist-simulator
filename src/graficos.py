import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from results import SimuladorVentana
import sim

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulación de Población y Recursos")

        # Inicialización
        self.paso_actual = 0
        self.animating = False

        # Crear el gráfico
        self.fig = Figure(figsize=(10, 5))
        self.ax = self.fig.add_subplot(1,1,1)
        self.line1, = self.ax.plot([], [], label="Población", color="blue")
        self.line2, = self.ax.plot([], [], label="Recursos", color="green")
        self.ax.set_xlabel("Años")
        self.ax.set_ylabel("Cantidad")
        self.ax.legend()
        self.ax.grid(True)
        self.ax.set_xlim(0, sim.num_anios)
        self.ax.set_ylim(0, max(sim.poblacion_inicial, sim.recursos_iniciales) * 1.5)

        # Anotación para mostrar datos
        self.annotation = self.ax.annotate('', xy=(0, 0), xytext=(10,10), textcoords='offset points', # offset points = desplazamiento en puntos desde el punto xy.
                                           bbox=dict(boxstyle="round", fc="w"),
                                           arrowprops=dict(arrowstyle="->"))
        self.annotation.set_visible(False)

        # Incrustar el gráfico en tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Conectar el evento de movimiento del ratón
        self.canvas.mpl_connect('motion_notify_event', self.on_motion)

        # Variables para Checkbuttons
        self.show_poblacion = tk.BooleanVar(value=True)
        self.show_recursos = tk.BooleanVar(value=True)

        # Crear Checkbuttons
        self.poblacion_check = ttk.Checkbutton(master, text="Mostrar Población", variable=self.show_poblacion, command=self.update_graph)
        self.poblacion_check.pack(side=tk.LEFT)

        self.recursos_check = ttk.Checkbutton(master, text="Mostrar Recursos", variable=self.show_recursos, command=self.update_graph)
        self.recursos_check.pack(side=tk.LEFT)

        # Crear botones
        self.play_button = ttk.Button(master, text="Reproducir", command=self.play_event)
        self.play_button.pack(side=tk.LEFT)
        self.pause_button = ttk.Button(master, text="Pausar", command=self.pause_event)
        self.pause_button.pack(side=tk.LEFT)
        self.forward_button = ttk.Button(master, text="Adelantar", command=self.forward_event)
        self.forward_button.pack(side=tk.LEFT)
        self.backward_button = ttk.Button(master, text="Retroceder", command=self.backward_event)
        self.backward_button.pack(side=tk.LEFT)

    def update_graph(self, actualiza_paso=0):
        self.paso_actual += actualiza_paso
        if self.paso_actual > sim.num_anios:
            self.paso_actual = sim.num_anios

        if self.show_poblacion.get():
            self.line1.set_data(range(self.paso_actual + 1), sim.poblacion[:self.paso_actual + 1])
            print(sim.poblacion[:self.paso_actual + 1])
        else:
            self.line1.set_data([], [])

        if self.show_recursos.get():
            self.line2.set_data(range(self.paso_actual + 1), sim.recursos[:self.paso_actual + 1])
        else:
            self.line2.set_data([], [])

        self.canvas.draw()

    def on_motion(self, event):
        if not event.xdata or not event.ydata:  # Si las coordenadas del ratón están fuera del gráfico
            self.annotation.set_visible(False)
            self.canvas.draw_idle()
            return

        year = round(event.xdata) #obtener el año redondeando la coordenada x del ratón
        if 0 <= year <= sim.num_anios: # si el año obtenido está dentro del rango válido de la simulación. 
            y_poblacion = sim.poblacion[year]
            y_recursos = sim.recursos[year]

            # Mostrar la anotación con los datos
            self.annotation.xy = (year, max(y_poblacion, y_recursos))
            self.annotation.set_text(f"Año: {year}\nPoblación: {y_poblacion}\nRecursos: {y_recursos}")
            self.annotation.set_visible(True)
        else:
            self.annotation.set_visible(False)

        self.canvas.draw_idle()


    def play_event(self):
        self.animating = True
        self.update_animation()

    def update_animation(self):
        if self.animating:
            self.update_graph(1)
            self.master.after(500, self.update_animation)

    def pause_event(self):
        self.animating = False

    def forward_event(self):
        self.paso_actual += 1
        if self.paso_actual > sim.num_anios:
            self.paso_actual = sim.num_anios
        self.update_graph()

    def backward_event(self):
        print(f"Antes: {self.paso_actual}")
        self.paso_actual -= 1
        print(f"Después: {self.paso_actual}")
        if self.paso_actual < 0:
            self.paso_actual = 0
        self.update_graph()


root = tk.Tk()
app = App(root)
root.mainloop()