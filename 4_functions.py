# will do later
# reusable block of code; and whenever we call it then it gets executed

def hello():
    print("hello user")

hello()

# parameters and arguments
'''
def sum(a,b):   # parameters
    print(a+b)

sum(2,3)        #arguments
'''
'''
## 3 types of arguments - positional argument, default argument, keyword argument
1. Positional Argument - first parameter, will always capture first argument and so on.
2. Default Argument - if you don't pass any value still the function will run by adding a defalut value to the parameter
3. Keyword Argument - you can pass values in any order
'''
# example of Postional Argument
def sum2(a, b):
    print(a)
    print(b)
    print(a+b)
sum2(1,2)

# example of Default Argument
def sum2(a = 5, b = 8):
    print(a)
    print(b)
    print(a+b)
sum2()

'''
Important thing to NOTE in default argument
def sum2(a = 25, b): # error : explanation after this code
    print(a)
    print(b)
    print(a+b)
sum2(15)

# in this code we have an error because Python kisi non-default argument ko default argument ke baad allow nahi karta.
# Correct rule - Pehle non-default arguments Uske baad default arguments

# correct syntax
def sum2(b, a=25):
    print(a)
    print(b)
    print(a+b)

sum2(15)
'''

# example of Keyword Argument
def greet(name, age):
    print(f"your name is {name} and you are {age} years old")

# greet(24, 'saswat')  # your name is 24 and you are saswat years old
greet(age=24, name='saswat')  #your name is saswat and you are 24 years old

# return in function

def multiply(a,b):
    return a*b
multiply(3,4)   # the return statement will come in the place of this code
print(multiply(3,4))