from flask import Blueprint, request, jsonify
from app.models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "User already exists"}), 400
    new_user = User(email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()

    # Create an empty portfolio for the user
    from app.models import Portfolio
    db.session.add(Portfolio(user_id=new_user.id))
    db.session.commit()

    return jsonify({"message": "User registered successfully"})

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email'], password=data['password']).first()
    if user:
        return jsonify({"message": "Login successful", "user_id": user.id})
    return jsonify({"error": "Invalid credentials"}), 401
