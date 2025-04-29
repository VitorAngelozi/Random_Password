import random

# Arrays for letters, numbers, and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
           'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['$', '%', '#', '@', '_', '!', '&', '*']

# Asking the user for password details
letter_count = int(input("How many letters would you like in your password? "))
number_count = int(input("How many numbers would you like in your password? "))
symbol_count = int(input("How many symbols would you like in your password? "))

# Creating an array to build the password before turning it into a string
password = []

# Randomly selecting and adding characters to the password array
for _ in range(letter_count):
    password += random.choice(letters)

for _ in range(number_count):
    password += random.choice(numbers)

for _ in range(symbol_count):
    password += random.choice(symbols)

# Shuffling the array to make the password more secure
random.shuffle(password)

# Joining the array into a single string
final_password = ''.join(password)
print(final_password)