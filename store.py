"""A Store Class to handle transactions"""

import item

class Store:
    def __init__(self):
        self.name = "Store"
        self.gold = 1000000
        self.inventory = [items.Stick(),
                      items.Knife(),
                      items.Sword(),
                      items.Bread(),
                      items.Elixir(),
                      items.Stick(),
                      items.Knife(),
                      items.Sword(),
                      items.Bread(),
                      items.Elixir(),
                      items.Stick(),
                      items.Knife(),
                      items.Sword(),
                      items.Bread(),
                      items.Elixir()]
        #self.location =