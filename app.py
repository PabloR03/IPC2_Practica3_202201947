from flask import Flask
from flask_cors import CORS
from Movie_DAO import Movie_DAO
from flask.globals import request
from flask.json import jsonify

movie_handler = Movie_DAO()
app = Flask(__name__)
CORS(app)

movie_handler.new_movie("Kung Fu Panda 1", "Adventure", "2011")
movie_handler.new_movie("Kung Fu Panda 2", "Adventure", "2012")
movie_handler.new_movie("Kung Fu Panda 3", "Adventure", "2020")
movie_handler.new_movie("FF 4", "Action", "2014")
movie_handler.new_movie("FF 5", "Action", "2015")
movie_handler.new_movie("FF 6", "Action", "2020")
movie_handler.new_movie("Chuky 7", "Horror", "2017")
movie_handler.new_movie("Chuky 8", "Horror", "2018")
movie_handler.new_movie("Chuky 9", "Horror", "2020")



@app.route("/")
def index():
    return "<h1> Pablo Andres Rodriguez Lima - 202201947 </h1>"

@app.route("/api/add-movie", methods=['POST'])
def add_movie():
    response = {}
    name = request.json['name']
    genre = request.json['genre']
    year = request.json['year']
    if movie_handler.new_movie(name, genre, year):
        response = {
            "success": True,
            "message": "Pelicula agregada exitosamente"
        }
        return response
    else:
        response = {
            "success": False,
            "message": "La pelicula ya existe"
        }
        return response

@app.route("/api/movies-by-genre/<genre>", methods=['GET'])
def movie_by_genre(genre):
    return movie_handler.movie_by_genre(genre)

@app.route("/api/movies-by-year/<year>", methods=['GET'])
def movie_by_year(year):
    return movie_handler.movie_by_year(year)

@app.route("/api/update-movie", methods=['PUT'])
def update_movie():
    response = {}
    data = request.json

    name = data.get('name', None)
    genre = data.get('genre', None)
    year = data.get('year', None)

    if name is not None:
        for movie in movie_handler.movies:
            if movie.name == name:
                if genre is not None:
                    movie.genre = genre
                if year is not None:
                    movie.year = year
                response = {
                    "success": True,
                    "message": "Película actualizada exitosamente"
                }
                return jsonify(response)

    response = {
        "success": False,
        "message": "La película no se encontró o no se proporcionaron datos de actualización"
    }
    return jsonify(response)



if __name__ == "__main__":
    app.run(threaded=True, port=5000,debug=True)