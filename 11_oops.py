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

