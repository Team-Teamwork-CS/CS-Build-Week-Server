import random
import uuid
import item

class Player:
    def __init__(self, name, starting_room, password_hash):
        self.username = name
        self.current_room = starting_room
        self.auth_key = Player.__generate_auth_key()
        self.password_hash = password_hash
        self.uuid = uuid.uuid4
        self.gold = 25
        self.hp = 100
        self.inventory = [item.Stick()]

    def __generate_auth_key():
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        auth_key_list = []
        for i in range(40):
            auth_key_list.append(random.choice(digits))
        return "".join(auth_key_list)

    def travel(self, direction, show_rooms = False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            return True
        else:
            print("You cannot move in that direction.")
            return False

    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print('* ' + str(item))
        print("Gold: {}".format(self.gold))

    def heal(self):
        edibles = [item for item in self.inventory
                       if isinstance(item, item.Edible)]
        if not edibles:
            print("You don't have any edibles to heal you!")
            return

        for i, item in enumerate(edibles, 1):
            print("Choose an item to use to heal: ")
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = edibles[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice, try again.")

    
    def is_alive(self):
        return self.hp > 0


    def pick_up(self):
        pass

    def drop_item(self):
        pass
