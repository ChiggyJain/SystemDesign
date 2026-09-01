
from abc import (
    ABC,
    abstractmethod
)

class Button(ABC):
    @abstractmethod
    def create_button(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def create_checkbox(self):
        pass


class DarkThemeButton(Button):
    def create_button(self):
        print(f"Dark theme submit button is created successfully")

class LightThemeButton(Button):
    def create_button(self):
        print(f"Light theme submit button is created successfully")


class DarkThemeCheckbox(Checkbox):
    def create_checkbox(self):
        print(f"Dark theme checkbox is created successfully")

class LightThemeCheckbox(Checkbox):
    def create_checkbox(self):
        print(f"Light theme checkbox is created successfully")


class WidgetFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

class DarkThemeWidgetFactory(WidgetFactory):
    def create_button(self) -> Button:
        return DarkThemeButton()
    def create_checkbox(self) -> Checkbox:
        return DarkThemeCheckbox()
    
class LightThemeWidgetFactory(WidgetFactory):
    def create_button(self) -> Button:
        return LightThemeButton()
    def create_checkbox(self) -> Checkbox:
        return LightThemeCheckbox()


def main():

    dark_theme_widget_factory_class_obj = DarkThemeWidgetFactory()
    create_button_class_obj = dark_theme_widget_factory_class_obj.create_button()
    create_button_class_obj.create_button()
    create_checkbox_class_obj = dark_theme_widget_factory_class_obj.create_checkbox()
    create_checkbox_class_obj.create_checkbox()

    light_theme_widget_factory_class_obj = LightThemeWidgetFactory()
    create_button_class_obj = light_theme_widget_factory_class_obj.create_button()
    create_button_class_obj.create_button()
    create_checkbox_class_obj = light_theme_widget_factory_class_obj.create_checkbox()
    create_checkbox_class_obj.create_checkbox()
    

main()
    












