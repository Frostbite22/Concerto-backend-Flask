from src import app, db 


venue_genre = db.Table('venue_genre',
    db.Column('venue_id', db.Integer, db.ForeignKey('venues.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True)
)
class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String())
    phone = db.Column(db.Integer,nullable=False)
    fb_link = db.Column(db.String())
    genres = db.relationship('Genre',backref=db.backref('venues', lazy=True),secondary= venue_genre)

