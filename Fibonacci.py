n = int(input("Enter number : "))
a = 0
b = 1
c = 1
for i in range(1, n+1):
    print(c,end=" ")
    c = a+b
    a = b
    b = c
