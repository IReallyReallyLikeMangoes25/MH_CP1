# Mh 2nd Rock paper scissors practice

import random
import time

rock = 1
paper = 2
scissors = 3
lizard = 4
spock = 5

while True:
    play_quit = input("Would you like to 1. Play. or 2. Quit?\n")
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