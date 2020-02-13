from room import Room
from player import Player
from items import Item

# Decalre all the items
items = {
    "fire": Item("Fire",
    "It allows when playing light the rooms."),

    "shovel": Item("Shovel",
    "It allows the player to dig in the rooms and find more items."),

    "food": Item("Food",
    "It allows the player to feed and recover"),

    "money": Item("Money","Who doesn't need money??")
}

# Declare all the rooms
room = {
        'outside':  Room("Outside Cave Entrance","""North of you, the cave
                         mount beckons"""),

        'foyer':    Room("Foyer", """Dim light filters in from the south.
                         Dusty passages run north and east."""),

        'overlook': Room("Grand Overlook", """A steep cliff appears before
                          you, falling into the darkness. Ahead to the north,
                          a light flickers in the distance, but there is no way
                          across the chasm."""),

        'narrow':   Room("Narrow Passage", """The narrow passage bends here from
                        west to north. The smell of gold permeates the air."""),

        'treasure': Room("Treasure Chamber", """You've found the long-lost
                          treasure chamber! Sadly, it has already been
                          completely emptied by earlier adventurers.
                          The only exit is to the south.""")
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

# room['outside'].add_item(items['money'])
# room['foyer'].add_item(items['fire'])
# room['overlook'].add_item(items['shovel'])
# room['narrow'].add_item(items['food'])
# room['treasure'].add_item(items['money'])
# # Main
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
print("..........................................")
print("..............ADVENTURE GAME..............")
print("......                              ......")
user_name = input("...... Please write your name:  ").upper()

# Make a new player object that is currently in the 'outside' room.
initial = room['outside']
player = Player(user_name, initial)
# * Waits for user input and decides what to do.

print(f"\nHello {user_name}!!!!\nYou can move arround the rooms using:")
print("\nn --> North\ns --> South\ne --> East\nw --> West\n")
print("q --> Quit the game\n")
print(f"{player.name} you start the game here: {player.currently}" )
directions = ['e','w','n','s']
start = True
while(start):
    d = input("\nWhere do you wanna go?:").lower()
    if d == 'q':
        print('Bye...')
        break
    elif d in directions:
        last_room = player.currently
        player.direction(d)

        print(f'{user_name} you are in {player.currently}')
        # NOTE:
        # print(f'Item here: {player.currently.show_inventory()}')
        # i = input('Type (d)rop or (t)ake to save this item in you bag')
        # if i == 'd':
        #     if item_here in player.inventory.keys():
        #         player.inventory[item_here].on_drop()
        #         player.drop_item(item_here)
        #     else:
        #         print("You cannot drop an item that it's not in your bag")
        # elif i == 't':
        #     print(item_here)

    #
    # if d in ['i', 'inventory']:
    #     print('Those are your items: ')
    #     player.show_inventory()

    else:
        print('Invalid coordinate')


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
