import sys

# The shutil.disk_usage is available since Python 3.3,
# but in other versions, we need to use psutil.disk_usage to replace it.
# (For Synology's compatibility; there is no psutil in Python 3 in Synology)
SUPPORT_SHUTIL = sys.version_info >= (3, 3, 0)

def disk_usage_(path):
    du = None

    if SUPPORT_SHUTIL:
        import shutil
        du = shutil.disk_usage(path)
    else:
        import psutil
        du = psutil.disk_usage(path)

    # Unified format
    return {
        'total': du.total,
        'used': du.used,
        'free': du.free,
    }
