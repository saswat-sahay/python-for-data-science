# syntax error, indentation error are not handled by exception handling

# try       Wrap the block of code that might cause an exception.
# except    Handle the exception if it occurs
# else      Run code only if no exception occurs
# finally   Run code no matter what, whether there's an exception or not
# raise     Manually throw an exception


# zero division error

a = int(input("enter number: "))

# print(10/a)  # now this line cause an error when a will be 0
# to avoid this error or exception we can do this

try:
    print(10/a)
except ZeroDivisionError:
    print("u cannot divide by 0")

print("division completed")

# now since we dont have only zero division error
# lets go for a general method for handling exceptions

a = int(input("enter number: "))

try:
    print(10/a)
except Exception as err:
    print(f"sorry this is an {err}")

# else - runs if except didnot run
else:
    print("good no exception")

finally:
    print("it will run always")

# raise

age = int(input("enter age"))
try:
    if age<18:
        raise ValueError("your age must be greater than 18")
    else:
        print("welocme to the voterlist")
except Exception as err:
    print(f"the error is {err}")
print("the voting will start soon")