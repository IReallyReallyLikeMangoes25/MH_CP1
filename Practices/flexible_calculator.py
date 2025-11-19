# MH 2nd flexible calculator practice

# SUM:
def add(*nums):
    nums = nums[0]
    # take all numbers in 
    # add them all
    # return the sum of all numbers
    return sum(nums)

# AVERAGE:
def average(*nums):
    nums = nums[0]
    # take all numbers in
    # save how many there are
    how_many = 0
    total = 0
    # add all one by one
    for num in nums:
        total += num
        how_many += 1
    # divide the sum by the amount of numbers
    avg = total/how_many
    # return the average
    return avg


# MAX:
def maximum(*nums):
    nums = nums[0]
    # takes all numbers in
    # compares all numbers
    # returns highest number
    return max(nums)

# MIN:
def minimum(*nums):
    nums = nums[0]
    # takes all numbers in
    # compares all numbers
    # returns lowest number
    return min(nums)


# PRODUCT:
def product(*nums):
    nums = nums[0]
    # takes in all numbers
    # multiplys all numbers
    multiplied = nums[0]
    del nums[0]
    for num in nums:
        multiplied *= num
    # returns product
    return multiplied

# ask user what operation they would like to perform
operation = int(input("What operation would you like to perform:\n1. Sum\n2. Average\n3. Maximum\n4. Minimum\n5. Product\n"))

# take in users numbers
how_many = int(input("How many numbers will this operation be performed upon?\n"))
numbers = []

for num in range(how_many):
    num = int(input("Number: "))
    numbers.append(num)

if operation == 1:
    print(f"The sum of those numbers is {add(numbers)}")

elif operation == 2:
    print(f"The average of those numbers is {average(numbers)}")

elif operation == 3:
    print(f"The maximum of those numbers is {maximum(numbers)}")

elif operation == 4:
    print(f"The minimum of those numbers is {minimum(numbers)}")

elif operation == 5:
    print(f"The product of those numbers is {product(numbers)}")

else:
    print("You input an invalid operation, please try again.")