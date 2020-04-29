def convert_bytes(byte):
    units = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB'
        'YiB', 'BiB', 'NiB', 'DiB', 'CiB']
    for x in units:
        if divmod(byte, 1024)[0] == 0:
            break
        else:
            byte /= 1024
    return ('%.2lf%s' % (byte, x))
