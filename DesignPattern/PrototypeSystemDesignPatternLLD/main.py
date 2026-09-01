
from abc import ABC, abstractmethod
import copy

class Shape(ABC):

    name: str
    color: str

    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def describe(self):
        pass

    def set_color(self, color: str):
        self.color = color

    def get_color(self):
        return self.color


class Circle(Shape):
    def __init__(self, name: str):
        super().__init__(name)
    def clone(self):
        return copy.deepcopy(self)
    def describe(self):
        print(f"CirecleID: {id(self)}, CircleName: {self.get_name()}, Color: {self.get_color()}")


class ShapeRegistry:
    def __init__(self):
        self.prototypes = {}
    def register_prototypes(self, shape_registery_name: str, shape_egistery_prototypes_class_obj: Shape):
        self.prototypes[shape_registery_name] = shape_egistery_prototypes_class_obj
    def create(self, shape_registery_name: str):
        if shape_registery_name in self.prototypes:
            return self.prototypes[shape_registery_name].clone()
        

def main():

    shape_registry_class_obj = ShapeRegistry()

    red_circle_class_obj_1 = Circle("Red-Circle")
    red_circle_class_obj_1.set_color("Red")
    red_circle_class_obj_1.describe()

    shape_registry_class_obj.register_prototypes("Red-Circle", red_circle_class_obj_1)

    red_circle_class_obj_2 = shape_registry_class_obj.create("Red-Circle")
    red_circle_class_obj_2.describe()




main()
    