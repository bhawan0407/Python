# define a basic function
def func1():
    print ("basic function-1") # this can be 2,3,4 spaces but the spaces/tabs
                               # must be consistent within a scope


# define a function with arguments
def func2(arg1, arg2):
    print(arg1 , " " , arg2)


# define a function with return value
def cube(x):
    return x*x*x


# function with default value of an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result *= num

    return result


func1()                         # basic function-1
print(func1())                  # basic function-1
                                # None 
print(func1)                    # function object


func2(10, 20)                   # 10 20
print(func2(10, 20))            # 10 20
                                # None

print(cube(3))                  # 27

print(power(5,3))               # 125
print(power(5))                 # 5
