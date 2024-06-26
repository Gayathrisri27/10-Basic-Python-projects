import random

# Get the comma-separated names string from the user
names_string = input("Enter names separated by commas: ")
names = names_string.split(",")

# Get the number of items in the list
num_items = len(names)

# Select a random index
random_choice = random.randint(0, num_items - 1)

# Print the randomly selected name
print(names[random_choice])
