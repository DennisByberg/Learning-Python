course = "python programming  "
phrase = "   Learn Python, it's fun!   "
quote = "the quick brown fox jumps over the lazy dog"
email = "student@university.com"

# Convert course to uppercase, lowercase, and title case (first letter of each word capitalized).
course_uppercase = course.upper()
course_lowercase = course.lower()
course_titlecase = course.title()

# Remove leading and trailing whitespace from course and phrase using the appropriate methods.
clean_phrase = phrase.strip()

# Combine rstrip() and lstrip() to remove all spaces from course in one step.
clean_phrase2 = phrase.lstrip().rstrip()

# Find the index of the word "Python" in phrase.
index_of_python = phrase.find("Python")

# Use .find() to search for the word "dog" in the quote string. What does it return if the word isn’t found?
is_dog_in_the_quote_string = quote.find(
    "dog"
)  # index 40, it returns -1 if the word isn't found.

# Search for the substring "fox" in quote. What is the result?
quote_sub = quote.find("fox")  # answer: 16

# Replace all occurrences of "p" with "P" in course.
replaced_course = course.replace("p", "P")

# Replace "fox" with "cat" in quote to make it say: "The quick brown cat jumps over the lazy dog".
replaced_with_cat = quote.replace("fox", "cat")

# Check if "Python" exists in course and print True or False.
is_python_in_course = "Python" in course
print(is_python_in_course)

# Check if "C++" does not exist in course and print the result.
is_not_c_plus_plus_in_course = "C++" not in course
print(is_not_c_plus_plus_in_course)

# Use .count() to find out how many times the letter "o" appears in quote.
o_counter = quote.count("o")
print(o_counter)

# Split the quote string into a list of words. Print the list.
quote_list = quote.split(" ")
print(quote_list)

# Check if the string email contains only alphanumeric characters (letters and numbers) using .isalnum().
is_email_only_alphanumeric_characters = email.isalnum()

# Check if course consists only of alphabetic characters using .isalpha().
is_course_alpha = course.isalpha()

# Verify if course is in all lowercase with .islower().
is_course_in_all_lowercase = course.islower()

# Check if the email ends with "com".
is_email_end_com = email.endswith("com")

# Create a new string by joining the words in quote back together using a comma , as the separator.
new_quote_string = ",".join(quote_list)

# Capitalize the first character of the string quote using .capitalize().
cap_quote = quote.capitalize()

# Use .swapcase() on course to switch the case of each letter.
course_swapped_case = course.swapcase()

# Given the email address "student@university.com", split it into the username and domain. Then, print a message like "Username: student, Domain: university.com".
splittedEmail = email.split("@")

if len(splittedEmail) == 2:
    username, domain = splittedEmail
    message = f"Username: {username} Domain: {domain}"
else:
    message = "invalid email format"
