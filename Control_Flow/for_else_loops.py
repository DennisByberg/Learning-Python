# Challenge: Write a program to check if a football player has scored in every game of a season using a for-else loop.

# Instructions:
# You have a list representing the number of goals scored by the player in each game of the season.
goals_per_game = [1, 2, 1, 3, 1]
# Use a for loop to iterate through this list.
# If the player scored 0 goals in any game, print "Scored 0 in a game!" and break out of the loop.
# If the player scored in every game (i.e., no 0 goals), print "Scored in every game!".
# Note: You should use the else part of the for loop to handle the case where no game had 0 goals.


# Your for-else loop should go here
for goals_in_game in goals_per_game:
    if goals_in_game == 0:
        print("Scored 0 in a game!")
        break
else:
    print("Scored in every game!")
