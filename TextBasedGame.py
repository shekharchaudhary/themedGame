# Shekhar Chaudhary

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.

def show_instructions():
    print("Dragon Text Adventure Game")
    print("Collect 7 items to win the game, or lose the game")
    print("Move direction: south, north, east, west")
    print("Add to Inventory: get 'item name'")
    print("----------------------")


def show_status_of_player(room, inventory, items):
    print(f"You are in the {room}")
    print(f"Inventory: {inventory}")
    if items:
        print(f"You see a {items}")
    print("----------------------")


def main():
    rooms = {
        'Entrance Hall': {
            'north': 'Library',
            'south': 'Physics Lab',
            'east': 'Cafeteria',
            'west': 'Secrete Room',
        },
        'Library': {
            'south': 'Entrance Hall',
            'east': 'Generator Room',
            'item': 'map'
        },
        'Physics Lab': {
            'north': 'Entrance Hall',
            'east': 'Biology Lab',
            'west': 'Chemistry Lab',
            'item': 'lighter'
        },
        'Secrete Room': {
            'east': 'Entrance Hall',
            'item': 'Dragon'
        },
        'Cafeteria': {
            'west': 'Entrance Hall',
            'north': 'Kitchen',
            'item': 'utensils'
        },
        'Kitchen': {
            'south': 'Cafeteria',
            'item': 'knife'
        },
        'Generator Room': {
            'west': 'Library',
            'item': 'keys'
        },
        'Biology Lab': {
            'west': 'Physics Lab',
            'item': 'safety glasses'
        },
        'Chemistry Lab': {
            'east': 'Physics Lab',
            'item': 'gas cylinder'
        }
    }

    items = {
        'map': 'Library',
        'lighter': 'Physics Lab',
        'Dragon': 'Secrete Room',
        'utensils': 'Cafeteria',
        'knife': 'Kitchen',
        'keys': 'Generator Room',
        'safety glasses': 'Biology Lab',
        'gas cylinder': 'Chemistry Lab'
    }

    current_location = 'Entrance Hall'  # starting room of the game

    # According to the dictionary, find the corresponding dictionary value

    print('\n', rooms[current_location])

    # direction = ''  # player does not have any direction yet

    # Function to move around the rooms
    def move_to_direction(current_room, go_to_direction):
        if go_to_direction in rooms[current_room]:
            current_room = rooms[current_room][go_to_direction]
            return current_room
        else:
            print(f"You can't go {go_to_direction} from here.")

    # Define a function to get items from the room
    def get_item(current_room, item):
        if item in items and items[item] == current_room:
            inventory.append(item)  # Add the item to the inventory
            del items[item]  # Delete the item once it has been picked up
            print(f"You picked up {item}!")
        else:
            print(f"You can't get {item} here.")

    # Define a list to represent the player's inventory
    inventory = []

    show_instructions()  # invoke function to get status of the player

    # The player should loop or move in the room unless player should exit the room so use while loop
    # The Game Loop

    while True:
        show_status_of_player(current_location, inventory, rooms[current_location].get('item'))

        direction = input('Move to which direction!').lower()
        print('You entered ', direction)

        if direction in rooms[current_location].keys():
            current_location = rooms[current_location][direction]
            get_item(current_location, rooms[current_location].get('item'))
            move_to_direction(current_location, direction)  # execute the move function

        else:
            print('please enter another direction')

        if current_location == 'Secrete Room':
            if len(inventory) >= 7:  # collect every item from rooms
                print("Congratulations! You have collected all items and defeated the dragon!")
                break
            else:
                print("Too early to enter the secrete room without all items GAME OVER!!!")
                break


print("Thanks for playing the game. Hope you enjoyed it.")

if __name__ == '__main__':
    main()

# There are some other edge cases that has to be  resolved, Thank you
