# encoding:utf-8
# memorizer main file

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty


import random


# count = 10
count = 2

class MemoScreen(Screen):

    scr = BooleanProperty(False)

    def number(self):
        return random.randint(100000, 999999)

    def time_left(self, *kwargs):
        global count
        time_ = str(count) + ' secs left'
        if count:
            count -= 1
            print('count decreased!')
        else:
            time_ = 'Time is over!'
            Clock.unschedule(self.time_left)
            print('Unscheduled!')
            print('BooleanProperty before: {}'.format(self.scr))
            self.scr = True
            print('BooleanProperty: {}'.format(self.scr))
        # return time_
        self.ids.time_left.text = time_
        print('self.ids... {}'.format(self.ids.time_left.text))
        # # return None # ????
        return self.ids.time_left.text

    def on_scr(self, *kwargs):
        print('on_scr called!')
        print('*kwargs: {}'.format(kwargs))
        # return sm.current('Check')
        # check = CheckScreen()
        # return check


class CheckScreen(Screen):
    pass

class MemorizerApp(App):

    def build(self):
        self.title = 'Memorizer'
        sm = ScreenManager()
        sm.add_widget(MemoScreen(name='MemoScr'))
        sm.add_widget(CheckScreen(name='CheckScr'))
        memo = MemoScreen()
        Clock.schedule_interval(memo.time_left, 1.0)
        return sm



if __name__ == '__main__':
    MemorizerApp().run()
