# Challenge: Sort a List of Tuples by Multiple Criteria
# Write a program that sorts a list of tuples based on multiple criteria using a lambda function.
# The list contains tuples representing products with their names, prices, and ratings.
# Your task is to sort the list first by price in ascending order
# and then by rating in descending order.

# Example Input:
products = [
    ("Product1", 10, 4.5),
    ("Product2", 9, 4.7),
    ("Product3", 12, 4.3),
    ("Product4", 10, 4.8),
]

# Expected Output:
# [
#     ("Product2", 9, 4.7),
#     ("Product1", 10, 4.5),
#     ("Product4", 10, 4.8),
#     ("Product3", 12, 4.3)
# ]

sorted_list = sorted(products, key=lambda product: (product[1], -product[2]))
print(sorted_list)
