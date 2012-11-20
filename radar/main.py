import kivy
kivy.require('1.0.8')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty, ObjectProperty


class RadarButton(CheckBox):

    filename = StringProperty(None)
    sound = ObjectProperty(None)

    def on_filename(self, instance, value):
        # the first time that the filename is set, we are loading the sample
        if self.sound is None:
            self.sound = SoundLoader.load(value)

    def on_active(self, *args, **kwargs):
        # stop the sound if it's currently playing
        if self.sound.status != 'stop':
            self.sound.stop()
        self.sound.play()


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
            root.add_widget(btn)

        return root

if __name__ == '__main__':
    RadarApp().run()
