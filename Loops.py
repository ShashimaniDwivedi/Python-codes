name = "Abhishek"
for i in name:
    print(i)
colors = ["Red", "Green", "Blue", "Yellow", "Orange"]
for color in colors:
    print(color)
    for X in color:
        print(X)
        print("Using for loop")
for K in range(1, 200, 5):
    print(K)
j = 5
print("Using While Loop")
while (j > 0):
    print(j)
    j = j-1
else:
    print("I am inside else")

# Emulate Do While Loop using while loop
print("Emulating do while loop using while loop")
i = 1
while True:
    print(i)
    i = i+1
    if (i % 10 == 0):
        break
print("*************")
# loop with else
for i in range(5):
    print(i)
else:
    print("Loop ctrl finished")
# loop with break and else
print("*************")
for i in range(5):
    print(i)
    if (i == 4):
        break
else:  # else block will not execute
    print("Loop ctrl finished")
print("*************")
i = 0
while i < 7:
    print(i)
    i = i+1
else:
    print("Loop ctrl finished")

for x in range(5):
    print("Iteration no {} in for loop".format(x))
