# MH 2nd Conditionals notes

import random
monster_hp = 30
dmg_mod = 2
atk_bonus = 3
roll = random.randint(1, 20)
player_hp = 25

if roll == 20:
    print(f"You rolled a crit! Double your damage! {roll}")
    attack = random.randint(1, 8) + random.randint(1, 8) + dmg_mod
    monster_hp -= attack
    print(f"You did {attack} damage to the monster!")
elif roll + atk_bonus > 10:
    attack = random.randint(1, 8) + dmg_mod
    monster_hp -= attack
    print(f"You did {attack} damage to the monster!")
elif roll <= 10:
    if roll == 1:
        print(f"You rolled a critical failure! The moster gets a free attack!")
        damage = random.randint(1, 10) + 2
        player_hp -= damage
        print(f"You took {damage} damage, health remaining: {player_hp}")
else:
    print(f"you missed! {roll}")

print("Your turn is over.")

if monster_hp and monster_hp > 0:
    print("It is the monsters turn.")
else:
    print('The monster is dead!')