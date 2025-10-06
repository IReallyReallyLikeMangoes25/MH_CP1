# Mh 2nd Rock paper scissors practice

import random
import time

rock = 1
paper = 2
scissors = 3
lizard = 4
spock = 5

while True:
    play_quit = input("Would you like to play, or quit?\n")
    play_quit.lower
    play_quit.strip

    if play_quit == "quit":
        print("Bye!")
        break
    elif play_quit == "play":
        print("Welcome to rock paper scisors lizard spock!")
        time.sleep(.10)
        hand = input("Would you like to play rock, paper, scissors, lizard, or Spock?\n")
        hand.lower
        hand.strip
        opp = random.randint(1, 5)
        if opp == rock and hand == "rock":
            print("We both played rock! It's a tie!")
        
        elif opp == rock and hand == "scissors":
            print("I played rock, you played scissors! Rock crushes scissors, I win!")
        
        elif opp == rock and hand == "paper":
            print("I played rock and you played paper! paper covers rock, you win!")

        elif opp == rock and hand == "lizard":
            print("I played rock and you played lizard! Rock crushes lizard, I win!")

        elif opp == rock and hand == "spock":
            print("I played rock and you played Spock! Spock vaporizes rock, you win!")

        elif opp == paper and hand == "paper":
            print("We both played paper! It's a tie!")

        elif opp == paper and hand == "scissors":
            print("I played paper and you played scissors! Scissors cuts paper, you win!")

        elif opp == paper and hand == "lizard":
            print("I played paper and you played lizard! Lizard eats paper, you win!")

        elif opp == paper and hand == "spock":
            print("I played paper and you played Spock! paper disproves Spock, I win!")
        
        elif opp == paper and hand == "rock":
            print("I played paper and you played rock! Paper covers rock, I win!")

        elif opp == scissors and hand == "scissors":
            print("We both played scissors! It's a tie!")

        elif opp == scissors and hand == "rock":
            print("I played scissors and you played rock! Rock crushes scissors, you win!")

        elif opp == scissors and hand == "paper":
            print("I played scissors and you played paper! Scissors cuts paper, I win!")

        elif opp == scissors and hand == "spock":
            print("I played scissors and you played Spock! Spock smashes scissors, you win!")
        
        elif opp == scissors and hand == "lizard":
            print("I played scissors and you played lizard! Scissors decapitates lizard, I win!")
        
        elif opp == lizard and hand == "lizard":
            print("We both played lizard! It's a tie!")

        elif opp == lizard and hand == "scissors":
            print("I played lizard and you played scissors! Scissors decapitates lizard, you win!")

        elif opp == lizard and hand == "paper":
            print("I played lizard and you played paper! Lizard eats paper, I win!")

        elif opp == lizard and hand == "spock":
            print("I played lizard and you played Spock! Lizard poisons Spock, I win!")
        
        elif opp == lizard and hand == "rock":
            print("I played lizard and you played rock! Rock crushes lizard, you win!")

        elif opp == spock and hand == "spock":
            print("We both played Spock! It's a tie!")

        elif opp == spock and hand == "scissors":
            print("I played Spock and you played scissors! Spock smashes scissors, I win!")

        elif opp == spock and hand == "paper":
            print("I played Spock and you played paper! paper disproves Spock, you win!")

        elif opp == spock and hand == "lizard":
            print("I played Spock and you played Lizard! Lizard poisons Spock, You win!")
        
        elif opp == spock and hand == "rock":
            print("I played Spock and you played rock! Spock vaporizes rock, I win!")

        else:
            print("that is not a valid input.")

        




#⠀⠀⠀        ⢀⣠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⠉⠉⠙⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⢀⣤⡶⠶⢶⣤⣄⣀⠘⠛⠶⣴⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⣾⡇⠀⠀⠀⠈⠙⢿⣿⣷⣶⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠘⢷⣄⡀⠀⠀⢀⣸⡟⠉⠙⠻⣿⣿⣿⣷⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠉⠛⠛⠛⠛⠉⠀⠀⢸⣦⣄⡉⠛⠿⣿⣿⣿⣿⣿⣶⣤⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣆⠀⠀⠙⠻⢿⣿⣿⣿⣿⣷⣄⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣦⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣷⡀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣷⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠓⠀⠀⠀⠀⠀⠀⠀⠀

#⠀⠀⣀⣀⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣞⠁⠨⠭⠱⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠈⠫⡒⠀⠀⡄⣽⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠘⣄⣠⢿⣿⢱⡿⠋⣷⣦⣜⠱⡀⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠈⡯⣄⡁⠈⠁⢸⣟⣁⢈⣷⣜⣷⣋⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠃⢈⡿⠦⣄⣀⡇⢀⡉⠋⠀⠙⢧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠠⣤⢄⣸⢸⠀⠀⠀⠈⡇⢨⠷⠤⠤⠥⠸⣁⡀⠹⢩⠒⠒⢲⢄⠀⠀
#⠀⣺⡿⠧⠤⠊⣀⣶⣶⣶⡁⣸⠀⠀⠀⠀⠀⠀⠀⠉⠁⠒⠠⢄⡐⠓⡄
#⠀⠁⠀⠀⠀⠈⢡⡴⠛⡽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡞⢻
#⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⣀⠀⠀⢀⡠⠃⡽
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠪⠭⠤⠐⠊⠁

#⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⢸⣿⣷⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠈⣿⣿⡆⠀⠀⠀⠀⣼⣿⣿⠀⣤⡀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡀⢹⣿⣧⠀⠀⠀⣸⣿⣿⠃⣰⣿⣿⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣇⠘⣿⣿⡄⠀⢀⣿⣿⡏⢠⣿⣿⡏⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡀⢻⣿⣧⠀⣸⣿⡟⢀⣾⣿⡿⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣇⣸⣿⣿⣶⣿⣿⠁⣼⣿⣿⠁⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠙⢿⣿⣿⣷⣦⣀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠛⠛⠛⠛⠛⠃⠀⠀⠀⠀
# 
# ⠀⠀⠀⠀⠀⠀⠀⢸⡒⠦⠤⠤⠄⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⢼⠀⠀⠒⠒⠤⠤⠤⠤⠤⣀⣀⣀⣀⠀⠀⠘⡇⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⢀⣀⠤⠔⠒⠉⠁⢀⣼⡀⠀⢠⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡧⠚⠉⢹⡀⠀⠀⠀⠀⠀⠀
#⠰⣖⠊⠉⠀⠀⠀⣠⠔⠚⠉⠁⢀⡇⠀⡀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⢀⡇⠀⣤⠀⢷⡀⠀⠀⠀⠀⠀
#⠀⠈⠳⡄⠀⠀⠋⣠⠖⠂⡠⠖⢙⡇⠀⠈⠉⠉⠉⠉⠓⠒⠒⠒⠒⠒⠆⠀⠀⣷⡀⠉⢦⠀⢳⡀⠀⠀⠀⠀
#⠀⠀⠀⠈⢦⠀⠀⠁⠀⠀⠀⢀⠼⡇⠀⠀⠦⠤⠤⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠱⡀⠀⠳⡀⠙⣆⠀⠀⠀
#⠀⠀⠀⠀⠀⠳⡄⠀⢀⡤⠊⠁⢠⡇⠀⠠⠤⢤⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⡧⡀⠙⢄⠀⠱⠄⠈⠳⡄⠀
#⠀⠀⠀⠀⠀⠀⠙⡄⠀⠀⡠⠔⢻⠀⠀⠀⠀⠀⠀⠠⣄⣀⣀⣁⣀⠀⠀⠀⠀⡇⠱⡀⠀⠀⠀⠀⠀⣀⣘⣦
#⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⡸⠀⠀⠰⣄⣀⡀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⡇⠀⠃⢀⣠⠴⠛⠉⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠙⠒⠀⠀⠀⠠⡇⣠⠔⠋⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⢸⠁⠀⠀⠀⠒⠲⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⢰⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠢⣄⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣎⣀⠀⠀⠀⠀⠀⠀⠀⠢⠤⣀⠀⠀⠁⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⠉⠙⠒⠤⢤⡀⠀⠀⠀⠀⠉⠒⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠶⠒⠊⠉⠉⠉⠓⠦⣀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠲⢄⡀⠀⠀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠲⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀   ⢠⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢕⠄⠀⠀
#⠀⠀⠀⠀⠀⠀⡠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠂⠀
#⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄
#⠀⠀⠀⠀⢠⣣⠀⠀⠀⠀⠀⠀⠀⢀⡠⣖⣂⣀⡀⠀⠀⠀⠀⠀⠀⠀⠸⢧
#⠀⢀⢾⠟⣯⡇⠀⠀⠀⠀⠀⠀⠀⠁⠈⣁⣀⠘⢷⣦⣄⡀⢀⢀⠀⣀⣀⣹
#⠀⢸⢸⠀⠈⠃⠀⠀⠀⠀⠀⠀⣰⣾⡻⣭⣭⣽⣿⣾⡽⣿⡟⣼⣾⣿⣿⡟
#⠀⠈⠹⣿⡏⠄⠀⠀⠀⠀⠀⠀⠁⠙⢜⠿⣿⣿⣿⣿⡧⠈⣸⣿⣿⣿⣿⡇
#⠀⠀⣇⠘⣃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⠿⠛⠋⠀⠀⢻⣿⣿⣿⡿⠀
#⠀⠀⠘⠤⠴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⠠⠂⠀⠀⢸⣿⣿⣿⡇⠀
#⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢿⡄⠀⠰⠄⠀⠀⠻⣿⣿⠇⠀
#⠀⠀⠀⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠈⣇⣤⡤⢄⠀⣴⣶⣿⠟⠀⠀
#⠀⠀⢀⠃⠀⠀⠀⠀⠀⠀⠀⠀⡔⠁⠀⡀⠀⠈⢹⣷⣿⣾⣿⣿⠏⠀⠀⠀
#⠀⡠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⢀⣠⣶⣦⣤⣤⣬⣿⣿⣿⣿⡟⠀⠀⠀⠀
#⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⣍⣛⣿⣿⣿⣿⡟⠠⣀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⢙⣿⣿⣿⣿⣷⣤⡀⠉⡢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀