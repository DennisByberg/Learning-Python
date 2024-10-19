from collections import Counter

sentence = "This is a common interview question and and"

# Count the frequency of each character
char_frequency = Counter(sentence)

# Sort the characters by frequency in descending order
char_frequency_sorted = char_frequency.most_common()

# Find the most repeated character, excluding spaces
most_repeated_char = char_frequency_sorted[0][0]
if most_repeated_char == " ":
    most_repeated_char = char_frequency_sorted[1][0]

print(f"The letter '{most_repeated_char}' is the most used")
