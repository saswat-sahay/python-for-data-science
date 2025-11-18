### Input and Output

name = 'saswat'
age = 25
'''
print('my name is:',name,'and i am:',age,'years old')
print(f"my name is {name} and my age is {age}")
print(f'my name is {name} and my age is {age}')

strYear = input("enter year")
print(strYear)
print(type(strYear))   #type str

intYear = int(input("enter year"))
print(intYear)
print(type(intYear))   #type int
'''
### Operators - Arithmetic, Assignment, Comparison, Logical

## Arithmetic
# +, -, *, / (with decimal; weather completely divide (6/3 = 2.0)), %, // (floor division - without decimal; weather not compelety divide (5/2 = 2)), ** (exponential)

a = 6
b = 2

'''
print(a+b)      # 8
print(a-b)      # 4
print(a*b)      # 12
print(a/b)      # 3.0
print(a%b)      # 0
print(a//b)     # 3
print(a**b)     # 36
'''

## Assignment operators
# =, +=, -=, *=, /=, %=, //=, **=

a = 2 # Assignment
## Compund Assignment Operator
a += 8
a -= 5
a *= 2
a /= 2
a %= 2
a *= 10
a //= 5
# a = int(a)
a **= 5
print(a)

## Comparison operators - gives True/ False
# ==, !=, <, >, <=, >=

a = 12
b = 10
'''
print(a == b)   # False
print(a != b)   # True
print(a < b)    # False
print(a > b)    # True
print(a <= b)   # False
print(a >= b)   # True
'''

a = 12.4
b = 10
c = 'saswat'

print("In python we can also compare in between different datatypes")
print(a == c)

print("we can also compare strings")
print(ord('a'))
print(ord('b'))
print("a" > "b")    # UNICODE OR ASCII code for a = 97 & b = 98
print(ord('A'))
print(ord('B'))
print("A" < "B")    # UNICODE OR ASCII code for A = 65 & B = 66

## Logical  - and, or, not

print("logical and operator")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print("logical or operator")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print("logical not operator")
print(not True)
print(not False)