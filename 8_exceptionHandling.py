# syntax error, indentation error are not handled by exception handling

# zero division error

a = int(input("enter number: "))

# print(10/a)  # now this line cause an error when a will be 0
# to avoid this error or exception we can do this

try:
    print(10/a)
except ZeroDivisionError:
    print("u cannot divide by 0")

print("division completed")

# now since we 
