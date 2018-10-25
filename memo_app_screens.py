# encoding:utf-8
# screens for memorizer app

from kivy.uix.screenmanager import Screen


try:
    from start_layout import StartLayout
    from check_layout import CheckLayout
    from result_layout import ResultLayout
except ImportError:
    print('Can\'t import some layouts')
else:
    print('Layouts imported successfully!')


class MemoScreen(Screen):

    def __init__(self, *args, **kwargs):
        super(MemoScreen, self).__init__(**kwargs)
        self.add_widget(StartLayout())


class CheckScreen(Screen):

    def __init__(self, *args, **kwargs):
        super(CheckScreen, self).__init__(**kwargs)
        self.add_widget(CheckLayout())


class ResultScreen(Screen):

    def __init__(self, *args, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        self.add_widget(ResultLayout())
