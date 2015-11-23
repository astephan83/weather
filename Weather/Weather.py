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

'''

import sqlite3
import pyowm
import sys
from PySide.QtCore import *
from PySide.QtGui import *
import datetime
from time import localtime, time
from math import *
from builtins import super

#app = QApplication(sys.argv)
#win = QWidget()
owm = pyowm.OWM('77dbc172aee4836d569ffcc9c4715602')
FORCAST_DAYS = 5

# Search for current weather in 'City, state'
def forcast(city, state=None):
    if state == None:
        rqsted_city = city
    else:
        rqsted_city = city + ', ' + state

    forcast = owm.daily_forecast(rqsted_city, limit=FORCAST_DAYS)
    cast = forcast.get_forecast()
    lst = cast.get_weathers()
    print(city)
    for weather in cast:
        print(weather.get_reference_time('iso'), weather.get_status())
    print()

# get five dates starting from today
def get_dates():
    dates = []
    for i in range(FORCAST_DAYS):
        dates.append((localtime(time() + 24*3600 * i)[0], localtime(time() + 24*3600*i)[1], localtime(time() + 24*3600*i)[2]))
    #print(number_of_days)

    # return a list of tuples(year, month, day) for FORCAST_DAYS
    return dates

# get the forcast for one day 
#    date should be a list of year, month, day
#    returns a weather object
def one_day_forcast(city, state=None, date=None):
    if date == None and state != None:
        observation = owm.daily_forecast(city + ", " + state)
    elif date < [localtime()[0], localtime()[1], localtime()[2]]:
        err = "Date can not be in the past"
        raise Exception(err)
    else:
        observation = owm.daily_forecast(city)
    
    return observation # weather object