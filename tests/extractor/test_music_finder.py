from extractor.music_finder import MusicFinder
from extractor.song import SongList


def test_can_instantiate_music_finder():
    dummy_finding_method = lambda: SongList()

    music_finder = MusicFinder(dummy_finding_method)

    assert music_finder.music_finding_method == dummy_finding_method
