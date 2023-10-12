# when buildingg various classes we may notice that these classes have one or more features or functions in common

from re import A, M


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eat")

# inheritance allows us to define the commons behaviors or functions in one class, and then inherit them in other classes
# to specify inheritance from one class to another we can specify the class in parenthases
# Animal: Parent, Base
# Mammal: Child, Sub


class Mammal(Animal):
    def walk(self):
        print("Walk")

# all fish could be able to eat but not walk


class Fish(Animal):
    def swim(self):
        print("Swim")


# we can also inherit the atttributes of a base class
m = Mammal()
m.eat()
print(m.age)
