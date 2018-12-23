
# Declare a variable and initialise it
f = 0
print(f)


#re-declaring the variable works
f = "hello"
print(f)


# ERROR: variables of different types cannot be combined
# print("this is str " + 123)  # TypeError: cannot concatenate str and int objects
print("this is str " + str(123))  # Output : 'this is str123'


# Global vs local variables in functions

def someFunction():
    f = "def" # local variable
    print(f)


def anotherFunction():
    global f
    f = "def"
    print(f)

someFunction()
print(f)

print("---------")
anotherFunction()
print(f)

del(f) # deletes the variable on run time
print(f)
