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
        return self.__dict__

