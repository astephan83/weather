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

app = QtGui.QApplication(sys.argv)

win = QtGui.QWidget()

owm = pyowm.OWM('77dbc172aee4836d569ffcc9c4715602')

# Will it be sunny tomorrow at this time in Milan (Italy) ?
forecast = owm.daily_forecast("Milan,it")
tomorrow = pyowm.timeutils.tomorrow()
forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)

# Search for current weather in London (UK)
observation = owm.weather_at_place('London,uk')
w = observation.get_weather()
print(w)                      # <Weather - reference time=2013-12-18 09:20, 
                              # status=Clouds>

# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(w.get_wind())
print(w.get_humidity())
print(w.get_temperature('celsius'))

# Search current weather observations in the surroundings of 
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)


win.resize(500, 400)   
win.setWindowTitle("Group B Weather. Welcome!") 
win.show()

sys.exit(app.exec_())