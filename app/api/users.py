from flask_restful import Resource,reqparse


mass = [
    {"id":1,"name":"Andrii Soroka"},
    {"id":2,"name":"Uliana Soroka"}
]
parse_data_model = reqparse.RequestParser()
parse_data_model.add_argument('id',type=int)
parse_data_model.add_argument('login',type=str)
parse_data_model.add_argument('email',type=str)
parse_data_model.add_argument('password',type=str)

class User(Resource):
    def get(self,id):
        return mass[0]

    def put(self,id):
        return []

    def delete(self,id):
        return []


class UserList(Resource):
    def get(self):
        return mass

    def post(self):
        data = parse_data_model.parse_args()
        print(data)
        return []