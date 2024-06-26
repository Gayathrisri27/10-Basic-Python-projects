# Create a 3x3 empty map
treasure_map = [['-', '-', '-'],
                ['-', '-', '-'],
                ['-', '-', '-']]

def print_map(map):
    for row in map:
        print(' '.join(row))

# Display the empty map
print("Empty Treasure Map:")
print_map(treasure_map)

# Get the treasure coordinates from the user
x = int(input("Enter the row (0, 1, or 2) to place the treasure: "))
y = int(input("Enter the column (0, 1, or 2) to place the treasure: "))

# Place the treasure on the map
treasure_map[x][y] = 'X'

# Display the updated map
print("Treasure Map with the treasure placed:")
print_map(treasure_map)
