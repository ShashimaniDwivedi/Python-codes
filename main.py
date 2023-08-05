import pandas
import hashlib
"""
Multiple line comment
our first python program
"""
# Single line comment

print("Hello world hey,4,5,6 \"I am a good boy\"\nBye", end="\n")
print("Hey", 4, 5, sep="~")
a = 1234567889
print(a)
b = "Manas"
print("The type of b is : ", type(b))
c = True
d = None
print(type(c), type(d))
e = complex(3, 4)
print(e)
list = [3, 4, 6, 2, ["Banana", "Mango"], [2.3, 4.5]]
print(list)
tuple = (("Code", "Harry"), ("RAM", "SITA"), 3, 4, 5)
print(tuple)
dict = {"Name": "Shashi", "Age": 18, "Height": "6Ft"}
# print(dict)
apple = """He said,
Hi Harry
Hey I am good
"I want to eat an apple\""""
name = "apple"
print(apple)
print(name[0])
print("Let's Use For Loop")
for character in apple:
    print(character)
names = "Harry,Manas"
print(names[0:5], len(names))  # to find length of string
# names[:] give full name                 negative Slicing
# behind the scene names[0:len(names)-3]
# behind the scene names[len(names)-3:len(names)-1]
# including 1 but not 3
print(names[1:3], names[:5], names[:], names[5:], names[0:-3], names[-3:-1])
nm = "Harry*****Raj Paul"
# new copy of string strings are immutable
print(nm.upper(), nm.lower(), nm.strip(),
      nm.rstrip("*"), nm.replace("Harry", "Manas"), nm.split(" "))
blogHeading = "introduction to python"
print(blogHeading.capitalize())
str = "Welcome to the Console Python interpreter!\n"
print(len(str))
print(len(str.center(50)))
print(str.center(50))
print(nm.count("Harry"))
print(str.endswith("!"))  # give Boolean value
print(str.endswith("to", 4, 10))
str1 = "My name is manas!"
print(str1.find("is"))
# print(str1.index("isjv"))  # Throw exception Value error
str2 = "World Health Organization"
print(str.isalnum())
print(str.isalpha())
print(str.isprintable())
print(str.isspace())
print(str2.istitle())
print(str2.swapcase())
print(str2.title())
