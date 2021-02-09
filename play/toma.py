def has_toma(value):
    if not isinstance(value, str):
        raise TypeError(f'value must be a str dude!, got {type(value)} instead')

    out = 'toma' in value.lower()
    return out
