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

    def __str__(self) -> str:
        return f"Song(title={self.title}, lyrics={self.lyrics:15}, genres={self.genres}"


class SongList:
    def __init__(self):
        self._song_list = []

    @property
    def is_empty(self):
        if not self._song_list:
            return True
        return False

    def add(self, song):
        self._song_list.append(song)

    def __contains__(self, song):
        return song in self._song_list

    def __str__(self) -> str:
        return str(self._song_list)


# TODO: MusicFinder
