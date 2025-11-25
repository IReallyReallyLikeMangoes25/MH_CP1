# Mh 2nd factorial calculator practice
# The pseudocode I was given was unfinished, so I had to fill in some spaces

# Make a variable named numbers, a user input
# moved the input inside of a while loop
# make the input an int fom the user "numbers = input"
# I removed this and if the input was a digit I turned it into an integer
# define function for numbers
# changed function name from numbers to factorial to make it more understandable
def factorial(num):
# numbers = []
# I removed the list because it was never used in the function as the function pseudocode was unfinished (I added the whole function after this, there was a for  loop in the pseudocode, but I added everything in the for loo[])
    # I added a parameter to take in the input
    # assigned a value to multiply by
    factor = 1
    # added a for loop to loop over the numbers to multiply by
    for i in range(num):
        factor *= (i + 1)
    # added a return statement
    return factor

# put this in a while loop
# input validation - Also unfinished and very unclear, in total what I added was the while and the for loop, and changed the if/elif/else to two if statements
# if number is not integer return false
# return can't be used here, so I removed it, and you can't check if it's not an integer, so I used isdigit in its place
# added a while loop and created an is_num boolean to help it run
is_num = False
while is_num != True:
    number = input("what number would you like the factorial of?\n")
    is_num = True
    # print(that is not valid, try again)
    # elif numbers  = [0]
    # print numbers
    # I removed this part because "elif numbers = [0]" is calculated within the function, making this piece a logic error
    # I changed the if as i said earlier, and added a for loop around it in case they input a number that had more than one character
    for i in number:
        if i.isdigit() != True:
            print("That is not valid, try again.")
            is_num = False

    # else:
    # print "that is not valid, try again!"
    # I changed this else because it was doing the same thing done by the if written earlier, so I combined the two to prevent errors
    # I also added the output statement
    if is_num == True:
        number = int(number)
        print(f"{number} factorial is {factorial(number)}")