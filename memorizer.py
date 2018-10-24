# encoding:utf-8
# memorizer main file

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

from kivy.config import Config
Config.set('graphics', 'height', '288')
Config.set('graphics', 'width', '512')
Config.set('graphics', 'resizable', '0')


import random


# count = 10
count = 1
# random_number = 0

class CustomLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        # print('CustomLayout.__init__:')
        # print('Args received: {}'.format(args))
        # print('Kwargs received: {}'.format(kwargs))
        super(CustomLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='Memorize this number:', font_size=70, size_hint=(1, 0.33)))
        self.add_widget(Label(text=str(self.number()), font_size=70, size_hint=(1, 0.33)))
        self.time_widget = Label(text='Countdowning commenced!', font_size=70, size_hint=(1, 0.33))
        self.add_widget(self.time_widget)
        Clock.schedule_interval(self.time_left, 1.0)


    def number(self):
        # return random.randint(100000, 999999)
        global random_number
        random_number = random.randint(100000, 999999)
        return random_number

    def time_left(self, *args, **kwargs):
        # print('MemoScreen.time_left:')
        # print('Args received: {}'.format(args))
        # print('Kwargs received: {}'.format(kwargs))
        global count
        print('time_var: {}'.format(count))
        if count:
            self.time_widget.text = '{} secs left'.format(count)
            count -= 1
        else:
            self.time_widget.text = 'Time is over!'
            Clock.unschedule(self.time_left)
            print('Time is over!')
            sm.current = 'CheckScr'

    def refresh_screen(self, *args, **kwargs):
        # return self.__init__(self, *args, **kwargs)
        return self.__init__()


class AnotherCustomLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        # print('AnotherCustomLayout.__init__:')
        # print('Args received: {}'.format(args))
        # print('Kwargs received: {}'.format(kwargs))
        super(AnotherCustomLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='Check Screen', font_size=70, size_hint=(1, .3)))
        self.add_widget(Label(text='Previously displayed number is:', font_size=70, size_hint=(1, .3)))
        self.answer = TextInput(font_size=40, size_hint=(.5, .1), pos_hint = {'center_x':.5}, multiline=False)
        self.answer_timer = Label(text='Time left', font_size=70, size_hint=(1, .3))
        self.add_widget(self.answer)
        self.add_widget(self.answer_timer)
        self.answer.bind(text=self.check_answer)

    def check_answer(self, *args, **kwargs):
        print('Args rcvd: {}, {} and {}'.format(random_number, args, kwargs))
        print('check_answer method called!')
        if self.answer.text == str(random_number):
            print('You are right')
            sm.current = 'ResultScr'

class ResultLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        # print('ResultLayout.__init__:')
        # print('Args received: {}'.format(args))
        # print('Kwargs received: {}'.format(kwargs))
        super(ResultLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='Congratulations!', font_size=70, size_hint=(1, .5)))
        self.add_widget(Button(text='Try again', on_press=self.to_memo_scr, font_size=70, size_hint=(1, .5)))

    def to_memo_scr(self, *args, **kwargs):
        print('to_memo_scr called!')
        # sm.remove_widget('MemoScr')
        # sm.add_widget(MemoScreen(name='MemoScr'))
        sm.current = 'MemoScr'



class MemoScreen(Screen):

    def __init__(self, *args, **kwargs):
        # print('MemoScreen.__init__:')
        # print('Args received: {}'.format(args))
        # print('Kwargs received: {}'.format(kwargs))
        super(MemoScreen, self).__init__(**kwargs)
        self.add_widget(CustomLayout())


class CheckScreen(Screen):

    def __init__(self, *args, **kwargs):
        # print('CheckScreen.__init__:')
        # print('Args received: {}'.format(args))
        # print('Kwargs received: {}'.format(kwargs))
        super(CheckScreen, self).__init__(**kwargs)
        self.add_widget(AnotherCustomLayout())


class ResultScreen(Screen):

    def __init__(self, *args, **kwargs):
        # print('ResultScreen.__init__:')
        # print('Args received: {}'.format(args))
        # print('Kwargs received: {}'.format(kwargs))
        super(ResultScreen, self).__init__(**kwargs)
        self.add_widget(ResultLayout())


class MemorizerApp(App):

    def build(self):
        self.title = 'Memorizer'
        global sm
        sm = ScreenManager()
        sm.add_widget(MemoScreen(name='MemoScr'))
        sm.add_widget(CheckScreen(name='CheckScr'))
        sm.add_widget(ResultScreen(name='ResultScr'))
        # print('Inherited: {}'.format(sm.__class__))
        # print('Based on: {}'.format(sm.__class__.__bases__))
        # print('sm dict: {}'.format(sm.__dict__))
        # print('MemorizerApp dict: {}'.format(MemorizerApp.__dict__))
        # print('ScreenManager dict: {}'.format(ScreenManager.__dict__))
        # print('sm dir: {}'.format(dir(sm)))
        # print('MemorizerApp dir: {}'.format(dir(MemorizerApp)))
        # print('ScreenManager dir: {}'.format(dir(ScreenManager)))
        print('random_number: {}'.format(random_number))
        return sm


if __name__ == '__main__':
    MemorizerApp().run()
