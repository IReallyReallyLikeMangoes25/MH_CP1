# MH 2nd flexible calculator practice

# SUM:
def sum(*nums):
    # take all numbers in
    total = 0 
    # add them all one by one
    for num in nums:
        total += num
    # return the sum of all numbers
    return total

# AVERAGE:
def average(*nums):
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
def max(*nums):
    # takes all numbers in
    biggest = float('-inf')
    # takes first number, compares it to second
    for num in nums:
    # if the first number is bigger, compare it to the next
    # if the second number is bigger, compare it to the next
        if num >= biggest:
            biggest = num
    # do this for all numbers
    return biggest

# MIN:
def min(*nums):
    smallest = float('inf')
    # takes all numbers in
    # takes first number, compares it to second
    for num in nums:
    # if the first number is smaller, compare it to the next
    # if the second number is smaller, compare it to the next
        if num <= smallest:
            smallest = num
    # do this for all numbers
    return smallest

# PRODUCT:
def product(*nums):
    # takes in all numbers
    numbers = []
    # multiplys all numbers
    for num in nums:
        numbers.append(num)

    multiplied = numbers[0]
    numbers.pop(0)

    for number in numbers:
        multiplied *= number
    # returns product
    return number

# ask user what operation they would like to perform
operation = int(input("What operation would you like to perform:\n1. Sum\n2. Average\n3. Maximum\n4. Minimum\n5. Product\n"))

# take in users numbers
how_many = int(input("How many numbers will this operation be performed upon?\n"))
numbers = []

for num in range(how_many):
    int(input("Number: "))
    numbers.append(num)

if operation == 1:
    print(f"The sum of those numbers is {sum(numbers)}")

elif operation == 2:
    print(f"The average of those numbers is {average(numbers)}")

elif operation == 3:
    print(f"The maximum of those numbers is {max(numbers)}")

elif operation == 4:
    print(f"The minimum of those numbers is {min(numbers)}")

elif operation == 5:
    print(f"The product of those numbers is {product(numbers)}")