'''
Group B
Jamie Wimsatt, Zack Powell, Amanda Stephan
Weather Application:
The application’s goal is to retrieve data about the weather 
using OpenWeatherMap API and displaying a week long forecast 
in an application using a GUI. The application will also allow 
users to save settings, such as cities and default temperature. 
Also have an option to print out the forecast.

77dbc172aee4836d569ffcc9c4715602

Initialize GUI and other code here
'''

import sys
from PySide import QtGui
import GUI_Main_Screen as GuiMain
import database_queries as dq
import Weather
from tkinter import *
from tkinter import ttk


def main():

    icon_desc = dq.save_city('Tampa, FL', 'K')
    #print(icon_desc)
    #cities = dq.delete_setting(0)
    #print(cities)
    root = Tk()
    app = GuiMain.GUI_Main_Screen(master=root)
    app.mainloop()
    root.destroy()


if __name__ == '__main__':
    main()