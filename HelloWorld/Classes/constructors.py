# to create constructors we create a function and its name should be double underlined named 'init' followed by subsequent double underlines
# this is known as a magic method, this magic method is called a contstructor
# all methods in a class should have at least one parameter which we call self by convention
# self is a reference to the current point object
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point.x)
point.draw()
