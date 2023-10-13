class Movie:
    def __init__(self,movield, name, genre, year):
        self.movield = movield
        self.name = name
        self.genre = genre
        self.year = year
    
    def dump(self):
        return {
            'movield': self.movield,
            'name': self.name,
            'genre': self.genre,
            'year': self.year
        }