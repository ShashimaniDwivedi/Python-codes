a = int(input("Enter your age : "))
print("Your age is ", a)
if (a > 18):
    print("You can drive")
elif (a == 18):
    print("You can also drive but be careful")
else:
    print("You cannot drive")
# Nested if else statements
num = 10
if (num < 0):
    print("Negative number")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1 to 10")
    elif (num >= 10 and num <= 20):
        print("Number is between 11 to 20")
    else:
        print("Number is between 21 to 30")
else:
    print("Number is 0")
