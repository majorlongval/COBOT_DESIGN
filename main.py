import tkinter as tk
from main_frame import Main_Frame


class MyApplication(tk.Tk):
    """Main Application of the cobot design"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("COBOT_DESIGN")
        self.geometry("1600x800")
        self.resizable(width=False, height=False)
        Main_Frame(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))

if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()
