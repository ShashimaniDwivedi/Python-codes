import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime("%H"))
if (hour < 12 and hour > 0):
    print("Good morning Sir!")
elif (hour >= 12 and hour < 18):
    print("Good afternoon Sir!")
elif (hour >= 18 and hour < 0):
    print("Good evening Sir!")
else:
    print("Good Night Sir!")
