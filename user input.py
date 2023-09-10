# Request user input
user_input = input("Please enter your name: ")

# Display the user's input
print("Hello, " + user_input + "!")

# Convert user input to uppercase
print("Uppercase: " + user_input.upper())

# Convert user input to lowercase
print("Lowercase: " + user_input.lower())

# Check if user input starts with a specific letter
start_letter = input("Enter a letter to check if your name starts with it: ")
if user_input.startswith(start_letter):
    print("Your name starts with " + start_letter)
else:
    print("Your name does not start with " + start_letter)

# Count the number of characters in user input
char_count = len(user_input)
print("Number of characters in your name: " + str(char_count))

# Replace a character in user input
replace_char = input("Enter a character to replace in your name: ")
new_name = user_input.replace(replace_char, '_')
print("Name with " + replace_char + " replaced: " + new_name)

# Split user input by spaces and display as a list
name_parts = user_input.split()
print("Name parts:", name_parts)

# Check if user input contains only alphabetic characters
if user_input.isalpha():
    print("Your name contains only alphabetic characters.")
else:
    print("Your name contains non-alphabetic characters.")

# Check if user input is numeric
if user_input.isnumeric():
    print("Your name is numeric.")
else:
    print("Your name is not numeric.")





