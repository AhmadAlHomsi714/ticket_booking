from app import db
from datetime import datetime

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(128), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text)
    capacite = db.Column(db.Integer, nullable=False)
    categorie = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
