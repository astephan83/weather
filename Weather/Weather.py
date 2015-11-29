'''
Group B
Jamie Wimsatt, Zack Powell, Amanda Stephan
Weather Application:
owm application code: 77dbc172aee4836d569ffcc9c4715602
'''

import pyowm
import sys
from time import localtime, time
from math import *
import database_queries
import datetime

owm = pyowm.OWM('77dbc172aee4836d569ffcc9c4715602')
FORCAST_DAYS = 5
DAYOFWEEK = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
TEMP_UNIT = {'K':'kelvin', 'C':'celsius', 'F':'fahrenheit'}

# Search for current weather in 'City, state'
def forcast(city, state=None, tmp_unit='F'):
    if state == None:
        rqsted_city = city
    else:
        rqsted_city = city + ', ' + state

    forcast = owm.daily_forecast(rqsted_city, limit=FORCAST_DAYS)
    cast = forcast.get_forecast()
    lst = cast.get_weathers()
    #print(city)
    dates = get_dates()
   
    return_list = []
    for weather, date, temp in zip(cast,dates):
       return_list.append((weather.get_status(), date, 'database_queries.get_icon(None, weather.get_status())', temp))
    return return_list # returns list of ['weather', (year, month, day, day_of_week), icon, (min_temp, max_temp)]

# get five dates starting from today
#
#    returns list of tuples (year, month, day, day_of_week)
def get_dates():
    dates = []
    for i in range(FORCAST_DAYS + 1):
        dates.append((localtime(time() + 24*3600 * i)[0], localtime(time() + 24*3600*i)[1], localtime(time() + 24*3600*i)[2], DAYOFWEEK[localtime(time() + 24*3600*i)[6]]))

    # return a list of tuples(year, month, day) for FORCAST_DAYS
    return dates

# get the forcast for one day 
#    date should be a list of year, month, day
#    returns a list of tuples of ints (min_temp, max_temp)
def one_day_forcast(forcast, city, state=None, tmp_unit='F'):
    dates = []
    weathers = []
    w = []
    temps = []

    for i in range(FORCAST_DAYS + 1):
        dates.append((localtime(time() + 24*3600 * i)[0], localtime(time() + 24*3600*i)[1], localtime(time() + 24*3600*i)[2], 12, 0))
    
    for date in dates:
        weathers.append(forcast.get_weather_at(date))

    if state != None:
        for weather in weathers:
            w.append(weather.weather_at_place(city + ',' + state))
    else:
        for weather in weathers:
            w.append(weather.weather_at_place(city))

    for each in w:
        temp.append(each.get_temperature(TEMP_UNIT[tmp_unit])['temp_min'], each.get_temperature(TEMP_UNIT[tmp_unit])['temp_max'])
    return temp # list of tuples of ints

# get the current tempurature
#  
#    returns a tuple of ints
def temp(city, state=None, tmp_units='F'):
    if state != None:
        observation = owm.weather_at_place(city + ',' + state)
    else:
        observation = owm.weather_at_place(city)
    weather = observation.get_weather()
    temps = weather.get_temperature(TEMP_UNIT[tmp_units])

    return temps[2], temps[3]