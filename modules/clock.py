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
date_label = Label(text=now.strftime("%A %d %B %Y"))
time_label = Label(text=now.strftime("%H:%M:%S"))

def init():
    """clock module init"""
    date_node = GridLayout(cols=1)

    date_node.add_widget(date_label)
    date_node.add_widget(time_label)

    return date_node

def update():
    """Clock update function"""
    now = datetime.now()
    date_label.text = now.strftime("%A %d %B %Y")
    time_label.text = now.strftime("%H:%M:%S")
