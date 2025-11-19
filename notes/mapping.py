# MH 2nd mapping notes

nums  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""divided = []

for num in nums:
    divided.append(num/2)"""

def divide(num):
    return num/2

divided = list(map(lambda num: num/2, nums))

print(divided)

#for i, num in enumerate(nums):
#    print(f"{num} divided by two = {divided[i]}")