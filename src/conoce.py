import tkinter as tk
from tkinter import font

class ConoceMasWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.initialize_window()
        self.create_ui()

    def initialize_window(self):
        self.title("Conoce Más")
        self.geometry("1200x1000")
        self.blue_color = "#051C3E"
        self.white_color = "white"

        self.custom_font = font.Font(family="Fredoka", size=14)

    def create_ui(self):
        self.create_nav_bar()
        self.create_content()
        self.create_paragraph()
        self.create_image_and_button()

    def create_nav_bar(self):
        nav_bar = tk.Frame(self.root, bg=self.blue_color)
        nav_bar.pack(side="top", fill="x")

        title_label = tk.Label(nav_bar, text="Conoce Más", 
                                font=self.custom_font, bg=self.blue_color, fg="white")
        title_label.pack(pady=5, padx=10, anchor="w")

    def create_content(self):
        content_frame = tk.Frame(self.root, bg=self.white_color)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)

        left_column = tk.Frame(content_frame, bg=self.white_color)
        left_column.pack(side="left", fill="both", expand=True)

        right_column = tk.Frame(content_frame, bg=self.white_color)
        right_column.pack(side="right", fill="both", expand=True)

        self.create_paragraph(left_column, "images/planeta1.png", "El simulador de Colonos, una herramienta interactiva que te permite explorar y comprender los patrones de crecimiento poblacional y la propagación de enfermedades a través de modelos matemáticos. En este simulador, hemos incorporado tres modelos fundamentales.")
        self.create_paragraph(left_column, "images/1.png", "Modelo de Crecimiento Exponencial: En este modelo, la población inicial y la tasa de natalidad desempeñan un papel clave. La población inicial establece el punto de partida, mientras que la tasa de natalidad determina la cantidad de nuevos individuos que se agregan diariamente. A medida que el tiempo avanza, la población crece de manera exponencial, sin restricciones.")

        self.create_paragraph(right_column, "images/2.png", "Modelo Logístico: La población inicial, la tasa de natalidad y la tasa de mortalidad juegan un papel esencial aquí. La población inicial establece el punto de partida y la tasa de natalidad afecta la tasa de crecimiento")
        self.create_paragraph(right_column, "images/3.png", "El Modelo de Propagación de Enfermedades simula cómo una enfermedad se propaga a través de la población, teniendo en cuenta la tasa de infección, recuperación y mortalidad. La tasa de infección determina la probabilidad de que una persona se contagie al estar en contacto con un individuo infectado. La tasa de recuperación indica la probabilidad de recuperación de una persona infectada")

    def create_paragraph(self, container, image_filename, text):
        paragraph_frame = tk.Frame(container, bg=self.white_color)
        paragraph_frame.pack(fill="both", expand=True, padx=10, pady=5)

        image = tk.PhotoImage(file=image_filename)
        image_label = tk.Label(paragraph_frame, image=image, bg=self.white_color)
        image_label.image = image
        image_label.pack(side="left", padx=10)

        text_label = tk.Label(paragraph_frame, text=text, font=self.custom_font, bg=self.white_color, justify="left", wraplength=350)
        text_label.pack(side="left", padx=10)

    def create_image_and_button(self):
        regresar_button = tk.Button(self.root, text="Regresar", font=self.custom_font, bg=self.blue_color, fg="white", borderwidth=0, command=self.return_main, cursor="hand2", activebackground="#5762D5")
        regresar_button.pack(side="bottom", anchor="center", pady=(0, 20))

    def return_main(self):
        self.destroy()
        from main import App # importación tardia, solo hace la importación hasta que se necesite.
        app = App("Simulador Colonos", (1000, 600))
        app.mainloop()

        

