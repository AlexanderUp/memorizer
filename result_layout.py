# encoding:utf-8
# ResultLayout for memorizer app

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


try:
    import config
except ImportError:
    print('Can\'t import configuration file! - result_layout')
else:
    print('Config imported successfully by result_layout!')


class ResultLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(ResultLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='Congratulations!', font_size=70, size_hint=(1, .5)))
        self.add_widget(Button(text='Try again', on_press=self.to_memo_scr, font_size=70, size_hint=(1, .5)))

    def to_memo_scr(self, *args, **kwargs):
        print('to_memo_scr called!')
        # sm.remove_widget('MemoScr')
        # sm.add_widget(MemoScreen(name='MemoScr'))
        config.sm.current = 'MemoScr'
