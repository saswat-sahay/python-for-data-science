'''
dict1 = {
    # key : value
    1: "hello"
}

# powers
# mutable (change, add, remove key value pair after creation), duplicates (keys must be unique but values can be duplicate), ordered (dict follows insertion order), heterogenious (can have different types of keys and value like integers, strings, lists or even another dict itself)

d = {
    10:100, 
    20:200,
    30:300,
    40:400
}

# print(d[0]) # wrong becuase index is not available
print(d[10])  # we have to go by the keys

d[10] = 150 # (change value) (update value)
print(d)

# update  function (used to create new key value pairs)
# d.update({50:5000})
d[50] = 500
print(d)
del d[30]   #delete
print(d)
'''
# traversal

d = {
    10:100, 
    20:200,
    30:300,
    40:400
}

# for i in d:
    # print(i)
    # print(d[i])

# for k in d.keys():  # keys() are bydefault
#     print(k)

# for v in d.values():
#     print(v)    

# methods
d = {
    10:100, 
    20:200,
    30:300,
    40:400
}

# 1. clear() -- removes all the data from dictionary
# d.clear()
# print(d)

# deep copy vs shallow copy
# deep copy -- change in the copy leads to change in the original
# shallow copy -- change in the copy doesnot leads to change in the original

# 2. copy -- shallow copy
d2 = d.copy()
d2[10] = 10
print(d2)
print(d)

# 3. items()
d3 = d.items()
print(d3)

# merge
# update and merge

d1 = {
    10:100,
    20:200
}

d2 = {
    10:1000,
    30:300,
    40:400,
    50:500,
    60:600
}

for i in d2:
    d1[i] = d2[i]

print(d1)

# sum all the values of the dict

d = {
    10:100,
    20:200,
    30:300,
    40:400
}

sum = 0
# for i in d.values():  # if use this then use sum = sum + i
for i in d: # if use this then use sum = sum + d[i]
    # sum = sum + i
    sum = sum + d[i]

print(sum)

# find frequency of each element in a list

l = [1,1,1,2,2,2,1,3,3,3,2,1,1,1,4,5,4]

dict = {}

for i in l:
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)

# merge two dictinary and add up the common key-values

d1 = {
    10:100,
    20:200
}

d2 = {
    10:100,
    20:400,
    30:300,
    40:400,
    50:500,
    60:600
}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]
print(d1)

