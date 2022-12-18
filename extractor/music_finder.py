class MusicFinder:
    def __init__(self, music_finding_method: function):
        self.music_finding_method = music_finding_method

    def find_music(self, number_of_songs: int):
        return self.music_finding_method(number_of_songs)
