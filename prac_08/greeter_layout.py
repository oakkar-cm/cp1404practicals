from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

Window.size = (500, 150)  # Optional window size

class GreeterApp(App):
    output_text = StringProperty('')

    def build(self):
        self.title = "Greeter Program"
        return Builder.load_file('greeter_layout.kv')

    def greet(self):
        name = self.root.ids.input_name.text.strip()
        self.output_text = f"Hello {name}"

    def clear(self):
        self.root.ids.input_name.text = ''
        self.output_text = ''

GreeterApp().run()