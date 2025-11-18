# powers
# immutable, allows duplicates, hetrogenious, ordered

t = (1,2.2,print(),"hell", True, False,1,2,3,6,5,1,2)
# methods
# 1. index finding  -   finds the first occurence of elements
index = t.index("hell")
# print(index)

# count - count no of times the elemetns exists

c= t.count(1)
print(c)    # in the list 1 is total 3 times but we are getting 4 as otput, it is because True is also taken as 1 in python


# Tuple unpacking
a = (1,2,3)
print(type(a)) # output tuple

a = (1)
print(type(a)) # output int

a,b,c = (1,2,3) #this is tuple unpacking
                #storing single values in different variable
print(a)
print(c)
print(b)

# now 

a = (1)
print(type(a)) #int
a = (1,)
print(type(a)) #tuple

# sets
s = {} #dictionary
s = {1,2,3} #set
# powers
# mutable, duplicates not allowed (because of hash value (learn it later)), unordered (cannot access by index), semi-hetrogenious (can store datatypes like strings, numbers, tuples but not everthing)


# print(s[0])     #not allowed

# set traversal
set1 = {1,2,8,4,3,9,"saswat",18,28,15}

for i in set1:
    print(i)  #when you print it multiple times you will see that there is not order is followung in the printing that is no sequenecce

# set methods
s = {3,1,5,2,"saswat"}
# 1. add(18) - adds an element at random place to the set
s.add(18)
print(s)
# 2. remove(2) - removes 2 (raises an error if not found)
s.remove(2)
print(s)
# 3. discard() - removes 5 - no error if not found)
s.discard(4)
print(s)
# 4. pop() - removes a random element
s.pop()
print(s)
# 5. clear() - removes all elements
s.clear()
print(s)

# 6. union
a = {1,2,3}
b = {2,3,4,5}

# s = a.union(b)
# s = a|b   # shortcut for union
# print(s)

# 7. intersection
# s = a.intersection(b)
# s = a&b
# print(s)

# 8. difference
# s = a.difference(b)
# s = b.difference(a)
# s = a-b
# s = b-a
# print(s)

# 9. symmetric difference
# s = a.symmetric_difference(b)
# s = a^b
# print(s)

# we can aslo do compund operation (-=, ^=, |=, &=)
# e.g

print("lets see compound operations")
print(b)
b -= a
print(b)