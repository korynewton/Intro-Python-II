from room import Room
from player import Player
from item import Item

# Declare all the rooms

game_items = {
    'knife': Item('knife', 'a v sharp blade to protect oneself'),
    'map': Item('map', 'a detailed map of the realm'),
    'money': Item('money', 'bitcoin, of course'),
    'coffee': Item('coffee',
                   'provides a quick burst of concentration and energy'),
    'lamp': Item('lamp', 'a great way to see in the dark'),
    'water': Item('water',
                  'an excellent way to stay hydrated on the ' +
                  'long journey that awaits you'),
    'tissues': Item("tissues", "a great way to wipe your tears after" +
                    " discovering that the treasure is long gone")
}


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

# Add items to room
room['outside'].items.append(game_items['knife'])
room['outside'].items.append(game_items['water'])
room['foyer'].items.append(game_items['coffee'])
room['overlook'].items.append(game_items['money'])
room['overlook'].items.append(game_items['water'])
room['narrow'].items.append(game_items['lamp'])
room['treasure'].items.append(game_items['tissues'])


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Joe Schmoe", room['outside'])


# main loop
while True:
    print(player.current_room)
    user_input = input(
        f'\nwhats your next move, {player.name}?\n\nvalid options: [n], [s],'
        ' [e], [w], [i], [q] or [pickup/drop *item*]\
            \n-------------------------\n>').lower().split()
    if len(user_input) == 1:
        if user_input[0] in ['q', 'quit']:
            print('Thanks for playing!')
            break
        elif user_input[0] in ['n', 's', 'e', 'w']:
            player.handle_move(user_input[0])
        elif user_input[0] in ['i', 'inventory']:
            print("Current Inventory: " +
                  ", ".join([str(item.name) for item in player.inventory]))
    elif len(user_input) == 2 and user_input[0] in ['pickup', 'drop']:
        action_item = game_items[user_input[1]]
        if user_input[0] == 'pickup':
            player.pickup_item(action_item)
            player.current_room.remove_from_room(action_item)
        elif user_input[0] == 'drop':
            player.drop_item(action_item)
            player.current_room.add_to_room(action_item)
        else:
            print('**Not a valid option**')
    else:
        print('**please enter one of the valid options**')
