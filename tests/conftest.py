import pytest

from extractor.song import Song


@pytest.fixture
def mon_everest():
    return Song("Mon Everest", "I spent my life climbing", ["Pop-Rap", "pop"])


@pytest.fixture
def toko_toko():
    return Song(
        "Toko Toko",
        "Est-ce que tu sens ce que je ressens",
        ["French Urban Pop/R&B", "French Rap"],
    )


@pytest.fixture
def closer():
    return Song(
        title="Closer",
        lyrics="We ain't ever getting older",
        genres=["Future bass", "pop"],
    )


@pytest.fixture
def glorious():
    return Song(
        title="Glorious",
        lyrics="I made through the darkest parts of the night",
        genres=["Hip-Hop/Rap"],
    )


@pytest.fixture
def danse_tal():
    return Song(
        title="Danse (feat. Flo Rida)",
        lyrics="La nuit vient de tomber, l'envie s'éveille en moi,...",
        genres=["Pop"],
    )
