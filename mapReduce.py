#MAP
def cube(x):
  return x*x*x
print(cube(2))

l=[1,2,3,4,5]
""" newl=[]
for item in l:
  newl.append(cube(item)) """
# newl=list(map(cube,l))  
newl=list(map(lambda x:x*x*x,l))
print(newl)  

#FILTER
def filter_function(a):
  return a>4

# newnewl=list(filter(filter_function,l))
newnewl=list(filter(lambda a:a>4,l))
print(newnewl)

#reduce
from functools import reduce
number=[1,2,3,4,5]
def mysum(x,y):
  return x+y
sum=reduce(mysum,number)
print(sum)
