def urlparse_(url):
    try: # for Python 3
        from urllib.parse import urlparse
    except ImportError: # for Python 2.7
        from urlparse import urlparse

    return urlparse(url)