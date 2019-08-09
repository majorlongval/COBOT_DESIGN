import tkinter as tk
from tkinter import ttk
from CLASSES import LabelInput


class Main_Frame(tk.Frame):
    """THE MAIN FRAME OF THE APP.
       THIS IS WHERE THE INTERACTIVE ROBOT WILL BE"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.Planar_cobot_img = tk.PhotoImage(file='Mecanisme_2DDL_pic_small.png')
        self.Planar_cobot_img_label = tk.Label(self, 
                                               image=self.Planar_cobot_img)
        self.Planar_cobot_img_label.grid(row=0, column=0)
        # Creating the numerical inputs
        dim_list = ['L1', 'L2', 'L3', 'L4', 'L5',
                    'l11', 'l12', 'l21', 'l22', 'l3', 'l4', 'l5']
        mass_list = ['m11', 'm12', 'm21', 'm22', 'm3', 'm4',
                     'm5', 'mp1', 'mp2', 'mp3']
        self.inputs = {}
        Properties = tk.LabelFrame(self, text="Properties")
        Properties.grid(row=1, column=0)
        Dimensions = tk.LabelFrame(Properties, text="Dimensions")
        Dimensions.grid(row=0, column=0, sticky=tk.S)
        Masses = tk.LabelFrame(Properties, text="Masses")
        Masses.grid(row=0, column=1, sticky=tk.S)
        pos = 0
        for item in dim_list:
            self.inputs[item] = LabelInput(Dimensions, item,
                                           input_class=ttk.Spinbox,
                                           input_var=tk.DoubleVar(value=0.1),
                                           input_args={'from_': 0.1,
                                            "to": 10, "increment": .1})
            self.inputs[item].grid(row=pos, column=0, sticky=tk.E)
            pos += 1

        pos = 0
        for item in mass_list:
            self.inputs[item] = LabelInput(Masses, item,
                                           input_class=ttk.Spinbox,
                                           input_var=tk.DoubleVar(value=0.1),
                                           input_args={'from_': 0.1,
                                            "to": 10, "increment": .1})
            self.inputs[item].grid(row=pos, column=0, sticky=tk.E)
            pos += 1
        # Creating a Canvas to the right of the robot image
        self.canvas_width = 800
        self.canvas_height = 600
        self.canvas_base = 3*self.canvas_height//4
        self.canvas = tk.Canvas(self, background='grey',
                                width=self.canvas_width,
                                height=self.canvas_height)
        self.canvas.grid(row=0, column=1, rowspan=2)
        self.update()
        self.canvas.create_rectangle(50, 550, 700, 599, fill="black")
        self.canvas.create_polygon(260, 550, 320, 550, 290, 460, fill='red')
        self.canvas.create_oval(290, 460, 20, 20, fill="blue")
        print(self.canvas.winfo_height())
        