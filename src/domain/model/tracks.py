from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


@dataclass
class Track:
    id_: str
    title: str
    author: str
    date_played: datetime


def track_factory(title: str, author: str, date_played: datetime) -> Track:
    return Track(
        id_=str(uuid4()),
        title=title,
        author=author,
        date_played=date_played,
    )
