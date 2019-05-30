# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def handle_move(self, input):
        attribute = input + '_to'

        room_move = getattr(self.current_room, attribute)

        if room_move is not None:
            self.current_room = room_move
        else:
            print('sorry that move is not available')
