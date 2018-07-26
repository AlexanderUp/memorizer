# encoding:utf-8
# memorizer main file

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock


import time

class Memorizer(Widget):

    def update(self, delta=30):
        start = time.time()
        elapsed_time = time.time -  start
        # while elapsed_time <= delta:
        while True:
            if elapsed_time <= delta:
                time_left = delta - elapsed_time
                time.sleep(1)
                # function showing time left to be called here
            else:
                break
        return None

class MemorizerApp(App):
    def build(self):
        self.title = 'Memorizer'
        memorizer = Memorizer()
        Clock.schedule_interval(memorizer.update, 1.0)
        return memorizer


if __name__ == '__main__':
    MemorizerApp().run()
