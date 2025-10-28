# MH 2nd combat practice
import time
import random

name = ("Hello young trainer! What is your name?\n")
starter = int(input(f"Hello {name}, nice to meet you. I am Professor Oak, please choose a starter pokemon:\n1. Bulbasaur\n2. Squirtle\n3. Charmander\n"))
rival = ""
potions = 1
rpotions = 1

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

while True:
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
        
        break
    
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
    
        break
    
    elif starter == 3:
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
    
        break
    
    else:
        print("Invalid input, try again.")
        starter = int(input(f"Hello {name}, nice to meet you. I am Professor Oak, please choose a starter pokemon:\n1. Bulbasaur\n2. Squirtle\n3. Charmander\n"))
        

def your_turn(starter, atk, rdefense, spec_atk, rspec_def, potions):
    damage = 0
    atk_debuff = 0
    def_debuff = 0
    boost = 0
    if starter == "Bulbasaur":
            action = int(input(f"What should Bulbasaur do?\n1.Tackle\n2. Growl\n3. Vine Whip\n4. Potion ({potions} left)\n"))
            while True:
                if action == 1:
                    print("Bulbasaur used Tackle!")
                    damage += ((atk + 40) / 5) - (rdefense / 15)
                    return damage, "damage"
                    break
                elif action == 2:
                    print("Bulbasaur used growl!")
                    atk_debuff += 10
                    return atk_debuff, "atk_debuff"
                    break
                elif action == 3:
                    print("Bulbasuar used vine Whip!")
                    damage += ((atk + 45) / 5) - (rdefense / 5)
                    return damage, "damage"
                    break
                else:
                    if potions == 1:
                        print("Used a potion. 0 left.")
                        potions -= 1
                        boost += 15
                        return boost, "boost"
                        break
                    else:
                        print("You are out of potions.")
                        action = int(input("Please choose another action:\n"))
        
    elif starter == "Squirtle":
            action = int(input(f"What should Squirtle do?\n1.Tackle\n2. Tail Whip\n3. Water Gun\n4. Potion ({potions} left)\n"))
            while True:
                if action == 1:
                    print("Squirtle used Tackle!")
                    damage += ((atk + 40) / 5) - (rdefense / 15)
                    return damage, "damage"
                    break
                elif action == 2:
                    print("Squirtle used Tail Whip!")
                    def_debuff += 15
                    return def_debuff, "def_debuff"
                    break
                elif action == 3:
                    print("Squirtle used Water Gun!")
                    damage += ((spec_atk + 40) / 5) - (rspec_def / 5)
                    return damage, "damage"
                    break
                else:
                    if potions == 1:
                        print("Used a potion. 0 left.")
                        potions -= 1
                        boost += 15
                        return boost, "boost"
                        break
                    else:
                        print("You are out of potions.")
                        action = int(input("Please choose another action:\n"))
                
    else:
        action = int(input(f"What should Charmander do?\n1.Tackle\n2. Growl\n3. Ember\n4. Potion ({potions} left)\n"))
        while True:
            if action == 1:
                print("Charmander used Tackle!")
                damage += ((atk + 40) / 5) - (rdefense / 15)
                return damage, "damage"
                break
            elif action == 2:
                print("Charmander used Growl!")
                atk_debuff += 15
                return atk_debuff, "atk_debuff"
                break
            elif action == 3:
                print("Charmander used Ember!")
                damage += ((spec_atk + 40) / 5) - (rdefense / 5)
                return damage, "damage"
                break
            else:
                if potions == 1:
                    print("Used a potion. 0 left.")
                    potions -= 1
                    boost += 15
                    return boost, "boost"
                    break
                else:
                    print("You are out of potions.")
                    action = int(input("Please choose another action:\n"))


    
def rival_turn(rpotions, defense, spec_def, rival, ratk, rdefense, rspec_atk):
    action = random.randint(1, 4)
    damage = 0
    atk_debuff = 0
    def_debuff = 0
    boost = 0
    if rival == "Bulbasaur":
        while True:
            if action == 1:
                print("Rivals Bulbasaur used Tackle!")
                damage += ((ratk + 40) / 5) - (defense / 15)
                return damage, "damage"
                break
            elif action == 2:
                print("Rivals Bulbasaur used Growl!")
                atk_debuff += 10
                return atk_debuff, "atk_debuff"
                break
            elif action == 3:
                print("Rivals Bulbasaur used Vine Whip!")
                damage += ((ratk + 45) / 5) - (defense / 5)
                return damage, "damage"
                break
            else:
                if potions == 1:
                    print("Rival used a potion. 0 left.")
                    rpotions -= 1
                    boost += 15
                    return boost, "boost"
                    break
                else:
                    action = random.randint(1, 4)
    
    elif rival == "Squirtle":
        while True:
            if action == 1:
                print("Rival Squirtle used Tackle!")
                damage += ((ratk + 40) / 5) - (defense / 15)
                return damage, "damage"
                break
            elif action == 2:
                print("Rival Squirtle used Tail Whip!")
                def_debuff += 15
                return def_debuff, "def_debuff"
                break
            elif action == 3:
                print("Rival Squirtle used Water Gun!")
                damage += ((rspec_atk + 40) / 5) - (spec_def / 5)
                break
            else:
                if potions == 1:
                    print("Rival used a potion. 0 left.")
                    rpotions -= 1
                    boost += 15
                    return boost, "boost"
                    break
                else:
                    action = random.randint(1, 4)
                    
    else:
        while True:
            if action == 1:
                print("Rival Charmander used Tackle!")
                damage += ((ratk + 40) / 5) - (defense / 15)
                return damage, "damage"
                break
            elif action == 2:
                print("Rival Charmander used Growl!")
                atk_debuff += 15
                return atk_debuff, "atk_debuff"
            elif action == 3:
                print("Rival Charmander used Ember!")
                damage += ((rspec_atk + 40) / 5) - (defense / 5)
                return damage, "damage"
                break
            else:
                if potions == 1:
                    print("Rival used a potion. 0 left.")
                    rpotions -= 1
                    boost += 15
                    return boost, "boost"
                    break
                else:
                    action = random.randint(1, 4)


print(f"Great! I think {starter} is the perfect choice for you. It's stats are:\nHP = {hp}\nSpeed = {speed}\nAttack = {atk}\nDefense = {defense}\nSpecial attack = {spec_atk}\nSpecial defense = {spec_def}")

print(f"Now, in order to begin your Pokemon journey, you must complete your first battle! This young man right here will be your opponent! He has chosen {rival} as his starter Pokemon!")
print(f"Go {starter}!")
print(f"Go {rival}!")


if speed > rspeed:
    print(f"{starter} goes first!")
    while True:
        condition, source = your_turn(starter, atk, rdefense, spec_atk, rspec_def, potions)
        if source == "damage":
            rhp -= condition
            print(f"{rival} takes {condition} damage!\n{rival}'s HP = {rhp}")
        elif source == "atk_debuff":
            ratk -= condition
            print(f"{rival}'s attack has been lowered by one stage!")
        elif source == "def_debuff":
            rdefense -= condition
            print(f"{rival}'s defense has been lowered by one stage!")
        else:
            potions = 0
            if (hp + condition) > hp:
                print(f"{starter} is now at full HP!")
                hp = hp
            else:
                print(f"{starter} has been healed by 15 points!\nHP is now {hp}")
                hp += condition
        if rhp < 0:
            print("You win, congrats!")
            break
            
        condition, source = rival_turn(rpotions, defense, spec_def, rival, ratk, rdefense, rspec_atk)
        if source == "damage":
            hp -= condition
            print(f"{starter} takes {condition} damage!\n{starter}'s HP = {hp}")
        elif source == "atk_debuff":
            atk -= condition
            print(f"{starter}'s attack has been lowered one stage!")
        elif source == "def_debuff":
            defense -= condition
            print(f"{starter}'s defense has been lowered by one stage!")
        else:
            rpotions = 0
            if (hp + condition) > hp:
                print(f"{rival} is now at full HP!")
                rhp = rhp
            else:
                print(f"{rival} has been healed by 15 points!\nHP is now {rhp}")
                rhp += condition
                
        if hp < 0:
            print("Your rival wins this time!")
            break
    

else:
    print(f"{rival} goes first!")
    while True:
        condition, source = rival_turn(rpotions, defense, spec_def, rival, ratk, rdefense, rspec_atk)
        if source == "damage":
            hp -= condition
            print(f"{starter}'s HP = {hp}")
        elif source == "atk_debuff":
            atk -= condition
            print(f"{starter}'s attack has been lowered one stage!")
        elif source == "def_debuff":
            defense -= condition
            print(f"{starter}'s defense has been lowered by one stage!")
        else:
            rpotions = 0
            if (hp + condition) > hp:
                print(f"{rival} is now at full HP!")
                rhp = rhp
            else:
                print(f"{rival} has been healed by 15 points!\nHP is now {rhp}")
                rhp += condition
        if hp <= 0:
            print("Good shot! But your rival wins this time!")
            break
                
        condition, source = your_turn(starter, atk, rdefense, spec_atk, rspec_def, potions)
        if source == "damage":
            rhp -= condition
            print(f"{rival}'s HP = {rhp}")
        elif source == "atk_debuff":
            ratk -= condition
            print(f"{rival}'s attack has been lowered by one stage!")
        elif source == "def_debuff":
            rdefense -= condition
            print(f"{rival}'s defense has been lowered by one stage!")
        else:
            potions = 0
            if (hp + condition) > hp:
                print(f"{starter} is now at full HP!")
                hp = hp
            else:
                print(f"{starter} has been healed by 15 points!\nHP is now {hp}")
                hp += condition
        if rhp <= 0:
            print("You win, congrats!")
            break
    
    
    
    