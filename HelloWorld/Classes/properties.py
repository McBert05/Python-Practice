# there are times where you would want to have control over an attribute in a class
# here we have this product class, and in the constructor we set the price attribute
from ast import Raise

# 'Product' class example without use of properties:


class Product:
    def __init__(self, price):
        # now that we have the set price method we don't need this line of code where we just automatically set the price
        # self.__price = price
        # instead we can set the price by calling the set price method and passing in the price
        self.set_price(price)

    # with the way we have implemented our class function we can create a product object
    # and give it a negative price, and python interpreter will execute this without any problem and this is not good
    # to ensure our products dont have a negative price, we can make the field private
    # and then define two methods for getting and setting the value of this
    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


# product = Product(-50)

# the solution above works but its not pythonic (its not using pythons language features the the best ability)
# rather we can use properties to get or set an attribute
# a property is an object that sits on front of an attribute and allows us to get or set the value of that attribute

# 'Product' class example with use of properties:
class Product2:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    # after we define our get and set methods we define a class attribute with the ideal name
    # in this case we will name it 'price', then we assign it to the built in 'property' fucntion
    # the 'property' function takes in four parameters, and all of the parameters are optional
    # the first parameter is a function for getting the value of an attribute
    # the second parameter is a function for setting the value of an attribute
    # the thrid parameter is a function for deleting an attribute
    # the last parameter is for documentation
    # for this implementation we only need to supply two arguments which are get_price and set_price
    price = property(get_price, set_price)


product = Product2(10)
# price is a property in which we can set like below:
# if set to negative value because of the way we specified our function it will throw/raise and error
product.price = -1
# price is also a property in which we can get like below:
print(product.price)
# the price property solved our problem but the two methods we wrote are still accessible
# if we type 'product.' we wil get access to our get_price and set_price method
# this is like having a remote with 50 buttons, these methods are polluting the interface of our object


# 'Product' class example with use of properties enhanced:
class Product3:
    def __init__(self, price):
        # since we no longer have 'set_price' as a attribute
        # we can use our 'price' property like a regular attribute
        self.price(price)

    # we can use a property decorator for this method
    # the we give the method name, in this case we call it price this will be the name of our property
    @property
    def price(self):
        return self.__price

    # similarly we need to apply a decorator to this method
    # the name of the decorator starts with the name of our property
    # the decorator will be the name of our property
    # the we fill follow it with a dot and its identifier in this case 'setter'
    # and rename the setter function to 'price' as well
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product2(10)
# price is a property in which we can set like below:
product.price = -1
# price is a property in which we can get like below:
print(product.price)
