from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

rest_api = Flask(__name__)
rest_api.secret_key = 'dimi'
api = Api(rest_api)

jwt = JWT(rest_api, authenticate, identity) #/auth

api.add_resource(Item, '/items/<string:name>') 
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
        rest_api.run(port = 5000, debug = True)