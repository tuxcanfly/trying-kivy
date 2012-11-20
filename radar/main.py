import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.factory import Factory
from kivy.clock import Clock
from random import randint, random


class Radar(Widget):

    def start(self):
        print "start"

    def update(self, *args):
        pass

    def on_touch_move(self, touch):
        print "touch", touch


class RadarPoint(CheckBox):
    pass


class RadarContainer(GridLayout):
    pass


Factory.register("Radar", Radar)


class RadarApp(App):
    def build(self):
        radar = Radar()
        radar.start()
        Clock.schedule_interval(radar.update, 1.0/60.0)

        container = RadarContainer(spacing=5)
        radar.add_widget(Label(text='Radar', font_size=32, size_hint_y=None))
        radar.add_widget(container)
        for i in xrange(5):
            pt = RadarPoint(group='radar')
            container.add_widget(pt)
        return radar


if __name__ == '__main__':
    RadarApp().run()
