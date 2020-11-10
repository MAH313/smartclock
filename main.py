"""Smart clock main controller"""

import locale
import importlib
import os
#import math

import kivy
from kivy.app import App
from kivy.clock import Clock
#from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
#from kivy.config import Config

#from datetime import timedelta

from modules import clock, countdown

module_list = [
    clock,
    countdown,
]

locale.setlocale(locale.LC_TIME, 'nl_NL.UTF-8')

kivy.require('1.11.1')


# kivy vars
ui_width = 800
ui_height = 510

class SmartClock(App):
    """Main app class"""

    def build(self):
        """main initialization function"""

        #modules[0] = modules.clock

        # for i in tree:
        #     print(i)
        #     importlib.import_module('modules.'+i)

        root = GridLayout(cols=3)

        Clock.schedule_interval(self.update, 1)

        #root.add_widget(self.modules[0].init())
        for i in range(len(module_list)):
            root.add_widget(module_list[i].init())

        return root

    def update(self, *args):
        """main update function"""

        for i in range(len(module_list)):
            module_list[i].update()

if __name__ == '__main__':
    Window.size = (ui_width, ui_height)

    SmartClock().run()
