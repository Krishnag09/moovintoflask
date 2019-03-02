from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://moovinto1:moovinto1234@moovinto1.cgvfbjj00kwe.us-east-1.rds.amazonaws.com/moovinto1'

db = SQLAlchemy(app)


@app.route("/")
def HelloWorld():
    return "Hello world"


# Product Class/Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


@app.route("/insertuser", methods=["POST"])
def userinsert():
    username = request.json['username']
    email = request.json['email']
    new_user = User(username, email)
    db.session.add(new_user)
    db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
