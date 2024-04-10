from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'hitc_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def json(self):
        return {'id': self.id, 'username': self.username, 'email': self.email, 'age': self.age}

with app.app_context():
    db.create_all()

# Headinthe clouds test route
@app.route('/hello', methods=['GET'])
def test():
    return make_response(jsonify({'message': 'hey there! welcome to the headintheclouds community! :)'}), 200)

# Create a user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'], age=data['age'])
        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify({'message': 'user successfully created!'}), 201)
    except Exception as e:
        return make_response(jsonify({'message': 'oops! something went wrong while creating user.'}), 500)

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return make_response(jsonify({'message': 'all users fetched successfully', 'users': [user.json() for user in users]}), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'oops! something went wrong while fetching users.'}), 500)

# Get a user by id
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            return make_response(jsonify({'message': 'user found!', 'user': user.json()}), 200)
        return make_response(jsonify({'message': 'user not found.'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'oops! something went wrong while fetching user.'}), 500)

# Update a user by id
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.username = data['username']
            user.email = data['email']
            user.age = data['age']  
            db.session.commit()
            return make_response(jsonify({'message': 'user details successfully updated!'}), 200)
        return make_response(jsonify({'message': 'user not found.'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'oops! Something went wrong while updating user details.'}), 500)

# Delete a user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({'message': 'user successfully deleted!'}), 200)
        return make_response(jsonify({'message': 'user not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'oops! Something went wrong while deleting user.'}), 500)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)