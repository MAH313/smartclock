"""Clock module"""
from datetime import datetime

import kivy
#from kivy.app import App
#from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
#from kivy.core.window import Window

#class module:

now = datetime.now()
counting_to = datetime(int(now.strftime('%Y'))+1, 1, 1)

label = Label(text="Nog in dit jaar")

time_label = Label(text='')

def init():
    """clock module init"""
    date_node = GridLayout(cols=1)

    delta = counting_to - datetime.now()
    time_label.text = generateTimeStr(delta)

    date_node.add_widget(label)
    date_node.add_widget(time_label)

    return date_node

def update():
    """Clock update function"""
    delta = counting_to - datetime.now()

    time_label.text = generateTimeStr(delta)

def generateTimeStr(timedelta):
    """generates a time string"""
    days = timedelta.days
    seconds = timedelta.seconds

    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d dagen %d uren %d minuten en %d seconden" % (days, hour, minutes, seconds)
