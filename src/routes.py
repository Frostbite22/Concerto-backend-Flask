from flask import render_template, abort, url_for, jsonify
from src.models.Genre import Genre
from src.models.Artist import Artist,artist_genre
from src.models.Venue import Venue, venue_genre
from src.models.Show import Show

from src import app,db


@app.route('/')
def index():
    return "yoo" 

