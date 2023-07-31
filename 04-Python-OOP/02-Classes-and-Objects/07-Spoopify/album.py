from song import Song


class Album:

    def __init__(self, name: str, *args):
        self.name = name
        self.published = False
        self.songs = [x for x in args]

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return 'Cannot add songs. Album is published.'
        if song in self.songs:
            return 'Song is already in the album.'
        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        song = [x for x in self.songs if x.name == song_name]
        if not song:
            return 'Song is not in the album.'
        if self.published:
            return 'Cannot remove songs. Album is published.'
        self.songs.remove(song[0])
        return f'Removed song {song_name} from album {self.name}.'

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'
        self.published = True
        return f'Album {self.name} has been published.'

    def details(self):
        album_info = [f'Album {self.name}']
        for s in self.songs:
            album_info.append(f'== {s.get_info()}')
        nl = '\n'
        return f'{nl.join(album_info)}'