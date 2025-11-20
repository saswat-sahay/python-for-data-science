# Inheritance works between classes.
# It allows a class (child class) to inherit properties and behaviors (attributes and methods) from another class (parent class)

# Benefits of using inheritance is - Code reusability; Organized structure; Easy to maintain and extend

class Factory1:
                           # super/ parent class
    a = "i am an attribute inside Factory 1"

    def hello(self):
        print("i am an method inside Factory 1")

class Factory2(Factory1):  # inherited factory1
                           # Sub/ child class
    pass

obj1 = Factory1()
print(obj1.a)
obj1.hello()

obj2 = Factory2()
print(obj2.a)
obj2.hello()


# Constructor in Inheritance - the constructor function of parent class will work for the child class as well.

# Lets say you have created a parent class with a constructor function inside it and then this class is inherited by another class then the constructor function of parent class will work for the child class as well. 

class Animal:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print(f"hello {self.name}")
    
class Human(Animal):
    pass

person1 = Human("saswat")
person1.show()

# if you want to get two arguments inside only your child class and you want to get only one common argument in both, then check below code and use super() function 

class Animal:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print(f"hello {self.name}")
    
class Human(Animal):
    def __init__(self, name, age):
        self.age = age
        super().__init__(name)  # super targets the parent class
    
    def show(self):
        print(f"hii {self.name} and age {self.age}")

animal1 = Animal("lion")  # (name: Any) -> Animal
person1 = Human("saswat", 25)  # (name: Any, age: Any) -> Human
animal1.show()
person1.show()

# types of inheritance - 1. Single, 2. Multiple, 3. multilevel, 4. heirarical 
# Single Inheritance - one parent one child
# Multiple Inheritance - two parent one child
# multilevel Inheritance - grandparent class → parent class → child class
# heirarical Inheritance - one parent class multiple child class

# note (In multiple inheritance): The constructor function will be inherited of the first class that has been Inherited. This is MRO(Method Resolution Order) followed by python.

class Animal:
    # name1 = "lion"

    def __init__(self, name):
        pass

class Human:
    # name2 = "saswat"

    def __init__(self, name, age):
        pass

class Robots(Animal, Human):
    name3 = "chitti 2.0"
        
obj = Robots()  # (name: Any) -> Robots {because of the order of inheritance; check the note before the code}
print(obj.name1)

# multilevel inheritance - grandparent class → parent class → child class

class SmallFactory:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips

class MediumFactory(SmallFactory):
    def __init__(self, material, zips, pocket):
        super().__init__(material, zips)
        self.pocket = pocket

class BigFactory(MediumFactory):
    def __init__(self, material, zips, pocket, color):
        super().__init__(material, zips, pocket)
        self.color = color