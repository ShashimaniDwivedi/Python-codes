# factorial program
def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n*fact(n-1)


print(fact(5))
# Fibonnaci Program

n = 10


def fib(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)


# To print in same line
for i in range(n):
    print(fib(i), " ", end="")
