# Challenge: Dynamic List Manager

# Initialize an empty list called fruits.
# Ask the user to add items to the list or remove items from it using the following commands:
# "add item_name": Adds the specified item_name to the list.
# "remove item_name": Removes the specified item_name from the list (if it exists).
# "show": Prints the current list.
# "quit": Exits the program.
# Edge Cases:
# If the user tries to remove an item that doesn't exist, print a message like "Item not found.".
# Ensure that the list doesn't allow duplicate items.
# Keep the Program Running:
# The program should continuously accept input until the user types "quit".
fruits = []


def add_fruit_and_print_message(fruit_to_add):
    fruits.append(fruit_to_add)
    print(f"\033[92m added {fruit_to_add} to the list\033[0m\n")


def remove_fruit_and_print_message(fruit_to_remove, i):
    fruits.pop(i)
    print(f"\033[91m removed {fruit_to_remove} from the list\033[0m\n")


while True:
    user_input = input(
        "'add fruit_name', 'remove fruit_name', 'show' or 'quit'\n>> "
    ).lower()

    if user_input.startswith("add "):
        user_input_fruit = user_input[4:].strip()

        # Check if fruit already exists in fruits
        if user_input_fruit in fruits:
            print("Fruit already exists")
        else:
            add_fruit_and_print_message(user_input_fruit)

    elif user_input.startswith("remove "):
        user_input_fruit = user_input[7:].strip()

        # Check if fruit exists in the list and remove it
        if user_input_fruit in fruits:
            index = fruits.index(user_input_fruit)
            remove_fruit_and_print_message(user_input_fruit, index)
        else:
            print("Can't find fruit in the list")

    elif user_input == "show":
        print(fruits)

    elif user_input == "quit":
        break

    else:
        print("Invalid command. Please try again.")

print("Final list:", fruits)
