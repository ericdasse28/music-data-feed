from typing import List


class Song:
    def __init__(self, title: str, lyrics: str, genres: List[str]):
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
    def __init__(self, song_list=None):
        if not song_list:
            self._song_list = []
        elif self._is_list_of_songs(song_list):
            self._song_list = song_list
        else:
            raise TypeError(
                "SongList optional argument should be a list of objects of type Song"
            )

    def _is_list_of_songs(self, song_list):
        return isinstance(song_list, list) and all(
            isinstance(element, Song) for element in song_list
        )

    @property
    def is_empty(self):
        if not self._song_list:
            return True
        return False

    def add(self, song: Song):
        self._song_list.append(song)

    def __contains__(self, song: Song):
        return song in self._song_list

    def __str__(self) -> str:
        return str(self._song_list)

    def __len__(self):
        return len(self._song_list)
