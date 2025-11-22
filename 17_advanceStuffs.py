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




# List, Dictionary and set comphrehension


# Lambda functions



# Map filter and zip





# Modules and packages 