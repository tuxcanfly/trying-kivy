from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App

class ListApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        for x in xrange(5):
            root.add_widget(Label(text='Hello World'))
        return root

if __name__ == '__main__':
    ListApp().run()
