from flask import g
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, reqparse

from model.user import User, collection

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)


auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username_or_token, password):
    user = User().verify_token(username_or_token)
    if user:
        g.user = user
        return True
    elif not user:
        data = collection.find_one({
            'username': username_or_token}
            )
        user = User(username=data['username'], email=data['email'])
        user.password_hash = data['password']
        if user.verify_password(password):
            g.user = user
            return True
    return False


class Login(Resource):

    def __init__(self):
        Resource.__init__(self)
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username')
        self.parser.add_argument('passwd')
        self.parser.add_argument('token')

    @auth.login_required
    def post(self):
        user = g.user
        return {'token': user.generate_auth_token().decode('utf-8')}


class SignUp(Resource):

    def __init__(self):
        Resource.__init__(self)
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username')
        self.parser.add_argument('passwd')
        self.parser.add_argument('email')

    def post(self):
        args = self.parser.parse_args()
        user = User(username=args.username,
                    password=args.passwd,
                    email=args.email)
        if collection.find_one({'username': user.username}) or \
                collection.find_one({'email': user.email}):
            return {'error': 'This username or email is already taken'}
        collection.insert_one(user.__dict__())
        return {'success': {'username': user.username}}


class Dashboard(Resource):

    @auth.login_required
    def get(self):
        user = g.user
        return {'hello': user.username}
