# Mh 2nd Password strength checker

# List of outputs
outputs = ["Password still needs:"]
# amount of points = 0
points = 0
# special characters
spec_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "[", "]", "{", "}", "|", ";", ":", ",", ".", "<", ">", "?"]

# while loop that runs until user has a complete password
while True:
    # asks user for password
    password = str(input("What is your password?"))
    print(password)
    # LOOP ONE
        # if password is at least 8 characters add one point
        # else add no points and add "You must have at least 8 characters" to list of outputs
    if len(password) >= 8:
            points += 1

    else: 
            outputs.append("At least 8 characters")

     # LOOP TWO
        # if password contains at least one uppercase letter add one point
        # else add no points and add "You must have at least one uppercase letter" to list of outputs
    for i in password:
        if i.isupper():
            points += 1
            break

        else:
            outputs.append("At least one uppercase letter")
            break

    # LOOP THREE
        # if password contains at least one lowercase letter add one point
        # else add no points and add "You must have at least one lowercase letter" to list of outputs
    for i in password:
        if i.islower():
            points += 1
            break
         
        else:
            outputs.append("at least one lowercase letter")
            break

    # LOOP FOUR
        # if password contains at least one number add one point
        # else add no points and add "You must have at least one number" to list of outputs
    for i in password:
        if i.isalnum():
            points += 1
            break
            
        else:
            outputs.append("At least one number")
            break
    # LOOP FIVE
        # if password contains at least one special character add one point
        # else add no points and add "You must have at least one special character" to list of outputs   
    if spec_chars in password:
        points += 1

    else:
        outputs.append("At least one special character")

    
    # disply points
    print(f"Your password strength is {points}/5 points.")
    # LOOP SIX
        # if points = 5 stop running code
        # else go back to start of program and display changes that need to be made
    if points == 5:
        break
    
    else:
        print(outputs)
