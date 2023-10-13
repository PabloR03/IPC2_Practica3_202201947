from Movie import Movie
import json

class Movie_DAO:
    def __init__(self):
        self.movies = []
        self.movield_counter = 1

    def new_movie(self, name, genre, year):
        for movie in self.movies:
            if movie.name == name:
                return False
        new = Movie(self.movield_counter, name, genre, year)
        self.movies.append(new)
        print("New movie added: ", new.dump())
        self.movield_counter += 1
        return True
    
    def movie_by_genre(self, genre):
        return json.dumps([Movie.dump() for Movie in self.movies if Movie.genre == genre], indent=4)
    
    def movie_by_year(self, year):
        return json.dumps([Movie.dump() for Movie in self.movies if Movie.year == year], indent=4)
        
    def update_movie(self, name, genre, year):
        for movie in self.movies:
            if movie.name == name:
                if genre is not None:
                    movie.genre = genre
                if year is not None:
                    movie.year = year
                return True
        return False
