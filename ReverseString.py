# ***************CASE 1********* 
# Reversing string while preserving its position
""" s=input("Enter String : ")
l=s.split(" ")
s1=""
for i in l:
  s1+=i[::-1]+" "
print(s1)    """ 
# ************CASE 2************
# Reversing word in String
s = input("Enter a sentence : ") 
l=s.split(" ")
s1=l[::-1]
s2=" ".join(s1)
print(s2) 
 