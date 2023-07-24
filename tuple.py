tuple5 = (1, 3, 4, 5, 6, 7)
tuple1 = ("Red", "Green", "Yellow")
tuple2 = (5,)
print(tuple2)
print(type(tuple1))
print(tuple1)
print(tuple[0], tuple[1], tuple[2], tuple[3])
# check if element is present in tuple
if 5 in tuple5:
    print("5 is present in tuple")
else:
    print("5 is not present in tuple")
# printing the element with in range
tup = tuple5[0:4:2]
print(tup)
tup1 = tuple5[-6:-1:2]
print(tup1)
# To make changes in tuple we convert it to list
country = ("Spain", "Italy", "India", "England", "Germany")
temp = list(country)
temp.append("Russian")
temp.pop(1)
temp[2] = "Bengaluru"
country = tuple(temp)
print(country)
country1 = ("Pakistan", "China")
n = country+country1
# to concate two tuple
print(n)
tuple5 = (3, 2, 5, 1, 1, 6, 9, 7)
print("Number of occurence Of 1 in tuple is : ", tuple5.count(1))
print(tuple5.index(1))
print(tuple5.index(1, 4, 6))
