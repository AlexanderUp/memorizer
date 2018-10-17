# encoding:utf-8
# memorizer main file

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
# from kivy.properties import BooleanProperty
# from kivy.properties import StringProperty


import random


# count = 10
count = 3

class CustomLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        print('CustomLayout.__init__:')
        print('Args recieved: {}'.format(args))
        print('Kwargs recieved: {}'.format(kwargs))
        super(CustomLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='Memorize this number:', font_size=70, size_hint=(1, 0.33)))
        self.add_widget(Label(text=str(self.number()), font_size=70, size_hint=(1, 0.33)))
        self.time_widget = Label(text='Countdowning commenced!', font_size=70, size_hint=(1, 0.33))
        self.add_widget(self.time_widget)
        print('self dict:')
        for d in self.__dict__.keys():
            print('{}: {}'.format(d, self.__dict__[d]))
        Clock.schedule_interval(self.time_left, 1.0)


    def number(self):
        return random.randint(100000, 999999)

    def time_left(self, *args, **kwargs):
        print('MemoScreen.time_left:')
        print('Args recieved: {}'.format(args))
        print('Kwargs recieved: {}'.format(kwargs))
        global count
        print('time_var: {}'.format(count))
        if count:
            self.time_widget.text = '{} secs left'.format(count)
            count -= 1
        else:
            self.time_widget.text = 'Time is over!'
            Clock.unschedule(self.time_left)
            print('Time is over!')


class MemoScreen(Screen):

    def __init__(self, *args, **kwargs):
        print('MemoScreen.__init__:')
        print('Args recieved: {}'.format(args))
        print('Kwargs recieved: {}'.format(kwargs))
        super(MemoScreen, self).__init__(**kwargs)
        self.add_widget(CustomLayout())


class CheckScreen(Screen):
    pass


class MemorizerApp(App):

    def build(self):
        self.title = 'Memorizer'
        sm = ScreenManager()
        sm.add_widget(MemoScreen(name='MemoScr'))
        sm.add_widget(CheckScreen(name='CheckScr'))
        return sm


if __name__ == '__main__':
    MemorizerApp().run()
