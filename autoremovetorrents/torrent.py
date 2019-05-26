#-*- coding:utf-8 -*-

import sys
import time

from .torrentstatus import TorrentStatus

class Torrent(object):
    def __init__(self):
        # Proper attributes:
        # hash, name, category, tracker, status, size, ratio, uploaded, create_time, seeding_time
        pass

    # Format torrent info
    def __str__(self):
        def disp(prop, converter = None):
            if hasattr(self, prop):
                if converter is None:
                    return getattr(self, prop)
                else:
                    return converter(getattr(self, prop))
            else:
                return '(Not Provided)'
        
        return "%s\nSize:%s\tRatio:%.3f\tTotal Uploaded:%s\tSeeding Time:%s\tCategory:%s\nCreate Time:%s" % \
            (disp('name'),
            disp('size', self._convert_bytes),
            disp('ratio'),
            disp('uploaded', self._convert_bytes),
            disp('seeding_time', self._convert_seconds),
            disp('category', ','.join),
            disp('create_time', self._convert_timestamp)
            )
    
    # Convert Seconds
    @staticmethod
    def _convert_seconds(sec):
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        return ('%dd %02d:%02d:%02d' % (d, h, m, s))

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
    
    # Convert Timestamp
    @staticmethod
    def _convert_timestamp(timestamp):
        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))