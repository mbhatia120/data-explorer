from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db



user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [user.to_dict() for user in users]
    return jsonify({"users": users_list})

@user_bp.route('/users', methods=['POST'])
def create_or_get_user():
    data = request.get_json()  

    if 'username' not in data:
        return jsonify({'error': 'Username link are required'}), 400

    username = data['username']

    # Check if the user already exists
    existing_user = User.query.filter_by(username=username).first()

    if not existing_user:
        
        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()  
        id = new_user.id
        message = 'New user created successfully!'
    else:
        
        user_id = existing_user.user_id
        message = 'User already exists.'

    return jsonify({
        'message': message,
        'user': {
            'user_id': id,
            'username': username,
        }
    }), 201 if not existing_user else 200 