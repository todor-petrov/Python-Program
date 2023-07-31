from album import Album
from song import Song


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, al: Album):
        if al in self.albums:
            return f'Band {self.name} already has {al.name} in their library.'
        self.albums.append(al)
        return f'Band {self.name} has added their newest album {al.name}.'

    def remove_album(self, album_name: str):
        al = [x for x in self.albums]
        if not al:
            return f'Album {album_name} is not found.'
        if al[0].published:
            return 'Album has been published. It cannot be removed.'
        self.albums.remove(al[0])
        return f'Album {album_name} has been removed.'

    def details(self):
        band_info = [f'Band {self.name}']
        for al in self.albums:
            band_info.append(al.details())
        nl = '\n'
        return f'{nl.join(band_info)}'


# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())
