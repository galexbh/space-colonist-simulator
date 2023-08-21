import tkinter as tk
from tkinter import font

# Constantes de color
BLUE_COLOR = "#051C3E"
WHITE_COLOR = "white"
ORANGE_COLOR = "#F7AD32"
RED_COLOR = "#932025"
ORANGE_BUTTON_COLOR = "#FE8B14"

class SimuladorVentana(tk.Tk):

    def __init__(self):
        super().__init__()
    
        self.CUSTOM_FONT = font.Font(family="Fredoka", size=14)
        self.TITLE_FONT = font.Font(family="Fredoka", size=24, weight="bold")
        
        self.initialize_window()
        self.create_ui()

    def initialize_window(self):
        self.title("Simulador Colonos")
        self.geometry("1200x600")


    def create_ui(self):
        self.create_blue_bar()
        self.create_content_frame()
        self.create_footer()

    def create_blue_bar(self):
        self.blue_bar = tk.Frame(self, bg=BLUE_COLOR)
        self.blue_bar.pack(side="top", fill="x")
        
        title_label = tk.Label(
            self.blue_bar, 
            text="Colonos del Horizonte", 
            font=self.CUSTOM_FONT, 
            bg=BLUE_COLOR, 
            fg=WHITE_COLOR
        )
        title_label.pack(pady=5, padx=10, anchor="w")

    def create_content_frame(self):
        self.content_frame = tk.Frame(self, bg=WHITE_COLOR)
        self.content_frame.pack(fill="both", expand=True)
        
        results_label = tk.Label(
            self.content_frame, 
            text="Resultados de la simulación", 
            font=self.TITLE_FONT, 
            fg=ORANGE_COLOR, 
            bg=WHITE_COLOR
        )
        results_label.pack(pady=20)

    def create_footer(self):
        self.footer_frame = tk.Frame(self, bg=WHITE_COLOR)
        self.footer_frame.pack(side="bottom", fill="x")
        
        button_frame = tk.Frame(self.footer_frame, bg=WHITE_COLOR)
        button_frame.pack()

        reiniciar_button = self._create_custom_button(
            button_frame, 
            text="Reiniciar simulación", 
            bg=RED_COLOR
        )
        reiniciar_button.pack(side="left", padx=10, pady=10)

        ver_datos_button = self._create_custom_button(
            button_frame, 
            text="Ver datos", 
            bg=ORANGE_BUTTON_COLOR,
            cursor="hand2"
        )
        ver_datos_button.pack(side="right", padx=10, pady=10)

    def _create_custom_button(self, parent, text, bg):
        return tk.Button(
            parent, 
            text=text, 
            font=self.CUSTOM_FONT, 
            bg=bg, 
            fg=WHITE_COLOR
        )
