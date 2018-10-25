# encoding:utf-8
# memorizer main file

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from kivy.config import Config
Config.set('graphics', 'height', '288')
Config.set('graphics', 'width', '512')
Config.set('graphics', 'resizable', '0')

import sys

try:
    from memo_app_screens import MemoScreen
    from memo_app_screens import CheckScreen
    from memo_app_screens import ResultScreen
except ImportError:
    print('Can\'t import some modules!')
    sys.exit()
else:
    print('Modules imported successfully by memorizer!')


try:
    import config
except ImportError:
    print('Can\'t import configuration file! - memorizer')
else:
    print('Config imported successfully by memorizer!')


class MemorizerApp(App):

    def build(self):
        self.title = 'Memorizer'
        # global sm
        config.sm = ScreenManager()
        config.sm.add_widget(MemoScreen(name='MemoScr'))
        config.sm.add_widget(CheckScreen(name='CheckScr'))
        config.sm.add_widget(ResultScreen(name='ResultScr'))
        print('random_number: {}'.format(config.random_number))
        return config.sm


if __name__ == '__main__':
    MemorizerApp().run()
