from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, \
    BadSignature, SignatureExpired
from pymongo import MongoClient
from config import MongoConfig
from flask import current_app

mongo_config = MongoConfig()
mongo = MongoClient(mongo_config.MONGO_URI)
db = mongo['flask_rest']
collection = db['users']


class User:
    def __init__(self, username=None, email=None, password=None):
        self.password = password
        self.username = username
        self.email = email
        self.confirmed = False
        self.is_active = False

    def __dict__(self):
        return dict(username=self.username,
                    password=self.password_hash,
                    email=self.email)

    @property
    def password(self):
        raise AttributeError('Password is not readable attribute')

    @password.setter
    def password(self, password):
        if password is not None:
            self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self):
        s = Serializer(current_app.config['SECRET_KEY'],
                       expires_in=86400)
        return s.dumps({'confirm': self.username})

    def verify_token(self, token):
        s = Serializer(current_app.config['SECRET_KEY'],
                       expires_in=86400)
        try:
            data = s.loads(token)
        except BadSignature:
            return False
        except SignatureExpired:
            return False
        user = collection.find_one({'username': data.get('confirm')})
        self.username = user['username']
        self.password_hash = user['password']
        self.email = user['email']
        return self
