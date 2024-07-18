from abc import ABC, abstractmethod


class AbstractShape(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def to_dict(self):
        # __dict__ yra magic metodas kuris grazina klases lygio atributus ir ju reiksmes.
        # self reiskia kad kai inicijuojamas objektas pvz:
        # sqr1 = Square(name='kvadratas', side_length=10), jo atributai
        # name ir side_length bus panaudojami i magiska metoda.

        return self.__dict__
        # print(self.__dict__)





"""Base Class: Shape
Attributes:
name (string): Name of the shape.
Methods:
__init__(self, name): Constructor to initialize the shape's name.
area(self): Method to calculate the area of the shape. Should be overridden by child classes.
perimeter(self): Method to calculate the perimeter of the shape. Should be overridden by child classes.
to_dict(self): Method to return the shape's parameters as a dictionary."""
