from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import time
from kivy.properties import StringProperty
import cv2
import numpy as np
class MainWindow(Screen):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        img_path = "IMG_{}.png".format(timestr)
        camera.export_to_png(img_path)
        print("Captured")
        img = cv2.imread(img_path)
        cv2.imwrite(img_path, cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
        print(np.sqrt(3))


class SecondWindow(Screen):
    id1 = StringProperty()



    print("load")
    def captureS(self):
        print("econd")


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()