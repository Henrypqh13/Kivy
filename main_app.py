# write our app here
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.uix.popup import Popup
from instructions import *
from seconds import Seconds
from sits import Sits
from runner import Runner
import ruffier

age = 0
name = ""
p1,p2,p3 = 0,0,0

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False
    

class InsScr(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        instr = Label(text = txt_instruction) 
        line1 = Label(text = "Name", size_hint = (0.2, 1))
        self.name_input = TextInput(multiline = False)
        line2 = Label(text = "Age", size_hint = (0.2, 1))
        self.age_input = TextInput(multiline = False)
        self.btn = Button(text = "Start", size_hint = (0.3, 0.2), pos_hint = {"center_x":0.5})
        
        hlayout1 = BoxLayout(size_hint = (1, 0.1))
        hlayout1.add_widget(line1)
        hlayout1.add_widget(self.name_input)
        
        hlayout2 = BoxLayout(size_hint = (1, 0.1))
        hlayout2.add_widget(line2)
        hlayout2.add_widget(self.age_input)

        vLayout = BoxLayout(orientation = "vertical")
        vLayout.add_widget(instr)
        vLayout.add_widget(hlayout1)
        vLayout.add_widget(hlayout2)
        vLayout.add_widget(self.btn)

        self.add_widget(vLayout)

        self.btn.on_press = self.next

    def next(self):
        global name
        name = self.name_input.text
        global age
        age = check_int(self.age_input.text)
        if age == False or age < 7:
            age = 7
            self.age_input.text = "7"
            Popup(title='Error', content=Label(text='Age must be a number greater than 7'), size_hint=(None, None), size=(400, 400)).open()

        else:
            self.manager.current = "2"

        

class PulseScr(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.next_scr = False

        instr1 = Label(text = txt_test1) 
        line1 = Label(text = "Enter the result", size_hint = (0.2, 1))
        self.p1_input = TextInput(multiline = False)
        self.p1_input.set_disabled(True)
        self.btn = Button(text = "Next", size_hint = (0.3, 1), pos_hint = {"center_x":0.5})
        self.btn1 = Button(text = "Back", size_hint = (0.3, 1), pos_hint = {"center_x":0.5})
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done = self.finished)


        hlayout1 = BoxLayout(size_hint = (1, 0.2))
        hlayout2 = BoxLayout(size_hint = (1, 0.2))
        hlayout2.add_widget(self.btn1)
        hlayout2.add_widget(self.btn)

        hlayout1.add_widget(line1)
        hlayout1.add_widget(self.p1_input)

        vLayout = BoxLayout(orientation = "vertical")
        vLayout.add_widget(instr1)
        vLayout.add_widget(self.lbl_sec)
        vLayout.add_widget(hlayout1)
        vLayout.add_widget(hlayout2)

        self.add_widget(vLayout)
        self.btn.on_press = self.next
        self.btn1.on_press = self.back
    
    def finished(self, *args):
        self.next_scr = True
        self.p1_input.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = "continue"

    def next(self):
        if self.next_scr == False:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p1
            p1 = check_int(self.p1_input.text)
            if p1 == False or p1 <= 0:
                p1 = 0
                self.p1_input.text = "0"
                Popup(title='Error', content=Label(text='The pulse must be a number greater than 0'), size_hint=(None, None), size=(400, 400)).open()
            else:
                self.manager.current = "3"
    def back(self):
        self.manager.current = self.manager.previous()



class Checksits(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        instr1 = Label(text = txt_test2)
        self.btn = Button(text = "Next", size_hint = (0.3, 0.2), pos_hint = {"center_x":0.5})
        self.next_scr = False
        self.lbl_sits = Sits(30)
        self.runner = Runner(30, 1.5)

        self.runner.bind(finished = self.finished)

        hLayout = BoxLayout()
        hLayout.add_widget(instr1)
        hLayout.add_widget(self.lbl_sits)
        hLayout.add_widget(self.runner)

        vLayout = BoxLayout(orientation = "vertical")
        vLayout.add_widget(hLayout)
        vLayout.add_widget(self.btn)

        self.add_widget(vLayout)

        self.btn.on_press = self.next
    
    def finished(self,instance, value):
        self.btn.set_disabled(False)
        self.next_scr = True
        self.btn.text = "Continue"

    def next(self):

        if self.next_scr == False:
            self.btn.set_disabled(False)
            self.runner.start()
            self.runner.bind(value=self.lbl_sits.next)
        else:
            self.manager.current = "4"
 


class PulseScr2(Screen):
    def __init__(self, **kw):
        self.stage = 0
        self.nxt_scr = False


        super().__init__(**kw)

        instr1 = Label(text = txt_test3) 
        line1 = Label(text = "Enter the result", size_hint = (0.2, 1))
        line2 = Label(text = "Enter the result", size_hint = (0.2, 1))
        self.p2_input = TextInput(multiline = False)
        self.p2_input.set_disabled(True)
        self.p3_input = TextInput(multiline = False)
        self.p3_input.set_disabled(True)
        self.btn = Button(text = "Next", size_hint = (0.3, 0.2), pos_hint = {"center_x":0.5})

        self.lbl = Label(text = "count your pulse")


        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done = self.finished)


        hlayout1 = BoxLayout(size_hint = (1, 0.2))
        hlayout1.add_widget(line1)
        hlayout1.add_widget(self.p2_input)

        hlayout2 = BoxLayout(size_hint = (1, 0.2))
        hlayout2.add_widget(line2)
        hlayout2.add_widget(self.p3_input)


        vLayout = BoxLayout(orientation = "vertical")
        vLayout.add_widget(instr1)
        vLayout.add_widget(self.lbl)
        vLayout.add_widget(self.lbl_sec)
        vLayout.add_widget(hlayout1)
        vLayout.add_widget(hlayout2)
        vLayout.add_widget(self.btn)



        self.add_widget(vLayout)
        self.btn.on_press = self.next

    def finished(self, *args):
        if self.lbl_sec.done:
            if self.stage == 0:
                self.stage = 1
                self.lbl.text = "Take a rest"
                self.lbl_sec.restart(30)
                self.p2_input.set_disabled(False)

            elif self.stage == 1:
                self.stage = 2
                self.lbl.text = "Count ur pulse"
                self.lbl_sec.restart(15)
            else:
                self.lbl.text = "complete"
                self.btn.set_disabled(False)
                self.nxt_scr = True
                self.p3_input.set_disabled(False)
        
            


    def next(self):
        if self.nxt_scr == False:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p2
            global p3
            p3 =check_int(self.p3_input.text)
            p2 = check_int(self.p2_input.text)
            if p2 == False or p2 <= 0 or p3 == False or p3 <= 0:
                p2 = 0
                self.p2_input.text = "0"
                p3 = 0 
                self.p3_input.text = "0"
                Popup(title='Error', content=Label(text='The pulse must be greater than 0'), size_hint=(None, None), size=(400, 400)).open()
            else:
                self.manager.current = "5"


class Result(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.instr = Label(text = "")
        self.add_widget(self.instr)
        self.on_enter = self.before


    def before(self):
        global name
        self.instr.text = name + "\n" + ruffier.test(p1,p2,p3,age)






class HeartCheck(App):
    def build(self):

        sm = ScreenManager()
        sm.add_widget(InsScr(name = "1"))
        sm.add_widget(PulseScr(name = "2"))
        sm.add_widget(Checksits(name = "3"))
        sm.add_widget(PulseScr2(name = "4"))
        sm.add_widget(Result(name = "5"))

        return sm
    
app = HeartCheck()
app.run()

