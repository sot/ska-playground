import pytest

from play.jamesk import knockknock
from play.jamesk import text2morse
from contextlib import redirect_stdout
import io
import re


def test_knockknock():
    # redirect stdout to a string stream
    stream = io.StringIO()
    with redirect_stdout(stream):
        # exercise the function
        knockknock()
    # evaluate the results
    full_joke = stream.getvalue()
    stream.close()

    pattern = re.compile(
        r"""Knock\sKnock...\r?\n
        \t\tWho's\sthere\?\r?\n
        ([^\r\n]+)\r?\n
        \t\t(\w+)\swho\?\r?\n
        ([^\r\n]+)\r?\n""", re.VERBOSE)
    match = pattern.search(full_joke)
    # 3 groups are expected
    assert len(match.groups()) == 3
    whos_there = match.group(1)
    # the first two are the same
    assert whos_there == match.group(2)
    # the first one should be a key in the jokes dict
    assert whos_there in knockknock.jokes
    # the third should be the matching value
    assert match.group(3) == knockknock.jokes[whos_there]


def test_text2morse_default():
    # test default text2morse behavior

    expected_str = '.... . .-.. .-.. ---        .-- --- .-. .-.. -..'
    # exercise the code
    actual_str = text2morse()
    # check the results
    assert actual_str == expected_str


def test_text2morse():
    # test text2morse

    expected_str = '.... .- .--. .--. -.--        -.. .- -.--'
    # exercise the code
    actual_str = text2morse("Happy Day")
    # check the results
    assert actual_str == expected_str


def test_text2morse_astrik():
    # test that an astrik returns the appropriate error
    with pytest.raises(ValueError,
                       match="'*' cannot be converted to morse code."):
        text2morse("All *.py")
