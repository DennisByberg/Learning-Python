from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(pi * self.radius * self.radius, 2)

    def perimeter(self):
        return round(2 * pi * self.radius, 2)


rectangle = Rectangle(5, 10)
print(rectangle.area())
print(rectangle.perimeter())

circle = Circle(7)
print(circle.area())
print(circle.perimeter())
