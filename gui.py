import kivy
import hurricane

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.core.window import Window

Window.size = (1120, 630)

filename="katrina.csv"


class kvBL(BoxLayout):
    def checkbox_click(self, instance, value):
        pass
    def pokreni(self):
        hurricane.obradi_uragan(filename) 
    def setfilename(self,text):
        global filename
        filename=text
class hurricaneApp(App):
    def build(self):
        self.title="Hurricane Tracker"
        return kvBL()


root = hurricaneApp()

if __name__ == '__main__':
    hurricaneApp().run()
    
