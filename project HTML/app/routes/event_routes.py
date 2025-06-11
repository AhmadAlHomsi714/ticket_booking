from flask import Blueprint, request, jsonify
from app import db
from app.models.event import Event
from flask_jwt_extended import jwt_required

event_bp = Blueprint('event', __name__)

@event_bp.route('/', methods=['GET'])
def list_events():
    events = Event.query.all()
    result = []
    for e in events:
        result.append({
            'id': e.id,
            'titre': e.titre,
            'date': e.date.strftime('%Y-%m-%d'),
            'description': e.description,
            'capacite': e.capacite,
            'categorie': e.categorie
        })
    return jsonify(result), 200

@event_bp.route('/', methods=['POST'])
@jwt_required()
def add_event():
    data = request.get_json()
    titre = data.get('titre')
    date_str = data.get('date')
    description = data.get('description')
    capacite = data.get('capacite')
    categorie = data.get('categorie')

    if not all([titre, date_str, capacite]):
        return jsonify({'msg': 'Missing required fields'}), 400

    try:
        from datetime import datetime
        date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return jsonify({'msg': 'Invalid date format'}), 400

    event = Event(titre=titre, date=date, description=description, capacite=capacite, categorie=categorie)
    db.session.add(event)
    db.session.commit()

    return jsonify({'msg': 'Event added successfully'}), 201
