#  Decorator - A decorator is just a function that modifies another function without changing its actual code. 
# Imagine you have a cake (your function). A decorator is like putting icing on the cake. It doesn’t change the cake itself, but makes it better, prettier, or adds some new flavor 
# For creating a decorator you first have to create a decorator functions and then inside that we will create a wrapper. 

'''
def decoratorFunction1(func1):      # func1 will accept hello function as a parameter
    def wrapper():
        print("i will print automatically before the hello function")
        func1()
        print("it will print after the hello function")
    return wrapper


@decoratorFunction1     # jiis bhi function ke upar ye likha hoga to wo function paas ho jaayega as a argument
def hii():
    print("hello, saswat")

hii()


# another example

def decorateThisFunction(sayFunctionAcceptKro):
    def giftWrapper():
        print("i love you")
        sayFunctionAcceptKro()
        print("will you marry me")
    return giftWrapper

@decorateThisFunction
def say():
    print("meri jaan meri jaan meri jaan")
say()

# example with professional naming

def decorate(func):
    def wrapper():
        print("before hello function")
        func()
        print("after hello function")
    return wrapper

@decorate
def hello():
    print("hello world")

hello()

# if you want to pass arguments (e.g sum of two variables)

def decorate(func):
    def wrapper(a,b):
        print("before hello function")
        func(a,b)
        print("after hello function")
    return wrapper

@decorate
def hello(a,b):
    print(f"sum is: {a + b}")

hello(12,3)
# but here is the catch; we dont know ki user kitne parameters bhejega to kya mai baar baar wrapper function aur func ko change krta rhunga;
# isi problem ko solve krne aaya h "args and kwargs" which is our next topic
'''

# Args and Kwargs 

# They’re special keywords in Python used in function definitions to accept a flexible number of arguments
# Now you always don’t have to use Args and Kwargs the main thing is * , ** you can use any names in front of them.
# so *args are used for multiple positional arguments, and **kwargs are used for multiple keyword arguments.
# And the *args becomes a tuple and **kwargs becomes a dictionary 
# The use case is great:
# 1. You don’t need to know how many inputs you'll get 
# 2. Helps in building flexible functions, decorators, APIs, and more

def addition(a,b):
    sum = 0
    print(a+b)

addition(5,3)
# but lets see if you pass more than two arguments
# addition(5,3,2)
# you got error: TypeError: addition() takes 2 positional arguments but 3 were given

def addition(*args):    # args is just a name you  can write anything here {imp. is single star}
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)
    print(args)    # see we got a tuple made up of positional arguments passed to the function

addition(5,2,5,2,1,21,20,15,10,1,10,3,5)
# see now you can pass n number of arguments without thinking about the parameters

def information(**kwargs):    # kwargs is just a name you  can write anything here {imp. is double star}
    for i in kwargs:    
        print(f" {i} : {kwargs[i]}")
    print(kwargs)    # see we got a dictonary made up of keyword arguments passed to the function

information(name = 'saswat', age = 25, education = 'MCA')

# THE USE OF ARGS AND KWARGS IN DECORATORS

def decorate(func):
    def wrapper(*args, **kwargs):
        print("decorate before")
        func(*args, **kwargs)
        print("decorate after")
    return wrapper

@decorate
def addtion2(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)

addtion2(10,2,2,5,1,50)


# List, Dictionary and set comphrehension


# Lambda functions



# Map filter and zip





# Modules and packages 