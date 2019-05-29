from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Joe Schmoe", room['outside'])

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while True:
    print(f"\nHey there, you are currently located {player.current_room.name}")
    print(f'\n{player.current_room.description}')
    user_input = input(
        f'\nwhere to next, {player.name}?\n\nvalid options: [n], [s],'
        ' [e], [w] or [q]\n-------------------------\n')
    if user_input == 'q':
        print('Thanks for playing!')
        break
    elif user_input == 'n':
        if player.current_room.n_to:
            print('moving north...')
            player.current_room = player.current_room.n_to
        else:
            print('I\'m afraid that is not possible')
    elif user_input == 's':
        if player.current_room.s_to:
            print('moving south...')
            player.current_room = player.current_room.s_to
        else:
            print('I\'m afraid that is not possible')

    elif user_input == 'e':
        if player.current_room.e_to:
            print('moving east...')
            player.current_room = player.current_room.e_to
        else:
            print('I\'m afraid that is not possible')
    elif user_input == 'w':
        if player.current_room.w_to:
            print('moving west...')
            player.current_room = player.current_room.w_to
        else:
            print('I\'m afraid that is not possible')
    else:
        print('**please enter one of the valid options**')
