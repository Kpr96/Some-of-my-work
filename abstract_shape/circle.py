from abstract_shape import AbstractShape


class Circle(AbstractShape):

    def __init__(self, name, radius: float):
        self.name = name
        super().__init__(name)
        self.radius = radius

    def perimeter(self):
        return 2 * self.radius * 3.14

    def area(self):
        return 3.14 * self.radius ** 2
