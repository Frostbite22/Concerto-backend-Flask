from src import app, db 
from datetime import datetime


class Show(db.Model):
    __tablename__ = 'shows'

    id = db.Column(db.Integer, primary_key=True)
    id_artist = db.Column(db.Integer,db.ForeignKey('artists.id'),nullable=False)
    id_venue = db.Column(db.Integer,db.ForeignKey('venues.id'),nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)


