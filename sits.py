# write module to count sq
from kivy.uix.label import Label


class Sits(Label):
    def __init__(self, total, **kwargs):
        self.current = 0
        self.total = total

        txt = "Squats left: " + str(self.total)

        super().__init__(text = txt,**kwargs)
        

    def next(self, *args):
        self.current += 1
        remain = max(0, self.total - self.current)
        self.text = "Squats left: " + str(remain)
        