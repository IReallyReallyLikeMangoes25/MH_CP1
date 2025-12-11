# MH 2nd final project

import random
play_or_quit = input("Do you want to play or quit?\n1. Play\n2. Quit")

current_room = 0

stats = {
    "player" : {
        "health" : 10,
        "attack" : 13,
        "special_attack" : 15,
        "defense" : 7,
        "special defense" : 6,
        "speed" : 10
    },
    "grunt" : {
        "health" : 10,
        "attack" : 7,
        "defense" : 13,
        "special defense" : 10,
        "speed" : 10,
        "magic" : 10
    },
    "Don" : {
        "health" : 13,
        "attack" : 7,
        "defense" : 7,
        "special defense" : 9,
        "speed" : 10,
        "magic" : 17
    }
}

inventory = {

}

player = True
Don = True
broken_wand = True
cursed_lasagne = True
thirty_dollars = True
generator = True
magical_cauldron = True
magical_artifact = True

def dons_office():
    pass

def front_room():
    print("description")
    choice = input("You see two doors at the back, seems they're the only ways forward. Which way should you go?\n1. Door one\n2. Door two")
    while True:
        if choice == "1":
            print("You walk up to the door and open it, hoping that red stain on the bottom is just marinara.")
            choice = "kitchen"
            break
        elif choice == "2":
            print("You approach the door and open it.")
            choice = "supplies room"
            break
        else:
            print("You can't see a door like that anywhere, choose from the ones you can see.")
            choice = input("You see two doors at the back, seems they're the only ways forward. Which way should you go?\n1. Door one\n2. Door two")
    return choice

def kitchen(lasagne):
    print("Looks like this is just the kitchen")
    if lasagne == True:
        take = input("On the counter is a lasagne, looks like it's been left out... You are pretty hungry... Eat it?\n1. Eat the lasagne\n2. Leave it alone")
        if take == 1:
            print("You eat the lasagne... It takes like cigarettes and has too many newts in it.")
            lasagne = False
            rand = random.randint(1,2)
            if rand == 1:
                print("Surprisingly though, it didn't kill you. You even feel slightly healthier than you did before.")
                stat_change = 5
            elif rand == 2:
                print("That was the worst decision of your life, why would you ever even consider eating that. You feel terrible, that thing was definitely cursed, it feels like your body is three times weaker than before.")
                stat_change = -5
    choice = input("There are three doors in this room. You should keep moving.\n1. Door one\n2. Door two\n3. Door three")
    while True:
        if choice == "1":
            print("You walk up to the door and go through.")
            choice = "front room"
            break
        elif choice == "2":
            print("You approach the door and go through.")
            choice = "generator room"
            break
        elif choice == "3":
            print("You approach the door and go through.")
            choice = "meeting room"
            break
        else:
            print("You can't see a door like that anywhere, choose from the ones you can see.")
            choice = input("You see three, seems they're the only paths to follow. Which way should you go?\n1. Door one\n2. Door two\n3. Door three")
    return choice, lasagne, stat_change


def supplies_room(artifact):
    print("Looks like this is the supplies room, it's got all kinds of wizard crap laying around. wands, rabbits feet, pixie dust, and are those live goblins? Is that ethical?")
    if artifact == True:
        knock_over = input("Far, far over in the corner you see a pedestal with something extra suspicious on top. You walk over.\nIt's... What looks like an articaft in the shape of margarita pizza. That's stupid, maybe you should knock it over.\n1. Knock it over\n2. Leave it be, it's not worth your time")
        if knock_over == 1:
            print("You knock it over... As far as you can tell nothing hapened. Whatever, it was really satisfying. Screw those magic idiots.")
            stat_change = -5
            artifact = False
        elif knock_over == 2:
            print("This isn't worth your time, let those magic freaks have their fun.")
    choice = input("There are three doors in this room. You should keep moving.\n1. Door one\n2. Door two\n3. Door three")
    while True:
        if choice == "1":
            print("You walk up to the door and go through.")
            choice = "front room"
            break
        elif choice == "2":
            print("You approach the door and go through.")
            choice = "vault"
            break
        elif choice == "3":
            print("You approach the door and go through.")
            choice = "meeting room"
            break
        else:
            print("You can't see a door like that anywhere, choose from the ones you can see.")
            choice = input("You see three, seems they're the only paths to follow. Which way should you go?\n1. Door one\n2. Door two\n3. Door three")
    return choice, artifact, stat_change

def incantation_room(cauldron):
    print("You step into a very dark, dingy room. It's got lots of weird magic stuff in it too. Goats head, unicorn horn, and a giant cauldron. Looks like there's a giant sigil on the ground as well, it's mostly normal except for the painting of a tomato in the middle... For safety's sake you should avoid stepping on that.")
    if cauldron == True:
        pour = input("There's also something in the cauldron... A bright red glowing liquid and a ladel. You smell it... It's tomato soup. Maybe... Just maybe...\n1. Pour the soup on the sigil\n2. That's a terrible idea don't do that!!!")
        if pour == "1":
            print("You grab the ladel and fill it with tomato soup, then you walk over and pour it on the middle of the sigil... For a minute nothing happens, but then the whole thing begins to glow, illuminating the room.")
            item = random.randint(1, 3)
            if item == 1:
                print("The ground opens from beneath you and a large singular ravioli flies out and into your hands. You eat it and despite the place it may have come from it tasted pretty good. Somehow you feel stronger too.")
                stat_change = 5
                cauldron = False
            elif item == 2:
                print("The ground opens from beneath you and a cup of gelato flies out and into your hands. You eat it and it tastes a little off. But you feel lighter than you did before.")
                stat_change = 5
                cauldron = False
            else:
                print("The ground opens from beneath you and the biggest peice of calamari you've seen in your life flies out and onto your feet. You eat it and it and it's amazing. You can feel yourself gaining the energy from that beheamoth.")
                stat_change = 5
                cauldron = False
        elif pour == "2":
            print("Yeah no, messing around with this stuff is always a bad idea.")
    while True:
        if choice == "1":
            print("You walk up to the door and go through.")
            choice = "generator room"
            break
        elif choice == "2":
            print("You approach the door and go through.")
            choice = "meeting room"
            break
        elif choice == "3":
            print("You approach the door and go through.")
            choice = "Dons office"
            break
        else:
            print("You can't see a door like that anywhere, choose from the ones you can see.")
            choice = input("You see three, seems they're the only paths to follow. Which way should you go?\n1. Door one\n2. Door two\n3. Door three")
    

def generator_room(the_generator):
    print("This room is blanketed with a fog of pixie dust, and the sound of hssing is all you can here, but in the back you can see a large generator.")
    if the_generator == True:
        off_on = input("Looks that that machine is how they get the energy to run this place, but you bet it's got some magical qualities to it as well. Maybe you should turn it off, give yourself the advantage.\n1. Turn off the generator\n2. Leave it on")
        if off_on == "1":
            print("You turn off the machine and the lights immediately go out, and you hear the screams of pixies from inside. Jeez these guys mean business. It's pitch black now, you're going to have to move slowly.")
            stat_change = -5
        elif off_on == "2":
            print("Nah, don't want this place to collapse while you're in it.")
    while True:
        if choice == "1":
            print("You walk up to the door and go through.")
            choice = "kitchen"
            break
        elif choice == "2":
            print("You approach the door and go through.")
            choice = "inantation room"
            break
        else:
            print("You can't see a door like that anywhere, choose from the ones you can see.")
            choice = input("You see three, seems they're the only paths to follow. Which way should you go?\n1. Door one\n2. Door two\n3. Door three")



def game_room(wand):
    print("Looks like these guys aren't complete monsters after all, they've got a pool table in here. Although, it is a bit off a mess. There a broken bottles and cigarettes everywhere.")
    if wand == True:
        take = input("On the pool table you also see a broken wand... It's against your morals but it could come in handy... Take it?\n1. Take the wand\n2. Leave it- it's broken anyway")
        if take == "1":
            pass
        elif take == "2":
            print("You leave the wand")
def vault():
    pass

def meting_room():
    pass

def battle():
    pass

def player_turn(player_attack, player_specialatk, enemy_defense, enemy_specialdef, player_inventory):
    action = input("What would you like to do?\n1. Attack\n2. Heal\n3. Special attack\n4. Use inventory item")
    auto_win = False
    while True:
        if action == 1:
            damage = (player_attack / 5) - (enemy_defense /5)
            return damage
        elif action == 2:
            healed = random.randint(0, 4)
            return healed
        elif action == 3:
            damage = (player_specialatk / 5) - (enemy_specialdef / 5)
        elif action == 4:
            print(player_inventory)
            use = input("what item would you like to use?")
            while True:
                if use == "broken wand":
                    rand = random.randint(1,2)
                    if rand == 1:
                        healed = 5
                        return healed
                    else:
                        healed = -4
                        return healed
                elif use == "30 dollars":
                    if enemy_defense == 13:
                        auto_win = True
                        return auto_win
                    else:
                        healed = -5
                        return healed
                else:
                    print("That is not in your inventoy, please choose again.")
                    use = input("what item would you like to use?")
        else:
            print("That is not an option right now, make anoter choice.")
            action = input("What would you like to do?\n1. Attack\n2. Heal\n3. Special attack\n4. Use inventory item")

def enemy_turn(player_attack, player_specialdef, player_defense, enemy_attack, enemy_defense, enemy_specialatk, magic):
    action = random.randint(1, 4)
    if action == 1:
        damage = (enemy_attack / 5) - (player_defense /5)
        return damage
    elif action == 2:
        healed = random.randint(1,4)
        return healed
    elif action == 3:
        damage = (magic / 5) - (player_specialdef /5)
        return damage
    else:
        damage = (enemy_specialatk / 5) - (player_specialdef /5)
        return damage
