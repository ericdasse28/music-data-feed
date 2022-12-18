class MusicFinder:
    def __init__(self, music_finding_method: function):
        self.music_finding_method = music_finding_method

    def find_music(self, number_of_songs: int):
        if not isinstance(number_of_songs, int) or number_of_songs < 0:
            raise AttributeError(
                "find_music argument should be an integer greater than or equal to 0"
            )
        return self.music_finding_method(number_of_songs)
