from room import Room
from player import Player
import random
import math
import bcrypt

class World:
    def __init__(self):
        self.starting_room = None
        self.rooms = {}
        self.players = {}
        self.create_world()
        self.password_salt = bcrypt.gensalt()

    def add_player(self, username, password1, password2):
        if password1 != password2:
            return {'error': "Passwords do not match"}
        elif len(username) <= 2:
            return {'error': "Username must be longer than 2 characters"}
        elif len(password1) <= 5:
            return {'error': "Password must be longer than 5 characters"}
        elif self.get_player_by_username(username) is not None:
            return {'error': "Username already exists"}
        password_hash = bcrypt.hashpw(password1.encode(), self.password_salt)
        player = Player(username, self.starting_room, password_hash)
        self.players[player.auth_key] = player
        return {'key': player.auth_key}

    def get_player_by_auth(self, auth_key):
        if auth_key in self.players:
            return self.players[auth_key]
        else:
            return None

    def get_player_by_username(self, username):
        for auth_key in self.players:
            if self.players[auth_key].username == username:
                return self.players[auth_key]
        return None

    def authenticate_user(self, username, password):
        user = self.get_player_by_username(username)
        if user is None:
            return None
        password_hash = bcrypt.hashpw(password.encode() ,self.password_salt)
        if user.password_hash == password_hash:
            return user
        return None

    def create_world(self):
        # Generate 100 rooms in a 10x10 grid style
        # generate them first, then connect them all together
        num_rooms = 100
        rows = 10
        columns = 10
        names = ["Grass", "Rock", "Bush"]
        descriptions = ["Grass", "Rock", "Bush"]
        id = 0
        x = 0
        y = 0

        rooms = []
        for col in range(columns):
            for row in range(rows):
                name = random.choice(names)
                description = name  # random.choice(descriptions)
                x = col
                y = row
                room = Room(name, description, id, x, y)
                self.rooms[id] = room
                self._rooms.append(room)
                id += 1
                rooms.append(room)

        print(rooms)
        self.starting_room = self.rooms[0]
        # connect all the rooms in grid style
        id = 0
        for col in range(columns):
            for row in range(rows):
                print('x')
                room = self.rooms[id]
                if row - 1 > 0:
                    room_n = self.rooms[col + (row - 1) * 10]
                    room.n_to = room_n
                if col + 1 < 10:
                    room_e = self.rooms[col + 1 + row * 10]
                    room.e_to = room_e
                if row + 1 < 10:
                    room_s = self.rooms[col + (row + 1) * 10]
                    room.s_to = room_s
                if col - 1 > 0:
                    room_w = self.rooms[col - 1 + row * 10]
                    room.w_to = room_w
                id += 1








