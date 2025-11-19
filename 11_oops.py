# classes and object - blueprint for creating objects
class Factory:
    a = 12 # attributes

    def greet(self):  # methods
        print("hello welcome to class")

    # print("Class inititalized")     # class only initialized once
# print(Factory().a)
# Factory().greet()

# creating object
obj1 = Factory()
# The object has all the powers of a class therefore a class object can access attributes and methods of a class.
print(obj1.a)
obj1.greet()

obj1.a = 2
print(obj1.a)

# constructor - A constructor is a method that runs automatically when we call a class and this constructor function will target the objects location
# we can accept parameters by the help of constructors

class Bag:
    def __init__(self, name, material, zips, pockets):
        # self tracks the location of the reebok, campus, localbrand (object)
        self.brandName = name
        self.material1 = material
        self.numberOfZips = zips
        self.numberofPockets = pockets

    def show(self):
        print(f"details of {self.brandName} are | material is {self.material1} | no of zips are {self.numberOfZips} | no of pockets are {self.numberofPockets}")

reebok = Bag("reebok","leather", 3, 4)
campus = Bag("campus","vegan-leather", 4, 7)
localbrand = Bag("localbrand","nylon", 8, 10)
'''
print(reebok.material1)
print(reebok.numberofPockets)
print(reebok.numberOfZips)
print(campus.material1)
print(campus.numberOfZips)
print(campus.numberofPockets)
print(localbrand.material1)
print(localbrand.numberOfZips)
print(localbrand.numberofPockets)
'''

reebok.show()
campus.show()
localbrand.show()

##  Types of Attribute

#  Class attribute - A normal variable create inside a class is a class attribute.
 
# Instance attribute - A attribute created using an instance like self.name, self.age etc. It is known as instance attribute.

class Animal:
    breed = "lion"  # class attribute

    def __init__(self, age):
        self.age = age  # instance attribute
        
    def ageTeller(self, age): # instance attribute
        self.age = age
    
# Types of Methods
# Instance Method - An instance method Works with instance (object) of the class. This method can access and modify instance attributes.

    def show(self):  # instance method
        print(f"this is a instance method and it point to the object {self.age}")

## Class Method - This method works with the class itself it will not target the instance (object) and it targets to the class. we have to use @classmethod decorator for creating the class method and it takes cls as their first parameter.

    @classmethod  # decorator
    def hello(cls):
        print(f"this is a class method and it points to the class and self.age will not work here")

# Static Method - This method doesn’t access class or instance directly it also uses a decorator @staticmethod it just acts like a regular function placed inside a class.
    @staticmethod
    def static():
        print("this is a static method and it doesnot target either class or object")

obj1 = Animal(20)
obj1.show()
obj1.hello()
obj1.static()


