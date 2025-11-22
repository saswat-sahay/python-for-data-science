# Abstraction doesnot exist in python but we can achieve it using a library
# It is used to simplifying complex systems by focusing on essential features and hiding unnecessary details
# used to define a common interface for different subclasses

# Abstract classes and methods - 
# Abstract classes are classes that contains one or more abstract methods 
# A method that is defined but not implemented in the abstract class. subclasses must provide the implementation.
'''
from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square:
    def __init__(self, side):
        self.side = side
    
class Circle(abstract):
    def __init__(self, radius):
        self.radius = radius
    
obj = Circle(5)
'''

# you haven't created area & perimeter which was an essential in this perticular example
# now lets see what will happen if you inherit abscract class
# TypeError: Can't instantiate abstract class Circle without an implementation for abstract methods 'area', 'perimeter' 
# we got this error
# so abstraction also helps to restrict you to code as it is required; you cannot replace or miss anything
# now lets correct the code

from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(abstract):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("this is area")
    
    def perimeter(self):
        print("this is perimeter")
    
class Circle(abstract):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("this is area")
    
    def perimeter(self):
        print("this is perimeter")
    
obj = Square(5)
obj = Circle(7)