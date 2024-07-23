from abstract_shape import AbstractShape


class Rectangle(AbstractShape):

    def __init__(self, name, length: float, width: float):
        super().__init__(name)
        self.name = name
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length * self.width)
