# encoding:utf-8
# CheckLayout for memorizer app

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

try:
    import config
except ImportError:
    print('Can\'t import configuration file! - check_layout')
else:
    print('Config imported successfully by check_layout!')

class CheckLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(CheckLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='Check Screen', font_size=70, size_hint=(1, .3)))
        self.add_widget(Label(text='Previously displayed number is:', font_size=70, size_hint=(1, .3)))
        self.answer = TextInput(font_size=40, size_hint=(.5, .1), pos_hint = {'center_x':.5}, multiline=False)
        self.answer_timer = Label(text='Time left', font_size=70, size_hint=(1, .3))
        self.add_widget(self.answer)
        self.add_widget(self.answer_timer)
        self.answer.bind(text=self.check_answer)

    def check_answer(self, *args, **kwargs):
        print('Args rcvd: {}, {} and {}'.format(config.random_number, args, kwargs))
        print('check_answer method called!')
        if self.answer.text == str(config.random_number):
            print('You are right')
            config.sm.current = 'ResultScr'
