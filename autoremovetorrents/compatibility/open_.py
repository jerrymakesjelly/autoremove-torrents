def open_(name, mode='r', **kwargs):
    try: # for Python 3
        return open(name, **kwargs)
    except TypeError: # for Python 2.7
        import io
        return io.open(name, **kwargs)