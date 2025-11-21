# Mh 2nd factorial calculator practice

# Make a variable named numbers, a user input
# changed this to number
number = int(input("what number would you like the factorial of?"))
# make the input an int fom the user "numbers = input"
# I removed this and just put int in the input
# # define function for numbers
def numbers(num):
# numbers = []
    nums = []
    # I added a parameter to take in the input and the factor variable
    factor = num
# for i in numbers
# changed numbers to num, my paramter
    for i in num:
# I added everything after this, as it was unfinished
        nums.append(factor - i)
    
    for i in nums:
        factor *= i

    return factor

# put this in a while loop
# input validation
# if number is not integer return false
# return doesn't need to be used here so i removed it
while number != int:
    if number is not int:

    # print(that is not valid, try again)
        print("That is not valid, try again!")
    # elif numbers  = [0]
    elif numbers == 0:
    # print numbers
    # changed this output to make it more clear
        print(numbers)
    # else:
    else:
        print("That is not valid, try again!")
    # print "that is not valid, try again!"