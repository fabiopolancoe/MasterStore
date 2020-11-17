# MasterStore app

#Import
from art import text2art

from kivy.app import App

from kivy.uix.label import Label

#Terminal Part
print(text2art("MasterStore"))
print("The gui window just pupup!")

#Gui part
class MasterStore(App):

    def build(self):

        return Label(text="Hello Kivy!")

MasterStore().run()