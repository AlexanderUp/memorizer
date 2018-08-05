# encoding:utf-8
# memorizer main file

from kivy.app import App
# from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.clock import Clock
# from kivy.properties import ObjectProperty


import time
import random


TIME = 10

class Memorizer(BoxLayout):

    def time_left(self, time=TIME):
        while time:
            time -= 1
            # time.sleep(1.0)
        return None

    def number(self):
        return random.randint(0, 999999)

class MemorizerApp(App):
    def build(self):
        self.title = 'Memorizer'
        memorizer = Memorizer()
        # Clock.schedule_interval(memorizer.time_left, 1.0)
        return memorizer


if __name__ == '__main__':
    MemorizerApp().run()
