# Challenge: Print the first and last number in a number list,
# also print the numbers between in a separated variable
numbers = list(range(1, 11))
print(numbers)

first, *other_numbers, last = numbers
print(f"first number: {first}")
print(f"last number: {last}")
print(f"other numbers: {other_numbers}")
