import tkinter as tk
from tkinter import font
from inputs import ColonosSimulator
from conoce import ConoceMasWindow

class LeftFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # Lado Izquierdo
        self.logo = tk.PhotoImage(file="images/logo.png")
        self.logo_label = tk.Label(self, image=self.logo, bg=self['bg'])
        self.logo_label.pack(pady=(80, 10))
        
        oleo_font = font.Font(family="Oleo Script", size=24)
        self.title_label = tk.Label(self, text="Colonos del Horizonte", font=oleo_font, bg=self['bg'], fg="white")
        self.title_label.pack(pady=(0, 20))

class RightFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # Lado Derecho
        self.nave1 = tk.PhotoImage(file="images/nave1.png")
        self.nave2 = tk.PhotoImage(file="images/nave2.png")
        self.nave1_label = tk.Label(self, image=self.nave1, bg=self['bg'])
        self.nave1_label.grid(row=0, column=0, padx=(10, 0), pady=(10, 0))

        self.nave2_label = tk.Label(self, image=self.nave2, bg=self['bg'])
        self.nave2_label.grid(row=0, column=1, padx=(0, 10), pady=(10, 0))

        fredoka_font = font.Font(family="Fredoka", size=20)
        self.welcome_label = tk.Label(self, text="Bienvenidos astronautas", font=fredoka_font, bg=self['bg'], padx=20)
        self.welcome_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))

        self.inicio_btn = tk.Button(self, text="Inicio", font=fredoka_font, bg=master.blue_color, fg="white", padx=20, pady=10, command=self.transition_to_simulator, cursor="hand2", activebackground="#5762D5")
        self.inicio_btn.grid(row=2, column=0, columnspan=2, pady=(0, 10), sticky="ew")

        self.conoce_btn = tk.Button(self, text="Conoce más", font=fredoka_font, bg=master.blue_color, fg="white", padx=20, pady=10, command=self.transition_to_help, cursor="hand2", activebackground="#5762D5")
        self.conoce_btn.grid(row=3, column=0, columnspan=2, sticky="ew")

        self.navemov = tk.PhotoImage(file="images/navemov.png")
        self.navemov_label = tk.Label(self, image=self.navemov, bg=self['bg'])
        self.navemov_label.grid(row=4, column=1, sticky="se", padx=(0, 10), pady=(0, 10))

    def transition_to_simulator(self):
        self.master.destroy()  # Cierra la ventana principal
        ColonosSimulator().mainloop()  # Abre la nueva ventana 

    def transition_to_help(self):
        ConoceMasWindow(self.master)

class App(tk.Tk):
    def __init__(self, title, size) -> None:
        # Inicializar la ventana
        super().__init__()  # Inicializa la ventana principal utilizando la clase base tk.Tk
        self.title(title)  # Establece el título de la ventana
        self.geometry(f'{size[0]}x{size[1]}')  # Establece el tamaño de la ventana
        self.mainsize = (size[0], size[1])  # Guarda el tamaño de la ventana en el atributo mainsize

        # Colores
        self.blue_color = "#051C3E"
        self.white_color = "white"

        # Fuentes
        self.oleo_font = font.Font(family="Oleo Script", size=24)
        self.fredoka_font = font.Font(family="Fredoka", size=20)

        # Inicializar el canvas
        self.setup_ui()

    def setup_ui(self):

        # Crear frames
        self.left_frame = LeftFrame(self, bg=self.blue_color)
        self.left_frame.pack(side="left", fill="both", expand=True)

        self.right_frame = RightFrame(self, bg=self.white_color)
        self.right_frame.pack(side="right", fill="both", expand=True)

        # Inicializar la aplicación
        self.mainloop()

if __name__ == "__main__":
    app = App("Simulador Colonos",(1000, 600))
