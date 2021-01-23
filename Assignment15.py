#----------Assignment 15 - Movie Collection----------#

class Movie:
    def __innit__(self, title, song)
        self.title = title
        self.song = song

    def __repr__(self):
       return 'Movie(title=%s, song=%s)' % (self.title, self.song)

    def __str__(self):
       return 'Movie(title=%s, song=%s)' % (self.title, self.song)


class Song:
    def __innit__(self, name, singer, composer)
        self.name = name
        self.singer = singer
        self.composer = composer

    def __repr__(self):
       return 'Song(name=%s, singer=%s, composer=%s)' % (self.name, self.singer, self.composer)

    def __str__(self):
       return 'Song(name=%s, singer=%s, composer=%s)' % (self.name, self.singer, self.composer)



song_1 = Song("Sunflower" , "Post Malone" , "Swae Lee")
song_2 = Song("Wolves" , "Post Malone" , "Big Sean")
song_3 = Song("Unforgettable" , "French Montana" , "Swae Lee")

movie_1 = Movie("Spider-Man: Into the Spider-Verse" , song_1)
movie_2 = Movie("Avatar" , song_2)
movie_3 = Movie("Mission Impossible" , song_3)


movie_songs = [song_1, song_2, song_3]
total_count_of_movie_songs = movie_songs.count_name()

print("Total number of movie songs: ", total_count_of_movie_songs)

