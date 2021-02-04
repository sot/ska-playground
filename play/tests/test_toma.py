import pytest

from play.toma import has_toma


def test_has_toma():
    assert has_toma('blatOmac')
    assert not has_toma('blatomic')


def test_has_toma_validation():
    with pytest.raises(TypeError, match='value must be a str'):
        has_toma(10)
