#staticmethod
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, point):
        return math.sqrt((point.x - self.x)**2 + (point.y - self.y) ** 2)

    @staticmethod
    def calc_distance(point_1, point_2):
        return math.sqrt((point_1.x - point_2.x)** 2 + (point_1.y - point_2.y) ** 2)


p = Point(5, 6)
p2 = Point(3, 4)
p.calculate_distance(p2)
Point.calc_distance(p, p2)

#classmethod
class Laptop:
    def __init__(self, memory, model):
        self.memory = memory
        self.model = model

    @classmethod
    def low_ram_laptop(cls, model):
        return cls(8, model)

    @classmethod
    def high_ram_laptop(cls, model):
        return cls(16, model)

    def __str__(self):
        return f"Laptop model is {self.model} with ram {self.memory}"

small_ram_laptop = Laptop.low_ram_laptop("Asus")
laptop2 = Laptop.low_ram_laptop("Mac")
laptop_custom = Laptop(32, "HP")
print(small_ram_laptop)
print(laptop2)
print(laptop_custom)
