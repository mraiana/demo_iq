from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

from text import questions, run_test

txt1 = "Тест на ваш IQ. \n Дисклеймер! \n Тест сделан в юмористических целях, чтобы узнать свой настоящий IQ обратитесь к специалисту."
age = 6
name = ""

class MainScr(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       instr = Label(text=txt1, halign='center')
 
       lbl1 = Label(text='Введите имя:', halign='right')
       self.in_name = TextInput(multiline=False)
       lbl2 = Label(text='Введите возраст:', halign='right')
 
       self.in_age = TextInput(text='6', multiline=False)
       self.btn = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
       self.btn.on_press = self.next
 
       line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
       line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
       line1.add_widget(lbl1)
       line1.add_widget(self.in_name)
       line2.add_widget(lbl2)
       line2.add_widget(self.in_age)
 
       outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
       outer.add_widget(instr)
       outer.add_widget(line1)
       outer.add_widget(line2)
       outer.add_widget(self.btn)
 
       self.add_widget(outer)
 
   def next(self):
           global name
           name = self.in_name.text
           self.manager.current = 'test1'

class Tst1Scr(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
      
       instr = Label(text=questions)
      
       line = BoxLayout(size_hint=(0.8, None), height='30sp')
       lbl_result = Label(text='Введите результат:', halign='right')
       
      
       line.add_widget(lbl_result)
       line.add_widget(self.in_result)
 
       self.btn = Button(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
       self.btn.on_press = self.next
 
       outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
       outer.add_widget(instr)
       outer.add_widget(line)
       outer.add_widget(self.btn)
 
       self.add_widget(outer)
 
   def next(self):
            pass
           
class MyApp(App):
    def build(self):
       sm = ScreenManager()
       sm.add_widget(MainScr(name='main'))
       sm.add_widget(Tst1Scr(name='test1'))
       return sm
 
app = MyApp()
app.run()
