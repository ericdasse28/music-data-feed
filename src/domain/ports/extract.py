from abc import ABC, abstractmethod
from typing import List

from domain.model.tracks import Track


class MusicExtractorService(ABC):
    @abstractmethod
    def get_recently_played_tracks(self) -> List[Track]:
        ...
