# MH 2nd combat practice
import time

name = ("Hello young trainer! What is your name?\n")
starter = str(input(f"Hello {name}, nice to meet you. I am Professor Oak, please choose a starter pokemon:\n1. Bulbasaur\n2. Squirtle\n3. Charmander\n"))
rival = ""

hp = 0
atk = 0
defense = 0
spec_atk = 0
spec_def = 0
speed = 0


rhp = 0
ratk = 0
rdefense = 0
rspec_atk = 0
rspec_def = 0
rspeed = 0

if starter == 1:
    starter = "Bulbasaur"
    hp = 45
    atk = 49
    defense = 49
    spec_atk = 65
    spec_def = 65
    speed = 45

    rival = "Charmander"
    rhp = 39
    ratk = 52
    rdefense = 43
    rspec_atk = 60
    rspec_def = 50
    rspeed = 65

elif starter == 2:
    starter = "Squirtle"
    hp = 44
    atk = 48
    defense = 65
    spec_atk = 50
    spec_def = 64
    speed = 43

    rival = "Bulbasaur"
    rhp = 45
    ratk = 49
    rdefense = 49
    rspec_atk = 65
    rspec_def = 65
    rspeed = 45

else:
    starter = "Charmander"
    hp = 39
    atk = 52
    defense = 43
    spec_atk = 60
    spec_def = 50
    speed = 65

    rival = "Squirtle"
    rhp = 44
    ratk = 48
    rdefense = 65
    rspec_atk = 50
    rspec_def = 64
    rspeed = 43

def your_turn(starter, hp, atk, defense, spec_atk, spec_def, speed, rival, rhp, ratk, rdefense, rspec_atk, rspec_def, rspeed):
    potions = 1
    damage = 0
    if starter = "Bulbasaur"
        action = print(int(input(f"What should Bulbasaur do?\n1. Tackle\n2. Growl\n3. Vine Whip\n4. Potion (1 left)")))
        if action == 1:
            print("Bulbasaur used Vine whip!")
            damage += 
        elif action == 2:
            pass
        elif action == 3:
            pass
        else:
            pass
    
def rival_turn(rhp, ratk, rdefense, rspec_atk, rspec_def, rspeed):
    pass

def turns_1():
    while hp > 0 or rhp > 0 :
    if hp < 0:
        winner = "Rival"
    elif rhp < 0:
        winner = "You"
    else:


def turns_2():
    while hp > 0 or rhp > 0:
    if hp < 0:
        winner = "Rival"
    elif rhp < 0:
        winner = "You"
    else:



print(f"Great! I think {starter} is the perfect choice for you. It's stats are:\nHP = {hp}\nSpeed = {speed}\nAttack = {atk}\nDefense = {defense}\nSpecial attack = {spec_atk}\nSpecial defense = {spec_def}")

print(f"Go {starter}!")
print(f"Go {rival}!")


if speed > rspeed:
    print(f"{starter} goes first!")
    first = "player"
else:
    print(f"{rival} goes first!")
    first = "rival"
    
    
    