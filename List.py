# list in python
l = [3, 5, 6, "Code with harry", 7, 5, 9, 10]
print(type(l))
print(len(l))
print(l[0])
print(l[1])
print(l[2])
print(l)
print(l[7])
print(l[-1])
# Checking element is present or not in the list
if 5 in l:
    print("Yes")
else:
    print("No")
if "arry" in "Harry":
    print("Yes")
else:
    print("No")
print(l[0:8:3])
# list Comprehension'
lst = [i for i in range(5)]
print(lst)
lst = [i for i in range(10) if i % 2 == 0]
print(lst)
# list methods
l1 = [1, 9, 3, 0, 5, 3, 7, 6, 8]
print(l1.index(0))
l1.sort()  # For ascending order
l1.sort()
print(l1)
l1.sort(reverse=True)  # For descending order
print(l1)
l1.reverse()
print(l1)
print(l1.index(7))
print(l1.count(3))  # count number of items
m = l1.copy()
m[0] = 12
print(l1)
l1.insert(1, 13)
print(l1)
n = [900, 10000, 110000]
# l1.extend(n)
# print(l1)
k = l1+n
print(k)
