# MH 2nd final project
import time
import random
play_or_quit = input("Do you want to play or quit?\n1. Play\n2. Quit\n")

current_room = 0

stats = {
    "player" : {
        "health" : 10,
        "attack" : 13,
        "special attack" : 15,
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

two_grunts = True
broken_wand = True
cursed_lasagne = True
thirty_dollars = True
generator = True
magical_cauldron = True
magical_artifact = True

def dons_office():
    press = input("...This room is pitch black... It's quiet, too quiet. You begin to look around and crash into what feels like a large steel block. On top you can feel a button, will you press it?\n1. Press it\n2. No way Hose\n")
    if press == "1":
        print("You press the button and immediately you feel the ground shifting, and the steel block lowers into the ground. From the hole it left a bright light begins to shine and you can see the fog blanketing the ground, and EDM music blares from speakers placed around the room. Then the floor opens up with a loud mechanical whir, and out from it rises a platform with noneother stadning on it than the Don. Once he rises fully there's a moment of awkward silence...")
        time.sleep(25)
        print("Aren't you a wizard???? Why did you built this whole setup if you could've just used magic?")
        time.sleep(4)
        print("Hey! This is MY boss fight! Stop chaning the subject! NOW-")
        time.sleep(3)
        print("But dude, you built this WHOLE wizard mafia, and instead of just making your life easy with magic you used probably like, thousands of dollars on something this stupid and cheesy?")
        time.sleep(5)
        print("Stop interupting me! As I was saying-")
        time.sleep(2)
        print("Like, seriously, for such a feared guy you'd think-")
        time.sleep(2)
        print("I like EDM ok!? Jeez. NOW AS I WAS SAYING- Detective player... I have been waiting for you... And.. Uh... Dang it my notecards are out of order! Whatever! This ends today detective!")
        winner = battle(stats["player"]["speed"], stats["player"]["health"], stats["Don"]["speed"], stats["Don"]["health"])
        if winner == "player":
            print("...Finally. It's over.")
            grunts = False
        else:
            print("So this is how it ends?")
            game_over = True
            return game_over
    else:
        pass

def front_room():
    print("description")
    choice = input("You see two doors at the back, seems they're the only ways forward. Which way should you go?\n1. Door one\n2. Door two\n")
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
    stat_change = 0
    print("Looks like this is just the kitchen")
    if lasagne == True:
        take = input("On the counter is a lasagne, looks like it's been left out... You are pretty hungry... Eat it?\n1. Eat the lasagne\n2. Leave it alone\n")
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
    choice = input("There are three doors in this room. You should keep moving.\n1. Door one\n2. Door two\n3. Door three\n")
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
    stat_change = 0
    print("Looks like this is the supplies room, it's got all kinds of wizard crap laying around. wands, rabbits feet, pixie dust, and are those live goblins? Is that ethical?")
    if artifact == True:
        knock_over = input("Far, far over in the corner you see a pedestal with something extra suspicious on top. You walk over.\nIt's... What looks like an articaft in the shape of margarita pizza. That's stupid, maybe you should knock it over.\n1. Knock it over\n2. Leave it be, it's not worth your time\n")
        if knock_over == 1:
            print("You knock it over... As far as you can tell nothing hapened. Whatever, it was really satisfying. Screw those magic idiots.")
            stat_change = -5
            artifact = False
        elif knock_over == 2:
            print("This isn't worth your time, let those magic freaks have their fun.")
    choice = input("There are three doors in this room. You should keep moving.\n1. Door one\n2. Door two\n3. Door three\n")
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
    stat_change = 0
    print("You step into a very dark, dingy room. It's got lots of weird magic stuff in it too. Goats head, unicorn horn, and a giant cauldron. Looks like there's a giant sigil on the ground as well, it's mostly normal except for the painting of a tomato in the middle... For safety's sake you should avoid stepping on that.")
    if cauldron == True:
        pour = input("There's also something in the cauldron... A bright red glowing liquid and a ladel. You smell it... It's tomato soup. Maybe... Just maybe...\n1. Pour the soup on the sigil\n2. That's a terrible idea don't do that!!!\n")
        if pour == "1":
            print("You grab the ladel and fill it with tomato soup, then you walk over and pour it on the middle of the sigil... For a minute nothing happens, but then the whole thing begins to glow, illuminating the room.")
            item = random.randint(1, 3)
            if item == 1:
                print("The ground opens from beneath you and a large singular ravioli flies out and into your hands. You eat it and despite the place it may have come from it tasted pretty good. Somehow you feel stronger too.")
                source = "attack"
                stat_change = 5
                cauldron = False
            elif item == 2:
                print("The ground opens from beneath you and a cup of gelato flies out and into your hands. You eat it and it tastes a little off. But you feel lighter than you did before.")
                source = "speed"
                stat_change = 5
                cauldron = False
            else:
                print("The ground opens from beneath you and the biggest peice of calamari you've seen in your life flies out and onto your feet. You eat it and it and it's amazing. You can feel yourself gaining the energy from that beheamoth.")
                source = "health"
                stat_change = 5
                cauldron = False
        elif pour == "2":
            print("Yeah no, messing around with this stuff is always a bad idea.")
    choice = input("There are three doors in this room. You should keep moving.\n1. Door one\n2. Door two\n3. Door three\n")
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
    return choice, cauldron, stat_change, source

def generator_room(the_generator):
    stat_change = 0
    print("This room is blanketed with a fog of pixie dust, and the sound of hssing is all you can here, but in the back you can see a large generator.")
    if the_generator == True:
        off_on = input("Looks that that machine is how they get the energy to run this place, but you bet it's got some magical qualities to it as well. Maybe you should turn it off, give yourself the advantage.\n1. Turn off the generator\n2. Leave it on")
        if off_on == "1":
            print("You turn off the machine and the lights immediately go out, and you hear the screams of pixies from inside. Jeez these guys mean business. It's pitch black now, you're going to have to move slowly.")
            stat_change = -5
            the_generator = False
        elif off_on == "2":
            print("Nah, don't want this place to collapse while you're in it.")
    choice = input("There are two doors in this room. You should keep moving.\n1. Door one\n2. Door two")
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
            choice = input("You see three, seems they're the only paths to follow. Which way should you go?\n1. Door one\n2. Door two")

    return choice, the_generator, stat_change


def game_room(wand):
    print("Looks like these guys aren't complete monsters after all, they've got a pool table in here. Although, it is a bit off a mess. There a broken bottles and cigarettes everywhere.")
    if wand == True:
        take = input("On the pool table you also see a broken wand... It's against your morals but it could come in handy... Take it?\n1. Take the wand\n2. Leave it- it's broken anyway")
        if take == "1":
            print("You grab the wand, it feels wrong to even hold this in your hand, but it's in the name of justice.")
            take = True
        elif take == "2":
            print("You leave the wand, it's not worth sacraficing your principles.")
            take = False
    choice = input("There are three doors in this room. You should keep moving.\n1. Door one\n2. Door two\n3. Door three")
    while True:
        if choice == "1":
            print("You walk up to the door and go through.")
            choice = "meeting room"
            break
        elif choice == "2":
            print("You approach the door and go through.")
            choice = "Dons office"
            break
        elif choice == "3":
            print("You approach the door and go through.")
            choice = "vault"
            break
        else:
            print("You can't see a door like that anywhere, choose from the ones you can see.")
            choice = input("You see three, seems they're the only paths to follow. Which way should you go?\n1. Door one\n2. Door two")
    return choice, take

def vault(cash):
    print("There is so much money in this room... So. Much. Money. Literally how did they get all this... Definitely not legally.")
    if cash == True:
        take = input("Though, some money might come in handy while in here. Who knows what those wizard lackeys would do for some of this cash their boss is hoarding...\n1. Take the cash\n2. You're better than that, who knows how many people they hurt to get that money.")
        if take == 1:
            print("You're not better than this, you take $30 dollars.")
            take = True
        elif take == 2:
            print("No! You have honour! Remember the detectives code! You leave the cash but you retain your dignity.")
            take = False
    choice = input("There are two doors in this room. You should keep moving.\n1. Door one\n2. Door two")
    while True:
        if choice == "1":
            print("You walk up to the door and go through.")
            choice = "supplies room"
            break
        elif choice == "2":
            print("You approach the door and go through.")
            choice = "game room"
            break
        else:
            print("You can't see a door like that anywhere, choose from the ones you can see.")
            choice = input("You see three, seems they're the only paths to follow. Which way should you go?\n1. Door one\n2. Door two")
    return choice, take

def meeting_room(grunts):
    print("Wow, this room is surprisingly normal. There's a normal people table, normal people chairs, and even a water cooler.")
    if grunts == True:
        print("The only thing not super normal is the two guys is giant sparkly robes. Oh wait those are wizards-")
        winner = battle(stats["player"]["speed"], stats["player"]["health"], stats["grunt"]["speed"], stats["grunt"]["health"])
        if winner == "player":
            print("Awesome! Wizard scum down!")
            grunts = False
        else:
            print("So this is how it ends?")
            grunts = True
            return grunts
        print("Just one left!")
        winner = battle(stats["player"]["speed"], stats["player"]["health"], stats["grunt"]["speed"], stats["grunt"]["health"])
        if winner == "player":
            print("Awesome! Wizard scum down!")
        else:
            print("So this is how it ends?")
            grunts = True
            return grunts
    choice = input("There are four doors in this room. You should keep moving.\n1. Door one\n2. Door two\n3. Door three\n4. Door four")
    while True:
        if choice == "1":
            print("You walk up to the door and go through.")
            choice = "kitchen"
            break
        elif choice == "2":
            print("You approach the door and go through.")
            choice = "supplies room"
            break
        elif choice == "3":
            print("You approach the door and go through.")
            choice = "game room"
            break
        elif choice == "4":
            print("You approach the door and go through.")
            choice = "incantation room"
            break
        else:
            print("You can't see a door like that anywhere, choose from the ones you can see.")
            choice = input("You see three, seems they're the only paths to follow. Which way should you go?\n1. Door one\n2. Door two")

    return choice, grunts
    

def battle(player_speed, player_health, enemy_speed, enemy_health):
    winner = ""
    if player_speed > enemy_speed:
            while True:
                condition, source = player_turn(stats["player"]["attack"], stats["player"]["special attack"], stats["Don"]["defense"], stats["Don"]["special_defense"], inventory)
                if source == "damage":
                    enemy_health -= condition
                elif source == "heal":
                    player_health += condition
                elif source == "heal from wand":
                    player_health += condition
                elif source == "win from cash":
                    winner = "player"
                    return winner
                elif source == "heal from cash":
                    player_health += condition
                
                if enemy_health or player_health < 0:
                    if enemy_health < 0:
                        winner = "player"
                        return winner
                    elif player_health < 0:
                        winner = "enemy"
                        return winner

                condition, source = enemy_turn(stats["player"]["special defense"], stats["player"]["defense"], stats["Don"]["attack"], stats["Don"]["special attack"], stats["Don"]["magic"])
                if source == "damage":
                    player_health -= condition
                elif source == "heal":
                    enemy_health += condition

                if enemy_health or player_health < 0:
                    if enemy_health < 0:
                        winner = "player"
                        return winner
                    elif player_health < 0:
                        winner = "enemy"
                        return winner
    else:
            while True:
                condition, source = enemy_turn(stats["player"]["special defense"], stats["player"]["defense"], stats["Don"]["attack"], stats["Don"]["magic"])
                if source == "damage":
                    player_health -= condition
                elif source == "heal":
                    enemy_health += condition
                
                if enemy_health or player_health < 0:
                    if enemy_health < 0:
                        winner = "player"
                        return winner
                    elif player_health < 0:
                        winner = "enemy"
                        return winner

                condition, source = player_turn(stats["player"]["attack"], stats["player"]["special attack"], stats["Don"]["defense"], stats["Don"]["special_defense"], inventory)
                if source == "damage":
                    enemy_health -= condition
                elif source == "heal":
                    player_health += condition
                elif source == "heal from wand":
                    player_health += condition
                elif source == "win from cash":
                    winner = "player"
                    return winner
                elif source == "heal from cash":
                    player_health += condition
                
                if enemy_health or player_health < 0:
                    if enemy_health < 0:
                        winner = "player"
                        return winner
                    elif player_health < 0:
                        winner = "enemy"
                        return winner
    
                        winner = "enemy"
                        return winner

def player_turn(player_attack, player_specialatk, enemy_defense, enemy_specialdef, player_inventory):
    action = input("What would you like to do?\n1. Attack\n2. Heal\n3. Special attack\n4. Use inventory item")
    auto_win = False
    source = ""
    while True:
        if action == 1:
            damage = (player_attack / 5) - (enemy_defense /5) + random.randint(4-7)
            print(f"You do {damage} damage")
            source = "damage"
            return damage, source
        elif action == 2:
            healed = random.randint(0, 4) + random.randint(4-7)
            print("You heal {healed} HP")
            source = "heal"
            return healed, source
        elif action == 3:
            damage = (player_specialatk / 5) - (enemy_specialdef / 5) + random.randint(4-7)
            print(f"You do {damage} damage")
            source = "damage"
            return damage, source
        elif action == 4:
            print(player_inventory)
            use = input("what item would you like to use?")
            while True:
                if use == "broken wand":
                    rand = random.randint(1,2)
                    if rand == 1:
                        healed = 5
                        source = "heal from wand"
                        print("The wands magic surrounds you and heals some of the more minor wounds. + 5 HP")
                        return healed, source
                    else:
                        healed = -5
                        source = "heal from wand"
                        print("The wands magic surrounds you and oh god it hurts. That was a mistake. - 5 HP")
                        return healed, source
                elif use == "30 dollars":
                    if enemy_defense == 13:
                        auto_win = True
                        source = "win from cash"
                        print("You give the wizard the $30 and he just leaves. What a sell out.")
                        return auto_win, source
                    else:
                        print("Hey, I'm not that cheap!\n While you tried to bribe him he took the opportinity to clean your clock. -5 HP")
                        healed = -5
                        source = "heal from cash"
                        return healed, source
                else:
                    print("That is not in your inventoy, please choose again.")
                    use = input("what item would you like to use?")
        else:
            print("That is not an option right now, make anoter choice.")
            action = input("What would you like to do?\n1. Attack\n2. Heal\n3. Special attack\n4. Use inventory item")

def enemy_turn(player_specialdef, player_defense, enemy_attack, enemy_defense, enemy_specialatk, magic):
    source = ""
    action = random.randint(1, 4)
    if action == 1:
        damage = (enemy_attack / 5) - (player_defense /5) + random.randint(4-7)
        print(f"The wizard attacks and you take {damage} damage")
        source = "damage"
        return damage, source
    elif action == 2:
        healed = random.randint(1,4) + random.randint(4-7)
        print(f"The wizard casts some baloney spell and gains +{healed} health. Friggin cheap.")
        source = "heal"
        return healed, source
    elif action == 3:
        damage = (magic / 5) - (player_specialdef /5) + random.randint(4-7)
        print(f"The wizard attacks and you take {damage} damage")
        source = "damage"
        return damage, source
    else:
        damage = (enemy_specialatk / 5) - (player_specialdef /5) + random.randint(4-7)
        print(f"The wizard casts a speel on you and you take {damage} damage")
        source = "damage"
        return damage, source

while True:
    next_room = front_room()
    while stats["player"]["health"] > 0:
        if next_room == "front room":
            next_room = front_room()
            continue
        elif next_room == "kitchen":
            next_room, lasagne, stat_change = kitchen(cursed_lasagne)
            stats["player"]["health"] += stat_change
            cursed_lasagne = lasagne
            continue
        elif next_room == "supplies room":
            next_room, artifact, stat_change = supplies_room(magical_artifact)
            stats["Don"]["magic"] += stat_change
            stats["grunt"]["health"] += stat_change
            magical_artifact = artifact
            continue
        elif next_room == "incantation room":
            next_room, cauldron, stat_change, source = incantation_room(magical_cauldron)
            if source == "attack":
                stats["player"]["attack"] += stat_change
            elif source == "speed":
                stats["player"]["speed"] += stat_change
            else:
                stats["player"]["health"] += stat_change
            magical_cauldron = cauldron
            continue
        elif next_room == "game room":
            next_room, wand = game_room(broken_wand)
            broken_wand = wand
            if wand == "True":
                inventory["Broken Wand"] = True
            continue
        elif next_room == "meeting room":
            next_room, two_grunts = meeting_room(two_grunts)
            continue
        elif next_room == "generator room":
            next_room, the_generator, stat_change = generator_room(generator)
            stats["Don"]["magic"] += stat_change
            stats["grunt"]["magic"] += stat_change
            stats["player"]["speed"] += stat_change
            generator = the_generator
            continue
        elif next_room == "vault":
            next_room, cash = vault(thirty_dollars)
            thirty_dollars = cash
            if cash == True:
                inventory["30 bucks"] = True
            continue
        else:
            dons_office()
            break
    play_or_quit = input("Would you like to play again?\n1. Yes\n2. No")
    if play_or_quit == "1":
        two_grunts = True
        broken_wand = True
        cursed_lasagne = True
        thirty_dollars = True
        generator = True
        magical_cauldron = True
        magical_artifact = True
        continue
    if play_or_quit == "2":
        break

print("Thanks for playing my good fellow.")