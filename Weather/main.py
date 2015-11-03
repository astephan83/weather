'''Initialize GUI and other code here'''

import sys
from PySide import QtGui
import GUI_Main_Screen 
import database_queries as dq
import Weather


def main():

    icon_desc = dq.save_city('Tampa, FL', 'K')
    #print(icon_desc)
    #cities = dq.delete_setting(0)
    #print(cities)

if __name__ == '__main__':
    main()