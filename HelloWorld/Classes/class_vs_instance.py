class Point:
    # class level attribute
    default_color = "blue"

    # instance level attribute
    def __init__(self, x, y):
        # we have declared two attributes for our point object in the constructor of the point class
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# whenever we create a new point object this point object will have these attributes by default
point = Point(1, 2)
# accessing instance attribute
print(point.x)

# accessing class attribute
print(point.default_color)
print(Point.default_color)

point.draw()

# we can also define an attribute after we create a point object because objects in python are dynamic
# so we dont have to define all the attributes in a constructor, we can define them later whenever we need them
point.z = 10

# all the attributes we have defined so far (x, y, and z) are instance attributes
# these attributes only belong to point instances (point objects)
# instance attributes are unique to each unique instance you create
# there also exists class attributes, which are attributes we define at the class level
# this will remain the same across all instances of a class, aka shared among all instances of a class (all humans have two eyes and two ears)
