class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist 
        self.genre = genre 
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls):
          cls.genre_count = {}
          for genre in cls.genres:
                if genre in cls.genre_count:
                      cls.genre_count[genre] += 1
                else:
                      cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls):
          cls.artist_count = {}
          for artist in cls.artists:
                if artist in cls.artist_count:
                      cls.artist_count[artist] += 1
                else:
                      cls.artist_count[artist] = 1