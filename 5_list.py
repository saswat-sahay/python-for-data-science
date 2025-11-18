# powers
'''
1. mutable - changed after creation
2. allow duplicates - duplicate values are allowed
3. ordered - maintain sequence of elements as they are inserted, this means we can access values after by their position (index)
4. heterogenius - multiple datatypes inside a single list
'''
'''
list1 = [1,2.5,"a", "and", True, print()]
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
print(list1[5])

fruit = ["apple", "banana", "carrot"]
fruit[2] = "corn"

# for i in range(0, len(fruit), 1):
    # print(fruit[i])
# check why none is also printed in the output
for i in fruit:
    print(i)

'''

# methods
# print(dir(list))
# help(list)  # check why it is not giving output

'''
# 1. append
l1 = [1,2,3]
l1.append(5)
print(l1)
# 2. insert
l2 = [1,3,5]
l2.insert(1,"second")
print(l2)
# 3. remove
l3 = [1,2,3,2]
l3.remove(2)
print(l3)
# pop - 
# etc etc check from the book

# 

l = [-21, 15, 10, -2, 22, 3124, -24]

print("+ve values of this list")
for i in l:
    if i>= 0:
        print(i)

print("-ve values of this list")
for i in l:
    if i < 0:
        print(i)

# avg of list

l = [1,2.3,0,4,5,8,10,15]
sum = 0
for i in l:
    sum = sum + i
print(sum/len(l))    

# greatest element and its index

l = [45,20,14,191,91,150]
index = 0
g = l[0]
for i in range(len(l)):
    if g < l[i]:
        g = l[i]
        index = i

print(f"greatest number is {g}, and the index is {index}")

'''

# 2nd largest
l = [45,20,14,191,911,151]
largest = l[0]
sec_largest = l[0]
'''
for i in range(len(l)):
    if largest <= l[i]:
        sec_largest = largest
        largest = l[i]
    elif l[i] >= sec_largest:
        sec_largest = l[i]    
print(f"laregest is {largest} second largest is {sec_largest}")

# or

for i in l:
    if i >= largest:
        sec_largest = largest
        largest = i
    elif i >= sec_largest:
        sec_largest = i
print(f"laregest is {largest} second largest is {sec_largest}")
'''
# check if list is sorted or not
l = [45,20,14,191,91,150]
# l = [1,2,3,4,5]
'''
c= 0
low = l[0]
for i in l:
    if low > i:
        c += 1
        break
if c == 0:
    print("sorted")
else:
    print("unsorted")

'''
c = 0
for i in range(len(l)-1):
    if l[i] < l[i+1]:
        c = 1
        continue
    else:
        # print("unsorted")
        c = 0
        break
if c== 1:
    print("sorted")

else:
    print("unsorted")