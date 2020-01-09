class Terrain():
    def __init__(self, name, description, damage = 0, helps = []):
        self.name = name
        self.description = description
        self.damage = damage
        self.helps = helps

terrains = Terrain("The Grasslands", "The tall grass makes it difficult to see whats hiding. Be careful!", 1, ["pants"])