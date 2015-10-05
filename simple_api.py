import os
from flask import Flask, request
from user import User
import json

__author__ = 'Max Buck'
__email__ = 'maxbuckdeveloper@gmail.com'
__version__ = '1.0.0'


app = Flask(__name__)

# API CHECK#############################################################################################################


@app.route('/', methods=['GET'])
def index():
    """ Call this method for basic version info or to ensure the api is running. """
    return 'Your api is up and running!'


# USER METHODS##########################################################################################################


@app.route('/users/<id>', methods=['GET', 'PATCH', 'DELETE'])
@app.route('/users', defaults={'id': None}, methods=['POST', 'GET'])
def user(id):
    """Methods directly Related to the user resource"""
    response = None
    if request.method == 'POST':
        response = User.create_resource(eval(request.data))
    elif request.method == 'PATCH':
        response = User.update_resource(eval(request.data), id)
    elif request.method == 'DELETE':
        response = User.deactivate_resource(id)
    elif request.method == 'GET' and id:
        response = User.get_resource(request.args, id)
    elif request.method == 'GET':
        response = User.get_collection(request.args)
    return response


@app.route('/users/<id>/relationships/<related_collection_name>', methods=['POST', 'PATCH', 'DELETE', 'GET'])
def user_relationships(id, related_collection_name):
    """Methods related to user relationships"""
    response = None
    if request.method == 'POST':
        response = User.create_relationships(id, related_collection_name, eval(request.data))
    elif request.method == 'PATCH':
        response = User.update_relationship(id, related_collection_name, json.loads(request.data))
    elif request.method == 'DELETE':
        response = User.disconnect_relationship(id, related_collection_name, eval(request.data))
    elif request.method == 'GET':
        response = User.get_relationship(request.args, id, related_collection_name)
    return response


# FLASK INFO############################################################################################################


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10200, debug=True)