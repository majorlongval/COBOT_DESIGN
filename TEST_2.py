import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.canvas = tk.Canvas(self, width=1024, height=768,
                                background='white')
        self.setup()
        self.canvas.pack(fill='both', expand=1)

    def setup(self):
        self.canvas.left = 0
        self.canvas.top = 0
        self.canvas.right = self.canvas.winfo_width()
        self.canvas.bottom = self.canvas.winfo_height()
        self.canvas.center_x = self.canvas.right // 2
        self.canvas.center_y = self.canvas.bottom // 2

        self.finish_line = self.canvas.create_rectangle((self.canvas.right-50,
                                                        0),
                                                        (self.canvas.right,
                                                         self.canvas.bottom),
                                                        fill='yellow',
                                                        stipple='gray50')
        self.after(200, self.setup)


App().mainloop()
