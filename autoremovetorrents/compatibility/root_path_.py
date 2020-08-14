def root_path(path):
    try: # for Python 3
        from pathlib import Path
        return Path(path).parts[0]
    except ImportError: # for Python 2.7
        import os
        dirname = os.path.dirname(path)
        return dirname if dirname != '' else path
        
