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

