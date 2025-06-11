from flask import Blueprint, request, jsonify
from app import db, bcrypt
from app.models.user import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import datetime, timedelta
import random

auth_bp = Blueprint('auth', __name__)

# In-memory store for verification codes (for demo purposes)
verification_codes = {}

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    nom = data.get('nom')
    email = data.get('email')
    password = data.get('password')
    date_naissance_str = data.get('date_naissance')

    if not all([nom, email, password, date_naissance_str]):
        return jsonify({'msg': 'Missing required fields'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'msg': 'Email already registered'}), 400

    try:
        date_naissance = datetime.strptime(date_naissance_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'msg': 'Invalid date format'}), 400

    user = User(nom=nom, email=email, date_naissance=date_naissance)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    # Generate verification code
    code = str(random.randint(100000, 999999))
    verification_codes[email] = code
    # In real app, send code via email here
    print(f"Verification code for {email}: {code}")

    return jsonify({'msg': 'User registered. Verification code sent to email (simulated).'}), 201

@auth_bp.route('/verify_email', methods=['POST'])
def verify_email():
    data = request.get_json()
    email = data.get('email')
    code = data.get('code')

    if not all([email, code]):
        return jsonify({'msg': 'Missing email or code'}), 400

    expected_code = verification_codes.get(email)
    if expected_code and expected_code == code:
        verification_codes.pop(email)
        return jsonify({'msg': 'Email verified successfully'}), 200
    else:
        return jsonify({'msg': 'Invalid verification code'}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not all([email, password]):
        return jsonify({'msg': 'Missing email or password'}), 400

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1))
        return jsonify({'access_token': access_token, 'nom': user.nom}), 200
    else:
        return jsonify({'msg': 'Invalid credentials'}), 401

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # JWT tokens are stateless; implement token revocation if needed
    return jsonify({'msg': 'Logout successful'}), 200
