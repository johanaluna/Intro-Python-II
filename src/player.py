# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:

    def __init__(self,name,initial):
        self.name = name
        self.currently = initial
        self.inventory = []


    def direction(self,coord):
        coordinates = {
            'n': self.currently.n_to, 's': self.currently.s_to,
            'e': self.currently.e_to,'w': self.currently.w_to}
        if coordinates[coord] != None:
            self.currently = coordinates[coord]

    def take_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.delete(item)
        """
        pop() method returns the item present at the given index.
        This item is also removed from the list.
        """
            # self.inventory.pop(item.name)

    def show_inventory(self):
        for n in self.inventory:
            return

    def __str__(self):
        return f"{self.name}{self.currently}{self.inventory}"
