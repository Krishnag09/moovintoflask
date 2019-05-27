from flask import Flask
from flask_mail import Mail
from flask_restful import Api

from config import config
from resources import SignUp, Login, Dashboard


mail = Mail()


def init_app():
    app = Flask(__name__)
    api = Api(app)
    mail.init_app(app)
    app.config.from_object(config['default'])
    config['default'].init_app(app)
    return app, api


app, api = init_app()

api.add_resource(SignUp, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Dashboard, '/')


if __name__ == '__main__':
    app.run(debug=True)
