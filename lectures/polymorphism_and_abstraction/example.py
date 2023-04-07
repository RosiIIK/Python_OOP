from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        return "Shape"


class Triangle(Shape):
    def __init__(self, h, side):
        self.h = h
        self.side = side

    def calculate_area(self):
        print("Calculating triangle area")

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        print("Calculating circle area")

class Square(Shape):
    def calculate_area(self):
        print("Calculating square area..,")

print(Square())

shapes = [Triangle(5, 2), Circle(5), Triangle(8,9), Triangle(2,4), Square()]

for shape in shapes:
    shape.calculate_area()
