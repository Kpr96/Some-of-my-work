from shapes import Square
from shapes import Circle
from shapes import Rectangle


sqr1 = Square(name='kvadratas', side_length=10)
circle1 = Circle(name='apskritimas', radius=5.5)
rectangle1 = Rectangle(name='staciakampis', length=5.5, width=4.4)

print(rectangle1.area())
print(rectangle1.perimeter())

print(circle1.perimeter())
print(circle1.area())

# C:\Users\kipra\PycharmProjects