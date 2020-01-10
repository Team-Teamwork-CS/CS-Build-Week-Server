# Implementing an Item Class to hold information about items. Includes names, descriptions, positions, and comabt attributes.

class Weapon:
    """A simple Weapon Class"""
    def __init__(self, name, description, location, damage, price):
        self.name = name
        self.description = description
        self.location = location
        self.damage = damage
        self.price = price

    def __str__(self):
        return "{}\n=====\n{}\nPrice: {}\n".format(self.name, self.description, self.price)    

class Stick(Weapon):
    def __init__(self):
        self.name = "Stick"
        self.description = "A stick to whack enemies with. Better than no stick!"
        self.damage = 8
        self.price = 2

class Knife(Weapon):
    def __init__(self):
        self.name = "Knife"
        self.description = "A knife to cut and stab. Bit rusty but oh well."
        self.damage = 12
        self.price = 6


class Sword(Weapon):
    def __init__(self):
        self.name = "Sword"
        self.description = "A fine weapon. Slash and hack your way to victory."
        self.damage = 24
        self.price = 12


class Edible:
    """A simple Edible Class"""
    def __init__(self, name, description, location, damage, price):
        self.name = name
        self.description = description
        self.healing = healing
        self.price = price


class Bread(Edible):
    def __init__(self, name, description, location, damage, price):
        self.name = "Bread"
        self.description = "Some stale bread to keep your strength up. Restores 20 HP!"
        self.healing = 20
        self.price = 10

class Elixir(Edible):
    def __init__(self, name, description, location, damage, price):
        self.name = "Elixir"
        self.description = "A magic potion that restores 100 HP!"
        self.healing = 100
        self.price = 40
