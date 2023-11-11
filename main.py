def add(a, b):
    print(a + b)


# Default argument come after non-default argument
def squa(a, b=2):
    print(a ** b)


# Positional Argument
add(2, 3)

# Keyword argument
add(b=5, a=3)

# Default Argument
squa(5)


# Arbitrary Argument 1. (Variable length)
# Take input as "TUPLE"
def addAllNum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


res = addAllNum(1, 2, 3, 4, 5)
print("Sum of all numbers : ", res)


# 2.Keyword Argument
def studentInfo(**kwargs):
    for i, j in kwargs.items():
        print(i, "is", j)


studentInfo(Name="Manas", age=19, city="Lucknow")


def outer_func():
    x = 1

    def inner_func():
        y = 2
        result = x + y
        return result

    return inner_func()


output = outer_func()
print(output)


# Pass by Value(Immutable Objects)
def sum1(a, b):
    a += 1
    b += 1
    print(a, b)


a = 2
b = 3
print("Inside func : ", end="")
sum1(a, b)
print("Outside func : ", a, b)


# Pass by Reference(Mutable Objects)
def modify_list(lst):
    lst.append(4)
    print("Inside list", lst)


lst = [1, 2, 3]
modify_list(lst)
print("Outside func : ", lst)
