# Mh 2nd Password strength checker

# List of outputs
outputs = ["Password still needs:"]
# amount of points = 0
points = 0
# special characters
spec_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "[", "]", "{", "}", "|", ";", ":", ",", ".", "<", ">", "?"]
# if conditions
upper = False
lower = False
num = False
spec = False
# while loop that runs until user has a complete password
while True:
    # asks user for password
    password = str(input("What is your password?\n"))
    points = 0
    outputs = ["Password still needs:"]
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
            upper = True
            break

    if upper == False:
        outputs.append("At least one capital letter")

    # LOOP THREE
        # if password contains at least one lowercase letter add one point
        # else add no points and add "You must have at least one lowercase letter" to list of outputs
    for i in password:
        if i.islower():
            points += 1
            lower = True
            break
         
    if lower == False:
        outputs.append("At least one lowercase letter")

    # LOOP FOUR
        # if password contains at least one number add one point
        # else add no points and add "You must have at least one number" to list of outputs
    for i in password:
        if i.isdigit():
            points += 1
            num = True
            break
            
    if num == False:
        outputs.append("At least one number")
    # LOOP FIVE
        # if password contains at least one special character add one point
        # else add no points and add "You must have at least one special character" to list of outputs   
    password = list(password)
    
    for i in password:
        if i in spec_chars:
            points += 1
            spec = True
            break
    if spec == False:
        outputs.append("At least one special character")

    
    password = str(password)
    
    # disply points
    print(f"Your password strength is {points}/5 points.")
    # LOOP SIX
        # if points = 5 stop running code
        # else go back to start of program and display changes that need to be made
    if points == 5:
        break
    
    else:
        print(outputs)
