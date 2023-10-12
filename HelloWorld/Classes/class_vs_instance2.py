# just like we have instance and class attributes, we also have instance and class methods
class Point:

    # this is an instance metod and can be called using an instance/object of the point class
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # this is an instance method and can be called using an instance/object of the point class
    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    # there are times when you wanna create a 'point' (refering to the point class in this case) and
    # you dont need an existing object and that is when we use a class method
    # we can define a class method, in this casee we will call it 'zero'
    # we will pass in 'cls' as the first parameter which stands for the class itself
    # to make this method a class method we need a decoration
    # we use the '@classmethod' for class method decoration and we put it right above our method signature
    @classmethod
    def zero(cls):
        # in this class method we have a reference to our class being 'cls'
        # and with that we can create a point object with initial values
        # we are creating a point object and then returning it
        return cls(0, 0)


point = Point(1, 2)
print(point.x)
point.draw()
point = Point.zero()
point.draw()
