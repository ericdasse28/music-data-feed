from abc import ABCMeta, abstractmethod


class MusicExtractorService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_recently_played_tracks(self, number_of_tracks):
        pass
