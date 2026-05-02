from kivy.app import App
from kivy.uix.button import Button

class MyTelegram(App):
    def build(self):
        return Button(text='Мой Telegram')

if __name__ == '__main__':
    MyTelegram().run()
