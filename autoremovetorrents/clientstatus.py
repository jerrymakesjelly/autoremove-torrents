from .util.convertbytes import convert_bytes
from .util.convertspeed import convert_speed

class ClientStatus(object):
    def __init__(self):
        # Proper attributes:
        # free_space, total_download_speed, total_upload_speed, etc.
        #
        # Note:
        # The type of free_space is a function because we need to specific a
        # directory to check its free space.
        pass

    # Format client status info
    def __str__(self):
        # Attribute Formater
        def disp(prop, converter = None):
            if hasattr(self, prop):
                attr = getattr(self, prop)
                if converter is not None:
                    return converter(attr)
            else:
                return '(Not Provided)'

        return ('Status reported by the client: \n' +
            '\tDownload Speed: %s\tTotal: %s\n' +
            '\tUpload Speed: %s\tTotal: %s\n' +
            '\tOutgoing Port Status: %s') % \
            (
                disp('download_speed', convert_speed),
                disp('total_downloaded', convert_bytes),
                disp('upload_speed', convert_speed),
                disp('total_uploaded', convert_bytes),
                disp('port_status', lambda s: s.name),
            )
