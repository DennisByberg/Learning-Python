number = 10
username = "admin"
password = "1234"

# Challenge: Write a program that takes a number and checks if it is odd or even.
# If the number is divisible by 2, print "The number is even."
# If the number is not divisible by 2, print "The number is odd."
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Challenge: Write a program that checks if a number is positive, negative, or zero.
# If the number is greater than 0, print "Positive number."
# If the number is less than 0, print "Negative number."
# If the number is exactly 0, print "The number is zero."
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")


# Challenge: You are given a username and a password. Write a program that checks if both the username and password are correct.
# If the username is "admin" and the password is "1234", print "Login successful!"
# Otherwise, print "Invalid username or password."
if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Invalid username or password.")
