from app import api
from app.api.users import User,UserList

api.add_resource(User,'/api/users/<int:id>')
api.add_resource(UserList,'/api/users')