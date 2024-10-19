def fizz_buzz(user_input):
    if user_input % 3 == 0 and user_input % 5 == 0:
        return "fizzbuzz"
    if user_input % 3 == 0:
        return "fizz"
    if user_input % 5 == 0:
        return "buzz"
    return user_input


print(fizz_buzz(3))
