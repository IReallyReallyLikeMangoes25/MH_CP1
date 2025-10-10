# Mh 2nd Password strength checker

# List of outputs
outputs = ["Password still needs:"]
# amount of points = 0
points = 0

# while loop that runs until user has a complete password
while True:
    # asks user for password
    password = list(input("What is your password?"))
    print(password)
    # LOOP ONE
        # if password is at least 8 characters add one point
        # else add no points and add "You must have at least 8 characters" to list of outputs
        if password.len() >= 8:
            point += 1

        else: 
            outputs.extend("At least 8 characters")

    # LOOP TWO
        # if password contains at least one uppercase letter add one point
        # else add no points and add "You must have at least one uppercase letter" to list of outputs
        for i in password:
            if i.isupper():
                points += 1

            else:
                outputs.extend()
    # LOOP THREE
        # if password contains at least one lowercase letter add one point
        # else add no points and add "You must have at least one lowercase letter" to list of outputs
    # LOOP FOUR
        # if password contains at least one number add one point
        # else add no points and add "You must have at least one number" to list of outputs
    # LOOP FIVE
        # if password contains at least one special character add one point
        # else add no points and add "You must have at least one special character" to list of outputs   

    # disply points
    # display list of outputs

    # LOOP 3
        # if points = 5 stop running code
        # else go back to start of program
