# Challenge 1: Convert and Concatenate
# Write a program that takes two inputs from the user:
# one as a string and the other as an integer. Convert the integer to a string and concatenate it with the original string input. Print the result.
x = input("enter a string: ")
y = int(input("enter an integer: "))

result = x + str(y)
print(result)

# Challenge 2: Sum of String Numbers
# Write a program that takes two inputs from the user. Both inputs should be numbers in string format. Convert them to integers, calculate their sum, and print the result.
num1 = input("enter number 1: ")
num2 = input("enter number 2: ")

sum = int(num1) + int(num2)
print(f"Sum: {sum}")
