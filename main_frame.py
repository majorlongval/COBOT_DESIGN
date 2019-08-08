import tkinter as tk
from tkinter import ttk


class Main_Frame(tk.Frame):
    """A friendly little module"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.myimage = tk.PhotoImage(file="Mecanisme_2DDL_pic_small.png")
        self.image_label = ttk.Label(self, image=self.myimage)
        self.image_label.grid(row=0, column=1)
        
