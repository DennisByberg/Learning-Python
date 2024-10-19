# Challenge: You are tasked with determining whether a player is eligible to participate in a football league
# based on a few conditions.

# The player must be at least 18 years old but not older than 35.
# The player must have played more than 10 matches or scored at least 5 goals.
# The player must not be currently injured.
# Instructions:

# Write a program that takes the player's
# age, number of matches played, number of goals scored, and whether they are injured (a boolean True or False).
# Use and, or, and not operators to determine if the player meets the eligibility criteria.
# Print "Player is eligible" if all conditions are met, otherwise print "Player is not eligible".
age = 30
number_of_matches_played = 300
number_of_goals_scored = 1
is_injured = False

if (
    (18 <= age < 35)
    and (number_of_matches_played > 10 or number_of_goals_scored >= 5)
    and not is_injured
):
    print("Eligible")
else:
    print("Not Eligible")
