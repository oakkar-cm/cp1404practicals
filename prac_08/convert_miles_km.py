
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty


CONVERSION_FACTOR = 1.60934

class ConvertmilestokmApp(App):
    output_label = StringProperty("0.0 km")

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size =(200,100)
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self,number):
        try:
            value = float(self.root.ids.input_number.text)
        except ValueError:
            value = 0
        value += number
        self.root.ids.input_number.text = str(int(value))

    def handle_convert(self):
        try:
            value = float(self.root.ids.input_number.text)
        except ValueError:
            return 0
        km = value * CONVERSION_FACTOR
        self.output_label = f"{km:.2f} km"


ConvertmilestokmApp().run()