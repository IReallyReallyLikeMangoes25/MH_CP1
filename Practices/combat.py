# MH 2nd combat practice
import time
import random

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
    atk = 50
    defense = 50
    spec_atk = 65
    spec_def = 65
    speed = 45

    rival = "Charmander"
    rhp = 40
    ratk = 50
    rdefense = 45
    rspec_atk = 60
    rspec_def = 50
    rspeed = 65

elif starter == 2:
    starter = "Squirtle"
    hp = 45
    atk = 50
    defense = 65
    spec_atk = 50
    spec_def = 65
    speed = 45

    rival = "Bulbasaur"
    rhp = 45
    ratk = 50
    rdefense = 50
    rspec_atk = 65
    rspec_def = 65
    rspeed = 45

else:
    starter = "Charmander"
    hp = 40
    atk = 50
    defense = 45
    spec_atk = 60
    spec_def = 50
    speed = 65

    rival = "Squirtle"
    rhp = 45
    ratk = 50
    rdefense = 65
    rspec_atk = 50
    rspec_def = 65
    rspeed = 45

def your_turn(action, starter, atk, rdefense, spec_atk, rspec_def):
    potions = 1
    damage = 0
    atk_debuff = 0
    def_debuff = 0
    boost = 0
    if starter == "Bulbasaur":
        if action == 1:
            print("Bulbasaur used Tackle!")
            damage += ((atk + 40) / 5) - (rdefense / 15)
            return damage
        elif action == 2:
            print("Bulbasaur used growl!")
            atk_debuff += 10
            return atk_debuff
        elif action == 3:
            print("Bulbasuar used vine Whip!")
            damage += ((atk + 45) / 5) - (rdefense / 5)
        else:
            if potions == 1:
                print("Used a potion. 0 left.")
                potions -= 1
                boost += 15
                return boost
            else:
                print("You are out of potions.")
    
    elif starter == "Squirtle":
        if action == 1:
            print("Squirtle used Tackle!")
            damage += ((atk + 40) / 5) - (rdefense / 15)
            return damage
        elif action == 2:
            print("Squirtle used Tail Whip!")
            def_debuff += 15
            return def_debuff
        elif action == 3:
            print("Squirtle used Water Gun!")
            damage += ((spec_atk + 40) / 5) - (rspec_def / 5)
        else:
            if potions == 1:
                print("Used a potion. 0 left.")
                potions -= 1
                boost += 15
                return boost
            else:
                print("You are out of potions.")
    
    else:
        if action == 1:
            print("Charmander used Tackle!")
            damage += ((atk + 40) / 5) - (rdefense / 15)
            return damage
        elif action == 2:
            print("Charmander used Growl!")
            atk_debuff += 15
            return atk_debuff
        elif action == 3:
            print("Charmander used Ember!")
            damage += ((spec_atk + 40) / 5) - (rdefense / 5)
        else:
            if potions == 1:
                print("Used a potion. 0 left.")
                potions -= 1
                boost += 15
                return boost
            else:
                print("You are out of potions.")


    
def rival_turn(action, starter, hp, atk, defense, spec_atk, spec_def, speed, rival, rhp, ratk, rdefense, rspec_atk, rspec_def, rspeed):
    potions = 1
    damage = 0
    atk_debuff = 0
    def_debuff = 0
    boost = 0
    if starter == "Bulbasaur":
        if action == 1:
            print("Rivals Bulbasaur used Tackle!")
            damage += ((atk + 40) / 5) - (rdefense / 15)
            return damage
        elif action == 2:
            print("Rivals Bulbasaur used Growl!")
            atk_debuff += 10
            return atk_debuff
        elif action == 3:
            print("Rivals Bulbasaur used Vine Whip!")
            damage += ((atk + 45) / 5) - (rdefense / 5)
        else:
    
    elif starter == "Squirtle":
        pass
    else:
        pass


def turns_1():
    while hp > 0 or rhp > 0 :
        if hp < 0:
            winner = "Rival"
        elif rhp < 0:
            winner = "You"
        else:
            pass

def turns_2():
    while hp > 0 or rhp > 0:
        if hp < 0:
            winner = "Rival"
        elif rhp < 0:
            winner = "You"
        else:
            pass


print(f"Great! I think {starter} is the perfect choice for you. It's stats are:\nHP = {hp}\nSpeed = {speed}\nAttack = {atk}\nDefense = {defense}\nSpecial attack = {spec_atk}\nSpecial defense = {spec_def}")

print(f"Go {starter}!")
print(f"Go {rival}!")


if speed > rspeed:
    print(f"{starter} goes first!")

else:
    print(f"{rival} goes first!")
    
    
    