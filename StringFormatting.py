letter = "Hey my name is {} and I am from {}"
# letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Manas"
print(letter.format(name, country))
# print(letter.format(country,name))
# ********fstring*********
print(f"Hey my name is {name} and I am from {country}")
# to print as it is
print(f"Hey my name is {{name}} and I am from {{country}}.")
price = 49.0546435
txt = f"for only {price:.2f} dollar!"
print(txt.format(price=49.0546435))
print(txt)

# *******DocString******


def square(n):
    '''Takes in a number n,returns  the square of n'''
    print(n**2)


square(5)
print(square.__doc__)
# *********sets**********
info = {2, 4, 2, 5, 7, 2, 2, 2}
print(info)
# empty set
val = set()
print(type(val))
# empty dictionary
val1 = {}
print(type(val1))
for i in info:
    print(i, " ", end="\n")
# *****setmethod********
s1 = {1, 2, 3, 4, 4}
s2 = {5, 6, 7, 2, }
print("Union : ", s1.union(s2))
print(s1, " ", s2)
s1.update(s2)
print(s1, " ", s2)
a1 = {1, 2, 3, 3, 4, 2}
a2 = {5, 7, 2, 4, 1}
print("Intersection : ", a1.intersection(a2))
print(a1, " ", a2)
a1.intersection_update(a2)
print(a1, " ", a2)
b1 = {1, 2, 3, 4, 5}
b2 = {5, 6, 7, 2, 3, 1, }
print("Symmetric diffrence : ", b1.symmetric_difference(b2))
print(b1, " ", b2)
b1.symmetric_difference_update(b2)
print(b1, " ", b2)
c1 = {1, 2, 5, 3, 6, 7}
c2 = {8, 1, 6, 3, 9}
print("Difference : ", c1.difference(c2))
c1.difference_update(c2)
print(c1, " ", c2)
d1 = {"Delhi", "Madras", "Goa", "Lucknow"}
d2 = {"Lucknow", "Kanpur", "Madras", "Surat"}
print(d1.isdisjoint(d2))
e1 = {"Delhi", "Madras", "Goa", "Lucknow"}
e2 = {"Lucknow", "Kanpur", "Madras", "Surat"}
print(e1.issuperset(e2))
e1 = {"Delhi", "Madras", "Goa", "Lucknow"}
e2 = {"Lucknow", "Kanpur", "Madras", "Surat", "Goa", "Delhi"}
print(e1.issubset(e2))
e1.add("Ladakh")
print("Adding element in set : ", e1)
e1.update(e2)
print("Updation : ", e1)
e1.remove("Ladakh")
print("Removing element in set : ", e1)
e1.discard(e2)
print("Discard : ", e1)
e1 = {"Delhi", "Madras", "Goa", "Lucknow"}
item = e1.pop()
print(e1, " ", item)
e1 = {"Delhi", "Madras", "Goa", "Lucknow"}
del e1
# print(e1) throws name error
e1 = {"Delhi", "Madras", "Goa", "Lucknow"}
e1.clear()
print(e1)
e1 = {"Delhi", "Madras", "Goa", "Lucknow"}
if ("Goa" in e1):
    print("Present")
else:
    print("not present")
