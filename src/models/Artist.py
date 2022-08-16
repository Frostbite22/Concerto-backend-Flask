from src import app, db 

artist_genre = db.Table('artist_genre',
    db.Column('artist_id', db.Integer, db.ForeignKey('artists.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True)
)

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String())
    phone = db.Column(db.Integer,nullable=False)
    fb_link = db.Column(db.String())
    genres = db.relationship('Genre',backref=db.backref('artists', lazy=True),secondary= artist_genre)
