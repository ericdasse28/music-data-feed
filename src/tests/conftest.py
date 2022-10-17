import pytest
from domain.ports.extract import MusicExtractorService


class FakeMusicExtractorServiceAdapter(MusicExtractorService):
    def get_recently_played_tracks(self, number_of_tracks):
        return []


@pytest.fixture
def fake_music_extractor():
    return FakeMusicExtractorServiceAdapter()
