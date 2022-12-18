from extractor.music_finder import MusicFinder
from extractor.song import SongList


def test_can_instantiate_music_finder():
    dummy_finding_method = lambda: SongList()

    music_finder = MusicFinder(dummy_finding_method)

    assert music_finder.music_finding_method == dummy_finding_method


def test_music_finder_can_find_music(
    mon_everest, toko_toko, closer, glorious, danse_tal
):
    dummy_finding_method = lambda n: SongList(
        [mon_everest, toko_toko, closer, glorious, danse_tal]
    )
    music_finder = MusicFinder(dummy_finding_method)

    result = music_finder.find_music(number_of_songs=5)

    assert isinstance(result, SongList), f"find_music should return a SongList"
    assert len(result) == 5
    assert result._song_list == [mon_everest, toko_toko, closer, glorious, danse_tal]
