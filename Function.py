def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print("Geometric mean is : ", mean)


def compare(a, b):
    if (a > b):
        print(a, "is Greater than", b)
    else:
        print(b, "is Greater than", a)


def islesser(a, b):
    pass
# it mean that we complete function later on


a = 9
b = 8
calculateGmean(a, b)
compare(a, b)
c = 8
d = 7
calculateGmean(c, d)
compare(c, d)


def avg(a=1, b=3):
    print((a+b)/2)


# avg()
# avg(2, 8)
avg(3)
