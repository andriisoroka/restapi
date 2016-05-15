from flask_restful import Resource,reqparse
from app.jsoongia import Serializer, relationships
from flask import request

class UserSerializer(Serializer):
    ref = 'id'
    type = 'user'
    attributes = ['name','email','password']


mass = [
    {"id":1,"name":"Andrii Soroka","email":'andrii_soroka@ukr.net',"password":'12121dasdsdcd'},
    {"id":2,"name":"Uliana Soroka","email":"starosta_7@mail.ru","password":'dfhjk4389034kl'}
]
parse_data_model = reqparse.RequestParser()
parse_data_model.add_argument('data',type=dict)

class User(Resource):
    def get(self,id):
        serializer = UserSerializer()
        res = serializer.serialize(mass[0],{})
        return res

    def put(self,id):
        return []

    def delete(self,id):
        return []


class UserList(Resource):
    def get(self):
        serializer = UserSerializer()
        res = serializer.serialize(mass,{})
        return res

    def post(self):
        try:
            id = mass[-1]['id'] + 1
            newUser = request.get_json(force=True)
            newUser['data']['id'] = id
            mass.append({"id":id,"name":newUser['data']['attributes']['name'],"email":newUser['data']['attributes']['email'],"password":newUser['data']['attributes']['password']})
            return newUser
        except Exception as e:
            print(e)