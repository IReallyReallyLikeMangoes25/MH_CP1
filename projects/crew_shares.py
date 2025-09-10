# MH 2nd crew shares project

money = float(input("How much money did the pirates earn:\n"))
crew = int(input("How many members are in the crew (Not including the captain and first mate):\n"))
captain = 7
first_mate = 3

money = money - crew * 500
shares = crew + captain + first_mate
share_amount = money/shares
captain_share = share_amount * 7
fm_share = share_amount * 3
c_fm_share = captain_share - fm_share
share_amount = share