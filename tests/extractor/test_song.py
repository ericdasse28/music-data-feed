"""This module tests features related to songs"""

import pytest
from extractor.song import Song


@pytest.mark.parametrize(
    "song_title, song_lyrics, song_genres",
    [
        ("Mon Everest", "Blablablabla", ["Pop-Rap", "pop"]),
        (
            "Finesse",
            "Elle me dit qu'elle aime quand on fait ça en finesse, que je suis son anti-stress",
            ["R&B", "new jack swing"],
        ),
        (
            "Toko Toko",
            "Tu me fais penser à moi, ...",
            ["French Urban Pop/R&B", "French Rap"],
        ),
    ],
)
def test_can_create_a_song(song_title, song_lyrics, song_genres):
    song = Song(title=song_title, lyrics=song_lyrics, genres=song_genres)

    assert song.title == song_title
    assert song.lyrics == song_lyrics
    assert song.genres == song_genres
