class Song:
    songs = []
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}
    count = 0

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        Song.songs.append(self)

        Song.genres.add(genre)
        Song.artists.add(artist)
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1

        Song.count += 1
