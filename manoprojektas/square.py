from .abstract_shape import AbstractShape


class Square(AbstractShape):

    def __init__(self, side_length: int, name):
        super().__init__(name)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return self.side_length * 4

    """
    Square:
Attributes:
side (float): Side length of the square.
Methods:
__init__(self, side): Constructor to initialize the side and set the name to "Square".
area(self): Override to calculate the area of the square.
perimeter(self): Override to calculate the perimeter of the square.
to_dict(self): Override to include the side in the dictionary.

    """
