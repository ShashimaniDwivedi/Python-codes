a = input("Enter number :")
print(f"The Multiplication Table of {a} is : ")
try:
    for i in range(11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
print("Some imp line of code")
print("End of program")
print("*********************")

try:
    num = int(input("Enter an integer number : "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Invalid Input")
except IndexError:
    print("Index Error")
# using finally
print("*********************")


def func():
    try:
        l = [1, 5, 6, 3]
        i = int(input("Enter the index : "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("I am always executed")


x = func()
print(x)
# ***************Raising custom error ****************
p = int(input("Please enter number between 4 and 9 : "))
if (p < 4 or p > 9):
    raise ValueError("Value must be between 4 and 9")


class CustomError(Exception):
    "raiseed when input is invalid"
    pass


# you need to guess this number
number = 18
try:
    number1 = int(input("Enter a number"))
    if (number1 < number):
        raise CustomError
    else:
        print("New Window")
except CustomError:
    print("Error occured")
