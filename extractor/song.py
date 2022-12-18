class Song:
    def __init__(self, title, lyrics, genres):
        self.title = title
        self.lyrics = lyrics
        self.genres = genres

    def __eq__(self, other_song):
        return (
            self.title == other_song.title
            and self.lyrics == other_song.lyrics
            and self.genres == other_song.genres
        )


class SongList:
    def __init__(self):
        self._song_list = []

    def add(self, song):
        self._song_list = [song]

    def __contains__(self, song):
        return song in self._song_list


# TODO: MusicFinder
