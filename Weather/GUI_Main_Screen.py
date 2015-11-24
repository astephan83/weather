# using tkinter

from tkinter import *
from tkinter import ttk

class GUI_Main_Screen(Frame):
    """class for main weather screen GUI"""
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.content = ttk.Frame(self)
        self.frame = ttk.Frame(self.content, borderwidth=5, relief="sunken", width=200, height=100)
        self.citylbl = ttk.Label(self.content, text="City")
        self.city = ttk.Entry(self.content)
        self.statelbl = ttk.Label(self.content, text="State")
        self.state = ttk.Entry(self.content)

        self.kelvin_var = BooleanVar()
        self.celcius_var = BooleanVar()
        self.threevar = BooleanVar()
        self.kelvin_var.set(True)
        self.celcius_var.set(False)
        self.threevar.set(True)

        # declarations
        self.kelvin = ttk.Checkbutton(self.content, text="Kelvin", variable=self.kelvin_var, onvalue=True)
        self.celcius = ttk.Checkbutton(self.content, text="Celcius", variable=self.celcius_var, onvalue=True)
        self.three = ttk.Checkbutton(self.content, text="Three", variable=self.threevar, onvalue=True)
        self.search = ttk.Button(self.content, text="Search")
        self.cancel = ttk.Button(self.content, text="Cancel")

        # placement
        self.content.grid(column=0, row=0)
        self.frame.grid(column=0, row=0, columnspan=3, rowspan=4)
        self.citylbl.grid(column=3, row=0, columnspan=2)
        self.city.grid(column=3, row=1, columnspan=2)
        self.statelbl.grid(column=3, row=2, columnspan=2)
        self.state.grid(column=3, row=3, columnspan=2)
        self.kelvin.grid(column=0, row=5)
        self.celcius.grid(column=1, row=5)
        self.three.grid(column=2, row=5)
        self.search.grid(column=4, row=5)
        self.cancel.grid(column=5, row=5)

    # bindings
    #search.bind(Weather.forcast(city.get(),state.get()))