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

owm = pyowm.OWM('77dbc172aee4836d569ffcc9c4715602')
FORCAST_DAYS = 5
DAYOFWEEK = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}

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
    for weather, date in zip(cast,dates):
       return_list.append((weather.get_status(), date, database_queries.get_icon(None, weather.get_status())))
    return return_list # returns list of strings

# get five dates starting from today
def get_dates():
    dates = []
    for i in range(FORCAST_DAYS + 1):
        dates.append((localtime(time() + 24*3600 * i)[0], localtime(time() + 24*3600*i)[1], localtime(time() + 24*3600*i)[2], DAYOFWEEK[localtime(time() + 24*3600*i)[6]]))

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