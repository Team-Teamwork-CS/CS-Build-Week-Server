import hashlib
import json
from time import time
from uuid import uuid4
import bcrypt

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from pusher import Pusher
from decouple import config

from room import Room
from player import Player
from world import World

# Look up decouple for config variables
# pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))

world = World()

app = Flask(__name__)

CORS(app)

def get_player_by_header(world, auth_header):
    if auth_header is None:
        return None

    auth_key = auth_header.split(" ")
    if auth_key[0] != "Token" or len(auth_key) != 2:
        return None

    player = world.get_player_by_auth(auth_key[1])
    return player


@app.route('/api/registration/', methods=['POST'])
def register():
    values = request.get_json()
    required = ['username', 'password1', 'password2']

    if not all(k in values for k in required):
        response = {'message': "Missing Values"}
        return jsonify(response), 400

    username = values.get('username')
    password1 = values.get('password1')
    password2 = values.get('password2')

    response = world.add_player(username, password1, password2)
    if 'error' in response:
        return jsonify(response), 500
    else:
        return jsonify(response), 200


@app.route('/api/login/', methods=['POST'])
def login():
    params = request.get_json()
    required = ['username', 'password']
    if not all(x in params for x in required):
        response = {'message': "Missing username or password"}
        return jsonify(response), 400

    username = params.get('username')
    password = params.get('password')
    user = world.get_player_by_username(username)
    if user is not None:
        password_hash = bcrypt.hashpw(password.encode(), world.password_salt)
        if user.password_hash == password_hash:
            # return auth key and username
            player_key = world.get_player_by_auth(user)
            return {'key': player_key, 'username': username}
        else:
            response = {'message': "Incorrect password"}
            return jsonify(response), 400
    else:
        response = {'message': "Username incorrect or unregistered"}
        return jsonify(response), 400

@app.route('/api/adv/init/', methods=['GET'])
def init():
    player = get_player_by_header(world, request.headers.get("Authorization"))
    if player is None:
        response = {'error': "Malformed auth header"}
        return jsonify(response), 500

    response = {
        'title': player.current_room.name,
        'description': player.current_room.description,
    }
    return jsonify(response), 200


@app.route('/api/adv/move/', methods=['POST'])
def move():
    player = get_player_by_header(world, request.headers.get("Authorization"))
    if player is None:
        response = {'error': "Malformed auth header"}
        return jsonify(response), 500

    values = request.get_json()
    required = ['direction']

    if not all(k in values for k in required):
        response = {'message': "Missing Values"}
        return jsonify(response), 400

    direction = values.get('direction')
    if player.travel(direction):
        response = {
            'title': player.current_room.name,
            'description': player.current_room.description,
        }
        return jsonify(response), 200
    else:
        response = {
            'error': "You cannot move in that direction.",
        }
        return jsonify(response), 500


@app.route('/api/adv/take/', methods=['POST'])
def take_item():
    # IMPLEMENT THIS
    response = {'error': "Not implemented"}
    return jsonify(response), 400

@app.route('/api/adv/drop/', methods=['POST'])
def drop_item():
    # IMPLEMENT THIS
    response = {'error': "Not implemented"}
    return jsonify(response), 400

@app.route('/api/adv/inventory/', methods=['GET'])
def inventory():
    # IMPLEMENT THIS
    response = {'error': "Not implemented"}
    return jsonify(response), 400

@app.route('/api/adv/buy/', methods=['POST'])
def buy_item():
    # IMPLEMENT THIS
    response = {'error': "Not implemented"}
    return jsonify(response), 400

@app.route('/api/adv/sell/', methods=['POST'])
def sell_item():
    # IMPLEMENT THIS
    response = {'error': "Not implemented"}
    return jsonify(response), 400

@app.route('/api/adv/rooms/', methods=['GET'])
def rooms():
    rooms = []
    for room in world._rooms:
        room_dict = dict(room.__dict__)
        room_dict['n_to'] = room.n_to.id if room.n_to is not None else ""
        room_dict['e_to'] = room.e_to.id if room.e_to is not None else ""
        room_dict['s_to'] = room.s_to.id if room.s_to is not None else ""
        room_dict['w_to'] = room.w_to.id if room.w_to is not None else ""
        rooms.append(json.dumps(room_dict))

    response = {'rooms': rooms}
    return jsonify(response), 200


# Run the program on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
