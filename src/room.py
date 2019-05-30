# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        n_to = None
        s_to = None
        e_to = None
        w_to = None

    def __repr__(self):
        string_of_items = "\n".join([str(x) for x in self.items])
        return f"\nCurrent Location: {self.name}...{self.description}.\n\n \
           Items availabe: \n{string_of_items}"

    def add_to_room(self, item):
        self.items.append(item)
        print(f'**{item.name} added to room**')

    def remove_from_room(self, item):
        self.items.remove(item)
        print(f'**{item.name} removed from room**')
