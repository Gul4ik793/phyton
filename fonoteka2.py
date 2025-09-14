class Song:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def get_list_author(self):
        return self.author

    def get_song_name(self):
        return self.name

class Album:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.list_songs = []

    def add_list_songs(self, song):
        self.list_songs.append(song)

    def get_name(self, name):
        for song in self.list_songs:
            if song.name == name:
                return f"Песня '{name}' содержится в альбоме", True
        return f"Песня '{name}' отсутствует в альбоме", False

    def get_song_name(self):
        return [song.name for song in self.list_songs]

    def get_list_author(self):
        return [song.author for song in self.list_songs]

    def get_unique_author(self):
        return list(set(self.get_list_author()))

    def get_list_song_author(self, author_name):
        unique_songs = set()

        for album in self.list_songs:
            if album.get_list_author() == author_name:
                songs = album.get_song_name()
                unique_songs.add(songs)
        return list(set(unique_songs))

class Fonoteka:
    def __init__(self, name):
        self.name = name
        self.list_album = []

    def add_list_album(self, album):
        self.list_album.append(album)

    def get_list_album_name(self):
        return [album.name for album in self.list_album]

    def get_list_song_author(self, author_name):
        unique_songs = set()

        for album in self.list_album:
            songs = album.get_list_song_author(author_name)
            unique_songs = list(unique_songs) + songs
        return list(unique_songs)

    def get_common_song(self):
        if not self.list_album:
            return []
        sets_of_song = [set(album.get_song_name()) for album in self.list_album]
        common_song = set.intersection(*sets_of_song)
        return common_song


song_one = Song("Песня 1", "Автор 1", 2001)
song_two = Song("Песня 2", "Автор 1", 2002)
song_three = Song("Песня 3", "Автор 3", 2003)
song_four = Song("Песня 4", "Автор 2", 2004)

album_one = Album("Альбом 1", 2005)
album_two = Album("Альбом 2", 2006)
album_three = Album("Альбом 3", 2007)
album_four = Album("Альбом 4", 2008)

fonoteka = Fonoteka("Фонотека")

album_one.add_list_songs(song_one)
album_one.add_list_songs(song_two)
album_two.add_list_songs(song_two)
album_two.add_list_songs(song_one)
album_three.add_list_songs(song_two)
album_three.add_list_songs(song_one)
album_four.add_list_songs(song_two)
album_four.add_list_songs(song_one)

fonoteka.add_list_album(album_one)
fonoteka.add_list_album(album_two)
fonoteka.add_list_album(album_three)
fonoteka.add_list_album(album_four)

print("Все песни Альбома 1:", album_one.get_song_name())
print("Все авторы Альбома 1:", album_one.get_unique_author())

print("Все песни Альбома 2:", album_two.get_song_name())
print("Все авторы Альбома 2:", album_two.get_unique_author())

print(f"Ищем песню в {album_one.name}:", album_one.get_name("Песня 1"))
print(f"Ищем песню в {album_one.name}:", album_one.get_name("Песня 4"))

print("Все песни Автора 1 в Фонотеке:", set(fonoteka.get_list_song_author("Автор 1")))

print(f"Песня (песни) {fonoteka.get_common_song()} содержится во всех альбомах")

