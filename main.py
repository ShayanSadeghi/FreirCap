from distutils.fancy_getopt import fancy_getopt
from kivy.app import App
from kivy.uix.widget import Widget

class faceBlur(Widget):
    pass

class faceBlurApp(App):
    def build(self):
        return faceBlur()

if __name__=="__main__":
    faceBlurApp.run()

