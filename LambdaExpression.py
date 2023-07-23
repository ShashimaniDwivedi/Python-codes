# def double(x):
#   return x*2

#using lambda function
double = lambda x:x*2
cube=lambda x:x*x*x
avg=lambda a,b,c:(a+b+c)/2
print(double(5))
print(avg(4,3,2))

def apply(fx,value):
  return 6+fx(value)

print(apply(cube,2))
print(apply(lambda x:x*x*x,2))