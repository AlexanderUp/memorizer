# encoding:utf-8
# memorizer main file

from kivy.app import App
# from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
from kivy.clock import Clock
# from kivy.properties import ObjectProperty


import time
import random


# count = 10
count = 3

class Memorizer(BoxLayout):

    def time_left(self, *kwargs): # ????
        print('Args: {}'.format(kwargs))
        global count
        print('count: {}'.format(count))
        time = str(count) + ' secs left'
        if count:
            count -= 1
            print('count decreased!')
        else:
            print("i'm here!")
            self.ids.time_left.text = 'Time is over!'
        self.ids.time_left.text = time
        return None

    def number(self):
        return random.randint(100000, 999999)

class MemorizerApp(App):

    def build(self):
        self.title = 'Memorizer'
        memorizer = Memorizer()
        Clock.schedule_interval(memorizer.time_left, 1.0)
        return memorizer


if __name__ == '__main__':
    MemorizerApp().run()
