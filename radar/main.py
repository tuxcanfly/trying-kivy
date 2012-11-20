import kivy
kivy.require('1.0.8')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock


class RadarButton(CheckBox):

    filename = StringProperty(None)
    sound = ObjectProperty(None)

    def on_filename(self, instance, value):
        # the first time that the filename is set, we are loading the sample
        if self.sound is None:
            self.sound = SoundLoader.load(value)

    def play_sound(self):
        # stop the sound if it's currently playing
        if self.sound.status != 'stop':
            self.sound.stop()
        self.sound.play()

    def update(self, *args):
        if self.active:
            self.play_sound()


class RadarBackground(GridLayout):
    pass


class RadarApp(App):

    def build(self):

        root = RadarBackground(spacing=5)
        for i in xrange(0, 100):
            btn = RadarButton(
                text="", filename="sound.wav", group=str(i),
                size_hint=(None, None), halign='center',
                size=(64, 64))
            Clock.schedule_interval(btn.update, 50.0/60.0 + i/10)
            root.add_widget(btn)
        return root

if __name__ == '__main__':
    RadarApp().run()
