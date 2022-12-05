from random import randint


def test_can_get_recently_played_tracks_from_music_extraction_service(
    fake_music_extractor,
):
    number_of_tracks = randint(0, 100)

    tracks = fake_music_extractor.get_recently_played_tracks(
        number_of_tracks=number_of_tracks
    )

    assert tracks == []


def test_returned_number_of_tracks_is_a_list(fake_music_extractor):
    number_of_tracks = randint(0, 100)

    tracks = fake_music_extractor.get_recently_played_tracks(
        number_of_tracks=number_of_tracks
    )

    assert type(tracks) == list