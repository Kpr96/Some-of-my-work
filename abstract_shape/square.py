from .abstract_shape import AbstractShape


class Square(AbstractShape):

    def __init__(self, side_length: int, name):
        super().__init__(name)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return self.side_length * 4
