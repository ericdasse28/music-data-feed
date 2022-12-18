"""This module tests features related to songs"""

import pytest
from extractor.song import Song, SongList


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
def test_can_add_a_song_to_an_empty_song_list(song_title, song_lyrics, song_genres):
    song = Song(title=song_title, lyrics=song_lyrics, genres=song_genres)
    song_list = SongList()
    former_song_list_length = len(song_list._song_list)

    song_list.add(song)

    assert len(song_list._song_list) == former_song_list_length + 1
    assert song in song_list


def test_can_add_a_song_to_a_song_list_that_already_contains_songs(
    mon_everest, glorious, closer
):
    song_list = SongList()
    song_list._song_list = [
        glorious,
        closer,
    ]
    former_song_list_length = len(song_list._song_list)

    song_list.add(mon_everest)

    assert len(song_list._song_list) == former_song_list_length + 1
    assert mon_everest in song_list


def test_song_list_is_empty_property_returns_true_when_song_list_is_empty():
    song_list = SongList()

    assert song_list.is_empty


def test_song_list_is_empty_property_returns_false_when_song_list_is_not_empty():
    song_list = SongList()
    song_list._song_list = [
        Song(
            title="Determinate",
            lyrics="Determinate, determinate, ...",
            genres=["Pop punk"],
        )
    ]

    assert not song_list.is_empty
