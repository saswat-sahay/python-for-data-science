# Dunder methods - Dunder methods are special methods in Python that start and end with double underscores, like __init__, __str__, __add__, etc 
# They automatically get called when you perform certain actions on an object 
# They help you Customize behavior of your class
# Make your class objects behave like built-in data types (like strings, lists, etc.)
# defines working and structure of objects

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"hello, how are you {self.name}"
    
    # for two objects
    def __add__(self, other):
        return f"sum of age is: {self.age + other.age}"

    # for three objects
    # def __add__(self, other):
    #     sum = 0
    #     for i in other:
    #         sum = sum + i.age
    #     return f"sum of age is: {self.age + sum}"

obj1 = Animal("lion",10)
obj2 = Animal("cow",15)
obj3 = Animal("Human", 50)
print(obj1)
print(obj2)
print(obj1 + obj2)
# print(obj1 + (obj2, obj3))
# but you cannot add three ages of animals by the same method
# here is the trick to add three objects
