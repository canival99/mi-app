from kivy.app import App
from kivy.uix.button import Button

class MiApp(App):
    def build(self):
        return Button(text="hola thanos mi primera app")

if __name__== "__main__":
     MiApp().run()
