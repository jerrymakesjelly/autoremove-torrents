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
                disp('download_speed', self._convert_speed),
                disp('total_downloaded', self._convert_bytes),
                disp('upload_speed', self._convert_speed),
                disp('total_uploaded', self._convert_bytes),
                disp('port_status', self._convert_port_status),
            )
    
    # Convert Bytes
    @staticmethod
    def _convert_bytes(byte):
        units = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB'
            'YiB', 'BiB', 'NiB', 'DiB', 'CiB']
        for x in units:
            if divmod(byte, 1024)[0] == 0:
                break
            else:
                byte /= 1024
        return ('%.2lf%s' % (byte, x))
    
    # Convert Speed
    @staticmethod
    def _convert_speed(byte):
        return ('%s/s' % ClientStatus._convert_bytes(byte))
    
    # Convert port status
    @staticmethod
    def _convert_port_status(status):
        return status.name
