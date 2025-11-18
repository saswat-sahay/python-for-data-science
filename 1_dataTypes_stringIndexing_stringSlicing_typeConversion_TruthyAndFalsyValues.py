# this is comment
"""
    this is not a comment this is a doc string
"""

firstName = "saswat" #camelCase
LastName = "sahay" #PascalCase
full_name = "saswat sahay" #snake_case

### data types - 1. number typed, 2. string typed, 3. boolean typed

## 1.number typed data types
a = 12 #int
b = 1.5 #float
c = 3/4 #float
d = 12/3 #float
complexx = 32j #complex #we have to use j | we cannot use anyother letter to make a number complex

'''
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(complexx))
'''

## 2.strings typed data types
str1 = 'ab12233$@/'
str2 = "SBCSHO230*(^&)"

'''
print(type(str1))
print(type(str2))
'''

## 3.boolean typed data types
boolean1 = True
boolean2 = False

### unicode point -  a universal character encoding standard; that assigns a unique number (code point) to every character (regardless of language) supports all language + emojis etc

a = "A"
# print(ord(a))   #unicode point of A

a = 65
# print(chr(a))   #Character stored in the code 65


### String Indexing - 2 types of indexing - positive indexing [from start], negative indexing [from end]

st = 'hello py'
# positive indexing = h -> 0    e -> 1      l -> 2      l -> 3      o -> 4  "space" -> 5    p -> 6    y -> 7
# negative indexing = h -> -8    e -> -7      l -> -6      l -> -5      o -> -4  "space" -> -3    p -> -2    y -> -1
# print(st)

# positive indexing

'''
print(st[0])
print(st[1])
print(st[2])
print(st[3])
print(st[4])
print(st[5])
print(st[6])
print(st[7])
'''

# negative indexing
'''
print(st[-1])
print(st[-2])
print(st[-3])
print(st[-4])
print(st[-5])
print(st[-6])
print(st[-7])
print(st[-8])
'''


### string slicing

# syntax: [start : stop : steps]

sli = "hi, i am saswat sahay"

'''
print(sli)
print(sli[6:8:1]) # am
print(sli[9:21:1]) # saswat sahay
print(sli[9::1]) # saswat sahay -- empty chorne pr by default end tk leta hai
print(sli[9:100:1]) # saswat sahay -- jitne characters hai usse jyada lene pr error nhi aayega last string characters tk jaayega
print(sli[0:8:1]) # hi, i am
print(sli[::1]) # hi, i am saswat sahay
print(sli[::2]) # h,ia awtshy
print(sli[::3]) # h,ia awtshy
'''

### Type Conversion - Implicit (python automatically does it) & Explicit (we have to do it with functions)

# Implicit type conversion - python automatically performs type convresion
a = 12 # int
print(a/2) #python automatically perform type casts int into float
# output - 6.0 

# Explicit type conversion - we have to do it with in-built functions
# 4 main functions - int(), float(), str(), complex(), bool(), list(), tuple() set(), dict()

a = 12
print(type(a))
a = str(a)
print(type(a))

# same you can check for float(), int(), bool()
# bool() -> converts into True/Flase

a = 12
print(type(a))
a = bool(a)
print(type(a))
print(a)

### Truthy & Falsy Values

# Falsy -> Flase, 0, 0.0, "" -> empty string, [] -> empty list, () -> empty tuple, {} -> empty dictionary
# Except anything will convert into True