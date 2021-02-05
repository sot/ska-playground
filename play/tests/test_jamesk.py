import pytest

from play.jamesk import knockknock

def test_knockknock():
    import sys
    import io
    import re

    # redirect stdout to a string stream
    stream = io.StringIO()
    sys.stdout = stream
    # exercise the function
    knockknock()
    # restore the stdout
    sys.stdout = sys.__stdout__
    # evaluate the results
    full_joke = stream.getvalue()
    stream.close()
    pattern = re.compile(r"Knock Knock...\n\t\tWho's there\?\n([^\n]+)\n\t\t([\w]+) who\?\n([^\n]+)\n")
    match = pattern.search(full_joke)
    assert len(match.groups()) == 3
    assert match.group(1) == match.group(2)
    assert match.group(1) in knockknock.jokes
    assert match.group(3) == knockknock.jokes[match.group(1)]
