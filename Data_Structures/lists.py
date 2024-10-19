numbers = list(range(1, (20 + 1)))

odd_numbers = []
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("even_numbers", even_numbers)
print("odd numbers", odd_numbers)
