from flask import render_template, abort, url_for, jsonify
from src.models.Genre import Genre
from src.models.Artist import Artist,artist_genre
from src.models.Venue import Venue, venue_genre
from src.models.Show import Show
from typing import Optional



from src import app,db



@app.route('/')
def index():
    return "yoo" 

@app.route('/create/genre')
def create_genre():
    json_object = {
        'name' : 'Jazz'
    }
    name= json_object['name']
    genre = Genre(name=name)
    db.session.add(genre)
    db.session.commit()
    print(Genre.query.all())
    return jsonify({"response":"Genre has been created!"})

@app.route('/create/artist')
def create_artist():
    json_object = {
        'name' : 'Yoshiki',
        'city' : 'Tokyo',
        'phone' : '55614412',
        'fb_link' :'fb/eve',
        'genre' : 'City Pop'
    }
    name= json_object['name']
    city = json_object['city']
    phone = json_object['phone']
    fb_link = json_object['fb_link']
    artist = Artist(name=name,city=city,phone=int(phone),fb_link=fb_link)
    genre = Genre.query.filter_by(name=json_object['genre']).first()
    artist.genres.append(genre)
    db.session.add(artist)
    db.session.commit()
    print(Artist.query.all())
    return jsonify({"response":"Artist has been created!"})

@app.route('/create/venue')
def create_venue():
    json_object = {
        'name' : 'ellou7',
        'city' : 'tunis',
        'phone' : '55614412',
        'fb_link' :'fb/lou7a',
        'genre' : 'Jazz'
    }
    name= json_object['name']
    city = json_object['city']
    phone = json_object['phone']
    fb_link = json_object['fb_link']
    venue = Venue(name=name,city=city,phone=int(phone),fb_link=fb_link)
    genre = Genre.query.filter_by(name=json_object['genre']).first()
    venue.genres.append(genre)
    db.session.add(venue)
    db.session.commit()
    print(Venue.query.first().name)
    return jsonify({"response":"Venue has been created!"})

@app.route('/create/show')
def create_show():
    json_object = {
        'artist_name' : 'EVE',
        'venue_name' : 'ellou7',
        'start_time' : '1998-10-25 21:00:00'
    }
    artist_name= json_object['artist_name']
    venue_name = json_object['venue_name']
    start_time = json_object['start_time']
    artist = Artist.query.filter_by(name=artist_name).first()
    venue = Venue.query.filter_by(name=venue_name).first()

    show = Show(id_artist=artist.id,id_venue=venue.id,start_time=start_time)
    db.session.add(show)
    db.session.commit()
    print(Show.query.first().start_time)
    return jsonify({"response":"Show has been created!"})


def to_dict(table,data,joined=None):
    table_cols = []
    table_cols += [column.key for column in table.__table__.columns]
    all_data_json = {table.__table__.name : []}
    for element in data:
        data_json = {}
        for col in table_cols:
            data_json[col]=  getattr(element,col) 
        if(joined):
            print(getattr(element,joined.__table__.name))
            data_json[joined.__table__.name] = to_dict(joined,getattr(element,joined.__table__.name))
        all_data_json[table.__table__.name].append(data_json)
    print(all_data_json)
    return all_data_json[table.__table__.name]


@app.route('/artists')
def get_artists():
    artists = Artist.query.all()
    artists_json = to_dict(Artist,artists,Genre)
    return jsonify({"artists":artists_json})

@app.route('/genres')
def get_genres():
    genres = Genre.query.all()
    genres_json = to_dict(Genre,genres)   
    return jsonify({"genres":genres_json})

@app.route('/venues')
def get_venues():
    venues = Venue.query.all()
    venues_json = to_dict(Venue,venues,Genre)   
    return jsonify({"venues":venues_json})

@app.route('/shows')
def get_shows():
    shows = Show.query.all()
    shows_json = to_dict(Show,shows)   
    return jsonify({"shows":shows_json})

