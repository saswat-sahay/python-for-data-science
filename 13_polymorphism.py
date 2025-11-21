# Polymorphism - same name different form

# Types - 2 ways {Mehtod Overriding and Duck Typing}[in compile time languages there are 3 ways; but python doesnot support method overloading]

#  Method overloading means having same name methods inside a class but parameters will be different but in python the latest definition will overwrite the previous one.

# Method Overriding - A child class overrides a method of the parent class, and Python decides at runtime which method to call, based on the object type.

# method overriding example

class Animal():
    def show(self):
        print("hello Animal")

class Human(Animal):
    def show(self):
        print("hello Human")

obj = Human()
obj.show()
ob = Animal()
ob.show()

# Mehtod overloading - Not Supported in python; [same name methods with differnet parameters inside a class]

# Duck Typing - Python follows the philosophy: "If it (any object) walks like a duck and quacks like a duck, it must be a duck"

class Duck:
    def talk(self):
        print("quack")
class Human:
    def talk(self):
        print("hii")
obj = Duck()
obj.talk()

obj2 = Human()
obj2.talk()