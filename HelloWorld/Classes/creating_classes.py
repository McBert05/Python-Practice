# let's create a point class in python
# first we start with the 'class' keyword and then we give it a name
# for classes we name Pascal naming convention
# Pascal: The first letter of every word should be upper cased
# example: MyPoint, Point, ThePoint
# after  our name we add a colon to indicate a block
# within this block we can define all of our functions
# all functions in classes should have at least one parameter
class Point:
    def draw(self):
        print("draw")


# now that we have a class or blueprint for creating point objects, every point object will create will have the draw method
# to create a point object we call the class like a function, which will create a point object that we can assign to a variable
point = Point()
print(type(point))

# we also have a method called 'isinstance' which is used to see if an object is an instance of a given class
# isinstance(object, class)
print(isinstance(point, Point))
