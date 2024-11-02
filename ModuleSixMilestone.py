# This is module six milestone
# Shekhar Chaudhary
# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Entrance Hall': {'north': 'Library', 'south': 'Physics Lab', 'east': 'Cafeteria', 'west': 'Secrete Room'},
    'Library': {'south': 'Entrance Hall', 'east': 'Generator Room'},
    'Physics Lab': {'north': 'Entrance Hall', 'east': 'Biology Lab', 'west': 'Chemistry Lab'},
    'Secrete Room': {'east': 'Entrance Hall'},
    'Cafeteria': {'west': 'Entrance Hall', 'north': 'Kitchen'},
    'Kitchen': {'south': 'Cafeteria'},
    'Generator Room': {'west': 'Library'},
    'Biology Lab': {'west': 'Physics Lab'},
    'Chemistry Lab': {'east': 'Physics Lab'}
}

current_location = 'Entrance Hall'  # starting room of the game

# According to the dictionary, find the corresponding dictionary value

print('\n', rooms[current_location])

# Available direction

# print(rooms[current_location].keys())
# print(*rooms[current_location].keys())

# rooms that are available

# print(rooms[current_location].values())
# print(*rooms[current_location].values())

direction = ''  # player does not have any direction yet


# Function to move around the rooms
def move_to_direction(current_room):
    return current_room


# The player should loop or move in the room unless player should exit the room so use while loop
# The Game Loop

while direction != 'exit':
    print('\nYou are in the ', current_location)

    players_possible_moves = rooms[current_location].keys()
    print('here are the players possible moves', *players_possible_moves)

    direction = input('Move to which direction!').lower()
    print('You entered ', direction)

    if direction in rooms[current_location].keys():
        current_location = rooms[current_location][direction]
        print(move_to_direction(current_location))  # execute the move function
    else:
        print('please enter another direction')

print('Thank you for Playing')