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
from PySide import QtGui
import datetime
from time import localtime, time

app = QtGui.QApplication(sys.argv)
win = QtGui.QWidget()
owm = pyowm.OWM('77dbc172aee4836d569ffcc9c4715602')
FORCAST_DAYS = 5

def findDataType(data):
    return str(data), str(type(data)), str(super(data.__class__, data))

# Will it be sunny tomorrow at this time in Milan (Italy) ?
forecast = owm.daily_forecast("Milan,it")
tomorrow = pyowm.timeutils.tomorrow()
forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)

# Search for current weather in 'City, state'
def forcast(city, state=None):
    if state == None:
        rqsted_city = city
    else:
        rqsted_city = city + ', ' + state
    
    observation = owm.weather_at_place(rqsted_city) # AssurtionError if not string
    forcast = owm.daily_forecast(rqsted_city, limit=FORCAST_DAYS)
    cast = forcast.get_forecast()
    lst = cast.get_weathers()
    print(city)
    for weather in cast:
        print(weather.get_reference_time('iso'), weather.get_status())
    print()

# get five dates starting from today
def get_dates():
    number_of_days = []
    for i in range(FORCAST_DAYS):
        number_of_days.append(datetime.date.today() + datetime.timedelta(days=i))

    days = []
    months = []
    years = []
    for dates in number_of_days:
        #print(dates)
        years.append(str(dates)[0:4])
        months.append(str(dates)[5:7])
        days.append(str(dates)[8:])

    # return a tuple of lists for five days
    return years, months, days

w = observation.get_weather()
#print(w)                      # <Weather - reference time=2013-12-18 09:20, status=Clouds>


print(findDataType(w.get_temperature()))


# Search current weather observations in the surroundings of 
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)

'''
FUNCTIONS FOR GUI
'''
class Weather:
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    # search button (takes info from user to search for city)
    def search(self, city_state=None, zip=None):
        if zip != None:
            self._observation = owm.weather_at_place(zip)
        if city_state != None:
            self._observation = owm.weather_at_place(city_state)
        else:
            return
    # dispaly funciton
    def display(self):
        pass


    
# history tab click (max 10)

# saved cities tab (from database)

# save button (saves current search)

# setting icon (bings up new window with settings)

# city and state text box (input from user)

# zip text box (input from user)

