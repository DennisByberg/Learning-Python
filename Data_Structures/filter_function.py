# Challenge: Filter Out Even Numbers from a List
# Write a program that filters out even numbers from a list of integers
# using the filter function and a lambda function. The list contains a mix of even and odd numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = list(filter(lambda number: number % 2 == 1, numbers))
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

print("odd_numbers: ", odd_numbers)
