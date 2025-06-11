from flask import Blueprint, request, jsonify
from app import db
from app.models.booking import Booking
from app.models.event import Event
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/', methods=['POST'])
@jwt_required()
def create_booking():
    user_id = get_jwt_identity()
    data = request.get_json()
    event_id = data.get('event_id')
    quantity = data.get('quantity', 1)

    if not event_id:
        return jsonify({'msg': 'Event ID is required'}), 400

    event = Event.query.get(event_id)
    if not event:
        return jsonify({'msg': 'Event not found'}), 404

    booking = Booking(user_id=user_id, event_id=event_id, statut='confirmed', date_reservation=datetime.utcnow())
    db.session.add(booking)
    db.session.commit()

    return jsonify({'msg': 'Booking created successfully'}), 201

@booking_bp.route('/', methods=['GET'])
@jwt_required()
def get_user_bookings():
    user_id = get_jwt_identity()
    bookings = Booking.query.filter_by(user_id=user_id).all()
    result = []
    for b in bookings:
        result.append({
            'id': b.id,
            'event_id': b.event_id,
            'event_titre': b.event.titre,
            'statut': b.statut,
            'date_reservation': b.date_reservation.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(result), 200
