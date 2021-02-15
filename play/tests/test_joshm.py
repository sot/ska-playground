import pytest

from play.joshm import has_joshm


def test_has_joshm():
    assert has_joshm('Ex')



def test_has_joshm_validation():
    with pytest.raises(ValueError, match='parrot must be \'Ex\''):
        has_joshm('alive')
