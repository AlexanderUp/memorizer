# encoding:utf-8
# StartLayout for memorizer app

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

import random

try:
    import config
except ImportError:
    print('Can\'t import configuration file! - start_layout')
else:
    print('Config imported successfully by start_layout!')


# try:
#     from memorizer import sm
# except ImportError:
#     print('Can\'t import sm!')
# else:
#     print('sm imported successfully!')


class StartLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(StartLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='Memorize this number:', font_size=70, size_hint=(1, 0.33)))
        self.add_widget(Label(text=str(self.number()), font_size=70, size_hint=(1, 0.33)))
        self.time_widget = Label(text='Countdowning commenced!', font_size=70, size_hint=(1, 0.33))
        self.add_widget(self.time_widget)
        Clock.schedule_interval(self.time_left, 1.0)


    def number(self):
        config.random_number = random.randint(100000, 999999)
        return config.random_number

    def time_left(self, *args, **kwargs):
        print('time_var: {}'.format(config.count))
        if config.count:
            self.time_widget.text = '{} secs left'.format(config.count)
            config.count -= 1
        else:
            self.time_widget.text = 'Time is over!'
            Clock.unschedule(self.time_left)
            print('Time is over!')
            config.sm.current = 'CheckScr'

    def refresh_screen(self, *args, **kwargs):
        # return self.__init__(self, *args, **kwargs)
        return self.__init__()
