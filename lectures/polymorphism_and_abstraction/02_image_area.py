class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __eq__(self, other): #equal to
        return self.get_area() == other.get_area()

    def __ge__(self, other): #greater or equal
        return self.get_area() >= other.get_area()

    def __gt__(self, other): #greater than
        return self.get_area() > other.get_area()

    def __le__(self, other): #less or equal
        return self.get_area() <= other.get_area()

    def __lt__(self, other): #less than
        return self.get_area() < other.get_area()
