#  Encapsulation - Encapsulation means putting data (variables) and code (functions) together in one place — inside a class. It also means hiding the internal details of how things work, and only showing what is needed 
# It keeps data safe from being changed by mistake 
# It makes your code clean and easy to use 
# It gives control over what others can access or change.

# Access Modifier
# 1. public
# 2. protected -> By single underscore _
# 3. private -> 

# 1. public - every thing (attributes and members) can accessed by the objects or the inherited class

# 2. protected - declared by single underscore (_) but attribute and member functions still can be accessed from outside the class
#  Python doesn’t enforce protected access like other languages (e.g., Java or C++). But it uses a naming convention to tell developers

# 3. private Attributes and Methods -  It cannot be accessed from outside the class; only from inside the class where it is defined
# In Python, we use two underscores (__) before the name to make it private

'''
class City:
    cityName = "hazaribagh"

    def show(self):
        print("this is show")
        
obj = City()
obj.cityName = "ranchi"
print(obj.cityName) # see we can access and change it also
'''

# now lets make it private so that we cannot access and cannot change it

class City:
    
    __cityName = "hazaribagh"

    def show():
        print("this is show")

obj = City()
obj.__cityName = "ranchi"
print(obj.__cityName)
obj = City()
obj.__cityName = "ranchi"

print(obj.__dict__)

# ⭐ 3. Python Private Variable ka Sach (Important)

# Python me private variable 100% private nahi hota.
# Python sirf name mangling karta hai.

# ✔ Naam mangling ka rule:
# __variable  →  _ClassName__variable


# Example me:

# __cityName → _City__cityName


# Python variable ka naam background me change kar deta hai.

# ⭐ 4. Kyun obj.__cityName = "ranchi" kaam karta hua lagta hai?

# Aap sochte ho ye private variable update hoga,
# par actually ye ek naya variable ban jata hai.

# Proof:
# obj.__cityName = "ranchi"
# print(obj.__dict__)


# Output:

# {'__cityName': 'ranchi'}


# ⚠ Original private variable same rehta hai:

# _City__cityName = "hazaribagh"


# aapka likha hua variable new ban jata hai, original untouched rehta hai.

# ⭐ 5. Real private variable access kaise hota hai?

# Background me Python variable ka naam change kar deta hai.

# Access karne ka original hidden method:

# print(obj._City__cityName)

# ⭐ 6. Private variable ko sahi tarike se update kaise karein? (Encapsulation ka asli tarika)
# Getter (read):
# def getCity(self):
#     return self.__cityName

# Setter (update):
# def setCity(self, name):
#     self.__cityName = name

# Use:
# obj = City()
# obj.setCity("ranchi")
# print(obj.getCity())

# ⭐ 7. Summary — Ek Line me

# __variable → private lagta hai

# Python actually variable ka naam mangling karke _Class__variable bana deta hai

# obj.__variable likhne se naya variable ban jata hai, original private change nahi hota

# Private variable ko modify karne ka sahi tarika = setter method