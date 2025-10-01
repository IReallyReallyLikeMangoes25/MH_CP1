# MH 2nd For Loops Notes

import time

nums = [6, 8, 400, 3, 200, 5, 900, 7, 1]

for num in nums:
    div = num/2
    if div >= 100:
        print(f"{div} is half of num and it is still a large number.")
    else:
        print(num)\
               
print("We've completed all the numbers!")
time.sleep(3)

print("New list.")
for x in range(1, 10):
    print(x)

time.sleep(3)

print("Counting by two's.")
for x in range(2, 10, 2):
    print(x)

time.sleep(3)

print("Counting down.")
for x in range(10, 0, -1):
    time.sleep(1)
    print(x)