""" #Reading a file
f=open("Manas.txt",'r')
text=f.read()
print(text)
f.close
#Writing a file
a=open("Manas.txt",'a')# It preserves old content
a.write("Hello world!")
a.close()
#In this you don't need to close the file
with open("Manas.txt",'a') as f:
  f.write("Hey I am Inside Text File") """
  
""" b=open("Manas.txt",'r')
while True:
  #It read data line by line
  line=b.readline()
  print(line)
  if not line :
   break  
  """
b=open("write.txt",'r')
i=0
while True:
  i=i+1
  line=b.readline()
  if not line :
    break   
  m1=int(line.split(",")[0])
  m2=int(line.split(",")[1])
  m3=int(line.split(",")[2])
  print(f"Marks of student {i} in Maths is : {m1*2}")
  print(f"Marks of student {i} in Physics is : {m2*2}")
  print(f"Marks of student {i} in Chemistry is : {m3*2}")
  
  print(line) 
  
  
f=open("write1.txt",'w')
lines=['lines1\n','lines2\n','lines3\n']
f.writelines(lines)
f.close()

with open("write2.txt",'r') as f:
 f.seek(10)# Move cursor to 10 bytes
 print(f.tell())# return current position of cursor
 data=f.read(5)
 print(data)
 
with open("write3.txt",'w') as f:
 f.write("Hello world!")
 f.truncate(5)