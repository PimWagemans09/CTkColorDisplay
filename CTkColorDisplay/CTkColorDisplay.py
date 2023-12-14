from typing import Optional, Tuple, Union
import customtkinter as ctk

class CTkColorDisplay(ctk.CTkFrame):
    def __init__(self, master: any, display_color:str = "#ffffff"):
        super().__init__(master)
        self._master = master
        self.configure(fg_color="transparent")
        