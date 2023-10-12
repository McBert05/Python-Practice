# magic methods have two underscores at the beginning and end of their name
# https://rszalski.github.io/magicmethods/ to find a list of magic methods
# and they are called automatically by python interpreter depending on how we use our object and classes
class Point:
    # here we have this 'init' magic method we dont automatically call it, its called automattically by python interpreter
    # when we create a new point object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    # we can tweek magic methods like so:
    # we first define it calling the specific magic method and edit the body to make it do what we intend
    def __str__(self):
        return f"({self.x}, {self.y})"


point = Point(1, 2)
# above we have a point object stored in a variable named 'point'
# if we try to print 'point' using the print statement on the console we will get:
# the name of our module
# followed by the class name
# and finally the address of this point object in memory
# this is the default implementation of the '__stir__' magic method
print(point)
