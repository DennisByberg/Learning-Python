# Football Scoring Simulator
# Challenge: Write a program that simulates a football match scoring system.
# The program should keep track of the goals scored by two teams until one team reaches a specified winning score.
# Instructions:

# Set the winning score (e.g., winning_score = 5).
# Initialize the scores for both teams (e.g., team_a_score = 0 and team_b_score = 0).
# Use a while loop to keep asking for goals scored until one of the teams reaches the winning score.
# Inside the loop:
# Prompt the user to enter which team scored (either "A" for Team A or "B" for Team B).
# If the user enters "A", increment team_a_score.
# If the user enters "B", increment team_b_score.
# Print the current scores after each entry.
# Once one of the teams reaches the winning score, print the final score and declare the winner.

# # Your while loop should go here
winning_score = 5
team_a_score = 0
team_b_score = 0

while (team_a_score < winning_score) and (team_b_score < winning_score):
    print(f"Team A Score: {team_a_score}")
    print(f"Team B Score: {team_b_score} \n")

    user_input = input("Enter A or B to choose which team scored: ")

    if user_input.upper() == "A":
        team_a_score += 1
    elif user_input.upper() == "B":
        team_b_score += 1
    else:
        print("\033[91mInvalid input, try again!\033[0m\n")

print(f"The winner is {"TEAM A" if team_a_score > team_b_score else "TEAM B"}")
