# MH 2nd final project
# Inport the random number generator library
# INPUT play: ask user "Do you want to play or quit?"

# CURRENT ROOM: Front room (this will change)

# Player = True (alive)

# STATS:{
    # player{
        # health 
        # speed 
        # attack 
        # defense 
    #}
    # grunt{
        # health 
        # speed 
        # attack 
        # defense 
        # magic 
    #}
    # Don{
        # health - 10
        # speed - 
        # attack - 
        # defense - 
        # magic - 15
    #}}

# ITEMS/INVENTORY:
    # inventory: {begins empty}
    # broken wand: True (not in inventory)
    # cursed lasagne: True (not eaten)
    # 30 dollars: True (not in inventory)
    # Generator: True (power on)
    # cauldron: True (full)
    # artifact: True (safe)

# FUNCTIONS:
    # ROOM FUNCTIONS:
    # The Dons office:
        # In this room the battle function will be run on the Don and the Player
        # if the player wins print that they won and ask if they want to play again
        # If the player loses print that they lost and ask if they want to play again
        # If they want to play again return True, if they want to quit return False

    # Front room:
        # In this room the player has their choice of two doors
        # door 1 - leads to the kitchen
        # door 2 - leads to the supplies room
        # return their room choice

    # Incantation room:
        # In this room there's a grunt, run the battle function
        # in this room if the cauldron is still full ask the player if they would like to use it
        # if they do randomize to choose what they get - 
        # +5 attack/speed/defense
        # return cauldron as False (empty) and display door options
        # the player has 3 door options in this room
        # door 1 - Go back to the generator room
        # door 2 - Go to the meeting room
        # door 3 - Go to the Dons office
        # return their room choice

    # Generator room:
        # in this room if the player hasn't already turned off the generator they will be given the choice to turn it off
        # if they choose to turn it off give all enemies -3 speed and player -3 attack and return generator as False (turned off) and display door options
        # the player has two door options in this room
        # door 1 - Go back to the kitchen
        # door 2 - Go to the incantation room
        # return their room choice

    # Kitchen:
        # check if cursed lasagne has been eaten, if it has provide door options, if it hasn't ask player if they want to eat the lasagne
        # if the player eats the lasagne randomly choose between giving them a stat boost or debuff and return cured lasagne as False (eaten) and display door options
        # the player will be given three door choices in this room
        # door 1 - Go back to the front room
        # door 2 - Go to the generator room
        # door 3 - Go to the meeting room
        # return their room choice

    # Game room:
        # Check if the broken wand is already in the players inventory, if it is provide door options, if it's not ask the player if they would like to pick up the broken wand
        # If they want to pick it up return broken wand as False (in inventory) and display door options
        # The player will have 3 door options in this room:
        # door 1 - Go to the meeting room
        # door 2 - Go to the Dons office
        # door 3 - Go to the vault
        # return their room choice

    # The vault:
        # Check if the $30 is already in the players inventory, if it is provide door options, if it's not ask them if they would like to pick it up
        # if they pick it up return 30 dollars as False (in inventory) and display door options
        # in this room there are 2 door options
        # door 1 - Go to the supplies room
        # door 2 - Go to the game room
        # return their room choice

    # Meeting room:
        # there are two grunts in this room, run the battle function for both
        # the player has to defeat both to get the door options
        # the player has 4 door options in this room
        # door 1 - Go to the kitchen
        # door 2 - Go to the supplies room
        # door 3 - Go to the game room
        # door 4 - Go to the incantation room
        # return their room choice

    # Supplies room:
        # check if the artifact has already been knocked over, if it hasn't ask the player if they want to knock it over
        # If they say they do, -2 from all enemy attack stats, return artifact as False (knocked over) and display door options
        # in this room the player has the choice between 3 doors
        # door 1 - Go back to the front room
        # door 2 - Go to the vault
        # door 3 - Go to the meeting room
        # return their room choice

    # BATTLE FUNCTION:
        # if the player is faster
            # While the player and enemy are alive:
                # player turn (players + enemies stats/inventory)
                # enemy turn (players + enemies stats)
            # after someone has died return who won

        # if the enemy is faster:
            # While the player and enemy are alive:
                # enemy turn (players + enemies stats)
                # player turn (players + enemies stats/inventory)
        # after someone has died return who won

    # PLAYER TURN FUNCTION: Takes in players stats, enemies stats, and player inventory
        # ask user what they want to do from the options:
            # INPUT: "What would you like to do? 1. Attack, 2. Special Attack, 3. Heal, 4. Use inventory item"
            # if user says "attack":
                # damage dealt = (attack / 5) - (enemy defense / 5)
                # return damage dealt
            # if user says "special attack":
                # damage dealt = (special attack / 5) - (enemy special defense / 5)
                # return damage dealt
            # if user says "heal":
                # health recovered = random number from 1 - health stat
                # return health recovered
            # if user says "Use inventory item"
                # LOOP:
                    # for every item in inventory display:
                        # what number in the inventory this item is
                        # item name
                    # INPUT: "What item would you like to use?"
                    # if the item they want to use is the broken wand:
                        # randomize a number from 1- 10
                        # if the number is 5 or higher add 5 points to the players health
                        # if the number is 4 or lower take five from the players health
                        # reutrn health
                    # if the item is the 30 dollars:
                        # check to see if the enemy is a grunt
                        # if the enemy is a grunt return that the user won
                        # if the enemy is the Don take 5 health from the user and return health



    # ENEMY TURN FUNCTION: Takes in players stats and enemies stats
        # generate a random number from 1-4
        # if the number is 1:
            # the enemy does a regular attack:
                # damage to player = (enemy attack / 5) - (player defense / 5)
                # return damage
        # in the number is 2:
            # the enemy does a special attack:
                # damage to player = (enemy special attack / 5) - (player special defense / 5)
                # return damage
        # if the number is 3:
            # the enemy heals a random number from 1 - enemy health stat
            # return health
        # if the number is 4:
            # the enemy uses a magic attack:
                # damage = (enemy magic / 5) - (player defense / 5)
                # reutrn damage

# GAME:
    # while user wants to play the game:
        # begin user in the front room, run the Front room function
        # update current room to whatever they chose in that function
        # while the user is alive:


    