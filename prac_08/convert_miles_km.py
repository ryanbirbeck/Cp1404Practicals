from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Ryan Birbeck'


class ConvertMilesKmApp(App):
    def build(self):
        Window.size = (400, 200)
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, value):
        try:
            result = float(value) * 1.60934
            calculation = f'{result:,.2f}'
            self.root.ids.output_label.text = f"{calculation} kilometres"
        except ValueError:
            pass

    def handle_up(self, value):
        try:
            self.root.ids.input_label.text = str(float(value) + 1)
        except ValueError:
            pass

    def handle_down(self, value):
        try:
            self.root.ids.input_label.text = str(float(value) - 1)
        except ValueError:
            pass


ConvertMilesKmApp().run()
