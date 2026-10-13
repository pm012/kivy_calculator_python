from kivy.app import App
from kivy.core.window import Window
from src.ui import CalculatorUI


class CalculatorApp(App):
    def build(self):
        self.calculator = CalculatorUI()
        Window.bind(on_key_down=self.calculator.on_key_down)
        Window.bind(on_textinput=self.calculator.on_textinput)
        return self.calculator

    def on_stop(self):
        Window.unbind(on_key_down=self.calculator.on_key_down)
        Window.unbind(on_textinput=self.calculator.on_textinput)


if __name__ == "__main__":
    CalculatorApp().run()