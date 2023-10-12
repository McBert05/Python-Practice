# there are times where we need to compare two objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __gt__(self, other):
        return (self.x > other.x) and (self.y > other.y)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# here we have the point object, if we define another point object with the exact same values
point = Point(10, 20)
point2 = Point(1, 2)

# at first without the use of the magic method if we compare these objects and print it to the console we get false
print(point == point2)
# the reason we get false is because the equality operator compares the references of these two objects in memory
# the two variables are referencing two different objects in memory, and that is why they are not equal
# to solve this problem we need a magic method
# we use the '__eq__' magic method to define the behavior of the equality '==' operator, this function requires two parameters being the two objects
# we use the '__gt__' magic method to define the behavior of the greater than '>' operator, this function requires two parameters being the two objects
# if we use the greater than magic method python will automatically figure what to do if we use the less than operator so there is no need for the redundency of methods
