# for number in range(5):
#     print("Hello", number)

# Challenge: You have a list of the number of goals scored by a player in each of the last 5 matches:
# Write a program to calculate the total number of goals and check if the player scored in every match.
# Instructions:
# Use a for loop to iterate over the list of goals.
# Count the total number of goals scored in all matches.
# Check if the player scored in every match (i.e., there should be no match with 0 goals).
# Print the total number of goals.
# If the player scored in every match, print "Player scored in all matches!". Otherwise, print "Player did not score in every match."

goals_per_match = [2, 1, 3, 1, 1, 0]
goal_counter = 0
goal_in_every_match = True
for goals_in_match in goals_per_match:
    if goals_in_match > 0:
        goal_counter += goals_in_match
    else:
        goal_in_every_match = False

print(
    f"The player scored {goal_counter} goals in the last {len(goals_per_match)} matches, "
    f"The player {'scored in all matches' if goal_in_every_match else 'did not score in all matches'}"
)
