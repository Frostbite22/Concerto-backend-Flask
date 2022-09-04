from flask import render_template, abort, url_for, jsonify, request
from src.models.Genre import Genre
from src.models.Artist import Artist,artist_genre
from src.models.Venue import Venue, venue_genre
from src.models.Show import Show
from typing import Optional



from src import app,db



@app.route('/')
def index():
    return "yoo" 

@app.route('/create/genre',methods=['GET', 'POST'])
def create_genre():
    json_object = request.json 
    name= json_object['name']
    genre = Genre(name=name)
    db.session.add(genre)
    db.session.commit()
    print(Genre.query.all())
    return jsonify({"response":"Genre has been created!"})

@app.route('/create/artist',methods=['GET', 'POST'])
def create_artist():
    json_object = request.json
    name= json_object['name']
    city = json_object['city']
    phone = json_object['phone']
    fb_link = json_object['fb_link']
    artist = Artist(name=name,city=city,phone=int(phone),fb_link=fb_link)
    genre = Genre.query.filter_by(name=json_object['genres']).first()
    artist.genres.append(genre)
    db.session.add(artist)
    db.session.commit()
    print(Artist.query.all())
    return jsonify({"response":"Artist has been created!"})

@app.route('/create/venue',methods=['GET', 'POST'])
def create_venue():
    json_object = request.json
    name= json_object['name']
    city = json_object['city']
    phone = json_object['phone']
    fb_link = json_object['fb_link']
    venue = Venue(name=name,city=city,phone=int(phone),fb_link=fb_link)
    genre = Genre.query.filter_by(name=json_object['genres']).first()
    venue.genres.append(genre)
    db.session.add(venue)
    db.session.commit()
    print(Venue.query.first().name)
    return jsonify({"response":"Venue has been created!"})

@app.route('/create/show',methods=['GET', 'POST'])
def create_show():
    json_object = request.json
    # artist_name= json_object['artist_name']
    # venue_name = json_object['venue_name']
    # start_time = json_object['start_time']
    # artist = Artist.query.filter_by(name=artist_name).first()
    # venue = Venue.query.filter_by(name=venue_name).first()
    artist_id = json_object['id_artist']
    id_venue = json_object['id_venue']
    start_time = json_object['start_time']

    show = Show(id_artist=artist_id,id_venue=id_venue,start_time=start_time)
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
    return all_data_json[table.__table__.name]

def to_dict_single(table,data,joined=None):
    table_cols = []
    table_cols += [column.key for column in table.__table__.columns]
    all_data_json = {table.__table__.name : []}
    data_json = {}
    for col in table_cols:
        data_json[col]=  getattr(data,col) 
    if(joined):
        print(getattr(data,joined.__table__.name))
        data_json[joined.__table__.name] = to_dict(joined,getattr(data,joined.__table__.name))
    all_data_json[table.__table__.name].append(data_json)
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


@app.route("/genre/<int:genre_id>")
def get_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    genre_json = to_dict_single(Genre,genre)  
    return jsonify({"genre":genre_json})


@app.route("/show/<int:show_id>")
def get_show(show_id):
    show = Show.query.get_or_404(show_id)
    show_json = to_dict_single(Show,show)  
    return jsonify({"show":show_json})


@app.route("/venue/<int:venue_id>")
def get_venue(venue_id):
    venue = Venue.query.get_or_404(venue_id)
    venue_json = to_dict_single(Venue,venue,Genre)  
    return jsonify({"venue":venue_json})


@app.route("/artist/<int:artist_id>")
def get_artist(artist_id):
    artist = Artist.query.get_or_404(artist_id)
    artist_json = to_dict_single(Artist,artist,Genre)  
    return jsonify({"artist":artist_json})

@app.route("/genre/<int:genre_id>/delete",methods=['POST','GET'])
def delete_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    try :
        db.session.delete(genre)
        db.session.commit()
    except:
        pass
    return jsonify({"genre":f"genre with id {genre_id} deleted"})

@app.route("/venue/<int:venue_id>/delete",methods=['POST','GET'])
def delete_venue(genre_id):
    venue = Venue.query.get_or_404(venue_id)
    try :
        db.session.delete(venue)
        db.session.commit()
    except:
        pass
    return jsonify({"venue":f"venue with id {venue_id} deleted"})

@app.route("/artist/<int:artist_id>/delete",methods=['POST','GET'])
def delete_artist(artist_id):
    artist = Artist.query.get_or_404(venue_id)
    try :
        db.session.delete(artist)
        db.session.commit()
    except:
        pass
    return jsonify({"artist":f"artist with id {artist_id} deleted"})

@app.route("/show/<int:show_id>/delete",methods=['POST','GET'])
def delete_show(show_id):
    artist = Artist.query.get_or_404(show_id)
    try :
        db.session.delete(show)
        db.session.commit()
    except:
        pass
    return jsonify({"show":f"show with id {show_id} deleted"})




