from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'renters'
app.config["MONGO_URI"] = "mongodb://localhost:27017/renters"
mongo = PyMongo(app)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.json['username']})

        if existing_user is None:
            users.insert({'name': request.json['username'], 'email': request.json['email']})
            return 'Welcome to Moovinto'
        else:
            return 'That username already exists!'


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
