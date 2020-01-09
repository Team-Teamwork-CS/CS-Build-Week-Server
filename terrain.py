class Terrain():
    def __init__(self, name, description, damage = 0, helps = []):
        self.name = name
        self.description = description
        self.damage = damage
        self.helps = helps

terrains = [
    Terrain("The Grasslands", "The tall grass makes it difficult to see whats hiding. Be careful!"),
    Terrain("The Rough", "Terrain looks rough. Going to be tough to travel through here with bare feet.", 2),
    Terrain("The Bush","Traveling through the bush is a nightmare! Its loaded with monsters and will destroy your body if you're not covered"),
    Terrain("The Forest","The sounds of the birds chirping in the forest is inviting. Just don't enter at night."),
    Terrain("The Desert", "The desert will drain you if you are not prepared!"),
    Terrain("The River", "Water looks calm, but it is impossible to know what lurks below."),
    Terrain("The Mountains", "Mountains are exhausting to travel through. Best to avoid them if possible.")
]