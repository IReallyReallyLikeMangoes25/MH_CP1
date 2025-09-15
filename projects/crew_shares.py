# MH 2nd crew shares project

money = float(input("How much money did the pirates earn:\n"))
crew = int(input("How many members are in the crew (Not including the captain and first mate):\n"))
captain = 7
first_mate = 3

# Divides money among captain, first mate, and crew

total_shares = crew + captain + first_mate
share_amount = money/total_shares
captain_share = share_amount * 7
fm_share = share_amount * 3
cfm_share = captain_share + fm_share
crew_shares = share_amount - 500

cps_round = round(captain_share, 2)
fms_round = round(fm_share, 2)
cs_round = round(crew_shares, 2)
print(f"The captain gets: ${cps_round} \n The first mate gets: ${fms_round} \n The crew gets: ${cs_round}")