from src import db,app

class Genre(db.Model):
    __tablename__="genres"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(),nullable=False)

