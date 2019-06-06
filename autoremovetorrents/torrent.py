#-*- coding:utf-8 -*-

import sys
import time

from .torrentstatus import TorrentStatus

class Torrent(object):
    def __init__(self, hash_value, name, category, tracker, status, stalled, size, ratio,
        uploaded, create_time, seeding_time):
        # Save Properties
        self.hash = hash_value
        self.name = name
        self.category = category
        self.tracker = tracker
        self.status = status
        self.stalled = stalled
        self.size = size
        self.ratio = ratio
        self.uploaded = uploaded
        self.create_time = create_time
        self.seeding_time = seeding_time

    # Format torrent info
    def __str__(self):
        return "%s\nSize:%s\tRatio:%.3f\tTotal Uploaded:%s\tSeeding Time:%s\tCategory:%s\nCreate Time:%s" % \
            (self.name,
            self._convert_bytes(self.size),
            self.ratio,
            self._convert_bytes(self.uploaded),
            self._convert_seconds(self.seeding_time),
            self.category,
            self._convert_timestamp(self.create_time)
            )
    
    # Convert Seconds
    @staticmethod
    def _convert_seconds(sec):
        if sec == -1:
            return '(Not Provided)'
        else:
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
        return '(Not Provided)' if timestamp == sys.maxsize \
            else time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))