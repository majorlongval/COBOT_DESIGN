import tkinter as tk
from tkinter import ttk
from CLASSES import LabelInput


class Main_Frame(tk.Frame):
    """THE MAIN FRAME OF THE APP.
       THIS IS WHERE THE INTERACTIVE ROBOT WILL BE"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.Planar_cobot_img = tk.PhotoImage(file='Mecanisme_2DDL_pic_small.png')
        self.Planar_cobot_img_label = tk.Label(self, image=self.Planar_cobot_img)
        self.Planar_cobot_img_label.grid(row=0, column=0)
        # Creating the numerical inputs 
        self.inputs = {}
        Dimensions = tk.LabelFrame(self, text="Dimensions")
        Dimensions.grid(row=1, column=0)
        self.inputs['L1'] = LabelInput(Dimensions, "L1",
                                       input_class=ttk.Spinbox,
                                       input_var=tk.DoubleVar(value=0.1),
                                       input_args={'from_': 0.1,
                                                   "to": 10, "increment": .1})
        self.inputs['L1'].grid(row=0, column=0)
        self.inputs['L2'] = LabelInput(Dimensions, "L2",
                                       input_class=ttk.Spinbox,
                                       input_var=tk.DoubleVar(value=0.1),
                                       input_args={'from_': 0.1,
                                                   "to": 10, "increment": .1})
        self.inputs['L2'].grid(row=1, column=0)
        self.inputs['L3'] = LabelInput(Dimensions, "L3",
                                       input_class=ttk.Spinbox,
                                       input_var=tk.DoubleVar(value=0.1),
                                       input_args={'from_': 0.1,
                                                   "to": 10, "increment": .1})
        self.inputs['L3'].grid(row=2, column=0)
        self.inputs['L4'] = LabelInput(Dimensions, "L4",
                                       input_class=ttk.Spinbox,
                                       input_var=tk.DoubleVar(value=0.1),
                                       input_args={'from_': 0.1,
                                                   "to": 10, "increment": .1})
        self.inputs['L4'].grid(row=3, column=0)
        # Creating a Canvas to the right of the robot image
        self.canvas = tk.Canvas(self, background='black')
        self.canvas.grid(row=0, column=1)