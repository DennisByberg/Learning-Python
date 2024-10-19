numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = list(filter(lambda number: number % 2 == 1, numbers))
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

# Write this using list comprehensions instead.

odd_numbers2 = [number for number in numbers if number % 2 == 1]

# and map...?
products = [
    ("Product1", 10, 4.5),
    ("Product2", 9, 4.7),
    ("Product3", 12, 4.3),
    ("Product4", 10, 4.8),
]

prices = [product[1] for product in products]


print(odd_numbers2)
print(prices)
