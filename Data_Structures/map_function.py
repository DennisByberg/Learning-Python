# Challenge: Extract and Capitalize First Names from a List of Full Names
# Write a program that extracts the first names from a list of full names
# and capitalizes them using the map function and a lambda function.
# The list contains full names in the format "First Last".

# Expected Output:
# ["John", "Jane", "Alice", "Bob"]

# Define the list of full names as shown in the example input.
full_names = ["john doe", "jane smith", "alice johnson", "bob brown"]

# Use the map function with a lambda function to extract the first name
# from each full name and capitalize it.
# Convert the result of the map function to a list.
first_names = list(map(lambda name: name.split()[0].capitalize(), full_names))

# Sort the names
sorted_first_names = sorted(first_names)

# Print the list of capitalized first names and sorted.
print(sorted_first_names)
