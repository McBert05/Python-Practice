# we also have magic methods for performing arithmetic operations between two objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    # without the '__str__' magic method python will print the memory address location and not the actual points of the object
    # go to line 21
    # def __str__(self):
    #     return f"({self.x}, {self.y})"


point = Point(10, 20)
point2 = Point(1, 2)
# we can combine the objects and then store it into one object and then print each variable seperately like so
combine = point + point2
print(combine.x)
