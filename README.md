# Ska playground

This is a fun place to practice making pull requests and doing very basic
Python development.

## Cloning this repo

...

## Practice suggestions

You can add anything you want in this repo. However, if there are multiple
people working on the same file at once then there might be merge conflicts.

Instead, just add a new Python module with a function using a unique version of
your name.  For instance see these existing files in the `play` directory and
make your own new module following that model. Substitute
`<first_name><last_initial>` for `toma`.

If you aren't sure what to do, just start by copying each of those files but
with your own unique name. Edit the function and the tests to your desire.
```
cp play/toma.py play/<yourname>.py
```

Now edit your module and make it do something different, maybe more interesting.

### Interactive play

Often you are going start by playing with a new function interactively. For
instance:

```
ipython

In [1]: from play import toma  # <yourname>

In [2]: toma.has_toma(1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-6f7036f4e705> in <module>
----> 1 toma.has_toma(1)

~/git/ska-playground/play/toma.py in has_toma(value)
      1 def has_toma(value):
      2     if not isinstance(value, str):
----> 3         raise TypeError(f'value must be a str, got {type(value)} instead')
      4
      5     out = 'toma' in value.lower()

TypeError: value must be a str, got <class 'int'> instead

In [3]: toma.has_toma('tom')
Out[3]: False

In [4]: toma.has_toma('toma')
Out[4]: True
```

### Testing

When you think it is working, run the tests. Maybe you are a star and already
wrote them, but most mortals write the code and then the tests.

Frequently there will already be some existing test files. In this case you
can copy an existing one and modify.
```
cp play/tests/test_toma.py play/tests/test_<yourname>.py
```

Now edit `play/tests/test_<yourname>.py` and adapt so the tests work for your
function.

Finally do the tests:
```
pytest play -v  # or --verbose
# OR
python setup.py test --args='-v'
```

If there is a failure that you want to debug you can do:
```
pytest play -v --pdb
# OR
python setup.py test --args='-v --pdb'
```
