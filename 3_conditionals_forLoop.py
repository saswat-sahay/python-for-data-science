### if statement
'''
a = 12
if a>10:
    print("a is greater than 10")

# if else statement
if (a>10):
    print("a is greater than 10")
else:
    print("a is smaller than 10")

# if elif else statement
if a == 0:
    print("a is 0")
elif a < 0:
    print("a is less than 0")    
else:
    print("a is greater than 0")
'''

### loops
# for
'''
a = range(1,5,1)    #range(start, stop, steps)
for i in a:
    print(i)    # 1,2,3,4

for i  in range(1,6,1):
    print(i)    # 1,2,3,4,5

for i  in range(11):    #default values for start is 0 and steps is 1
    print(i)    # 0,1,2,3,4,5,6,7,8,9   # we must have to give stop

for i  in range(10,1,-1):       # 10,1,-1 -> 10 to 2 
    print(i)                    # 10,0,-1 -> 10 to 1 
                                # 10,-1,-1 -> 10 to 0 

# print table of n entered by user   
n = int(input("enter number:- "))
for i in range(1,11,1):
    print(f"{n} * {i} = {n*i}")
'''
'''
# for with strings

a = "helllo"
# print(len(a)) 

# for i in range(len(a)):

for i in range(0,len(a),1):
    print(a[i])

for i in a:
    print(i)


for i in range(1,21,1):
    if(i == 15):
        print("break executed")
        break
    print(i)
else:       # this else is used with break statement
            # the same else is used with if else
            #else is also related to for
    print("break is not executed")

# sum upto 100
sum = 0
for i in range(101):
    sum = sum + i
print(sum)   

# factorial upto 100
fact = 1
for i in range(1,6):
    fact = fact * i
print(fact)   

# print sum of even and odd
n = int(input("enter no"))

even_sum = 0
odd_sum = 0

for i in range(1,n+1,1):
    if(i%2 == 0):
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
print(f"odd sum is: {odd_sum}")
print(f"even sum is: {even_sum}")

# factors of a no

n = int(input("enter no"))
for i in range(1,n+1,1):
    if n%i == 0:
        print(i)

# check for a perfect no (sum of factors = no)

sum_fact = 0
n = int(input("enter no"))
for i in range(1,n,1):
    if n%i == 0:
        sum_fact = sum_fact + i
if sum_fact == n:
    print("perfect") 
else:
    print('not perfect')       
'''
'''

# reverse a string without func
a = "saswat"
# print(a[::-1])
# by for loop
rev_str = ""
for i in range(len(a)-1, -1, -1):
    rev_str = rev_str + a[i]
    print(a[i])
print(rev_str)

# palindrome or not string

n = input("enter name")
rev_str = ""
for i in range(len(n)-1, -1, -1):
    rev_str = rev_str + n[i]
if rev_str == n:
    print("Palindrome")
else:
    print("Not a Palindrome")    

# count no of char

str = "1asd2q332532241%^##%"
count = 0
for i in str:
    count = count+1
print(count)

# count digits, special symbols and alphabets seperately

str = "123456SASWAT!@^#SAHAY)(*&)%"
digit_sum = 0
alphabet_sum = 0
special_char_sum = 0
for i in str:
    if i.isdigit():
        digit_sum = digit_sum + 1
    elif i.isalpha():
        alphabet_sum = alphabet_sum + 1
    else:
        special_char_sum = special_char_sum + 1    

print(f"total digit are {digit_sum} alphabet are {alphabet_sum} special character are {special_char_sum}")
'''
# print(dir(str)) #to check all the functions and methods of str

# while

# separate each digit of a number

a = 123432145
while a>0:
    last_digit = a%10
    print(last_digit)
    a = a//10

# reverse the number

n = 123987
rev_dig = 0
while n>0:
    last_digit = n%10
    rev_dig = rev_dig *10 + last_digit
    n //= 10
print(rev_dig)     

# no is palindrome or not

p_num = 1212121
copynum = p_num
reverse = 0
while p_num > 0:
    last_digit = p_num % 10
    reverse = reverse * 10 + last_digit
    p_num = p_num//10
if copynum == reverse:
    print("palindrome")    
else:
    print("palindrome")

# guess the number game
import random
random_num = random.randint(1,10)
# print(random_num)
guess = int(input("enter your guess"))
attempts = 1
if guess == random_num:
    print(f"you have selected right and your guess is {guess}")
    print(f"total attempts:- {attempts}")
else:
    if random_num > guess:
        print(f"random number is bigger")
    else:
        print("random number is smaller")
while guess != random_num:
    guess = int(input("enter your guess"))
    attempts += 1
    if guess == random_num:
        print(f"you have selected right")
    else:
        if random_num > guess:
            print(f"random number is bigger")
        else:
            print(f"random number is smaller")
print(f"total attempts:- {attempts}")
