import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class RareKivy(App):

    def build(self):
        main_layout = BoxLayout(orientation='vertical')
        search_input = TextInput(text='Type Something')
        btn1 = Button(text='Search',size_hint=(.1, .1))
        main_layout.add_widget(search_input)
        main_layout.add_widget(btn1)
        return main_layout


if __name__ == '__main__':
    RareKivy().run()