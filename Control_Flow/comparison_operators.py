# Challenge: Compare two numbers and print whether the first number is greater than, less than, or equal to the second number. For example,
# if a = 5 and b = 3, the program should print "5 is greater than 3."
a = 10
b = 5

if a > b:
    print(f"{a} is bigger than {b}")
elif b < a:
    print(f"{b} is bigger than {a}")
else:
    print(f"{b} is equal to {a}")

# Challenge: Write a program that checks if a person is old enough to vote. Assume the legal voting age is 18.
# You should have a variable age and print whether the person is eligible to vote or not.
age = int(input("enter your age: "))
print(f"You can {"not vote" if age < 18 else "vote"}!")

# Challenge: Given a temperature in Celsius, determine if it’s considered "cold" (below 10°C), "warm" (between 10°C and 25°C), or "hot" (above 25°C). Print the result based on the temperature.
while True:
    try:
        temp = int(input("Enter the temperature in Celsius: "))
        break

    except ValueError:
        print("Please enter a valid integer for the temperature.")

if temp > 25:
    print("Hot")
elif temp >= 10:
    print("Warm")
else:
    print("Cold")

# Challenge: Given a number, check if it falls within the range of 10 to 20 (inclusive). Print whether the number is in the range or not.
number = 0
while number < 10 or number > 20:
    number = int(input("Enter a number between 10 and 20: "))

print(f"{number} is between 10 and 20")
