# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    """
    Room class in which we are creating the name of the rooms,
    their description and assigning some items to each room
    """
    def __init__(self,name,descrp,n_to=None, s_to=None,
                 e_to=None, w_to=None):
        self.name = name
        self.descrp = descrp
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.inventory = []

    def add_item(self, *item):
        self.inventory.append(item)

    def remove_item(self, *item):
        if item in self.inventory:
            self.inventory.remove(item)

    def show_inventory(self):
        for n in self.inventory:
            return n

    def __str__(self):
        return f"{self.name}: {self.descrp}"
