l=int(input("Enter number : "))
l1=[]
while(l>0):
  digit=l%10
  l1.append(digit)
  l=l//10
  
l1.sort()
num=0
for digit in l1:
  num = num * 10 + digit
print(num)  