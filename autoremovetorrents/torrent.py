#-*- coding:utf-8 -*-

import time

from .compatibility.urlparse_ import urlparse_
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
        
        return ("%s\n" +
            "\tProgress:%.2f%%\tSize:%s\tRatio:%.3f\tTotal Uploaded:%s\n" +
            "\tSeeder(connected/total):%d/%d\tLeecher(connected/total):%d/%d\tStatus:%s\n" +
            "\tDownload Speed:%s(Avg.:%s)\tUpload Speed:%s(Avg.:%s)\n" +
            "\tCreate Time:%s\tSeeding Time:%s\tLast Activity:%s\n" +
            "\tCategory:%s\tTracker:%s") % \
            (
                disp('name'),
                disp('progress', lambda x: x*100),
                disp('size', self._convert_bytes),
                disp('ratio'),
                disp('uploaded', self._convert_bytes),
                disp('connected_seeder'),
                disp('seeder'),
                disp('connected_leecher'),
                disp('leecher'),
                disp('status', self._convert_status),
                disp('download_speed', self._convert_speed),
                disp('average_download_speed', self._convert_speed),
                disp('upload_speed', self._convert_speed),
                disp('average_upload_speed', self._convert_speed),
                disp('create_time', self._convert_timestamp),
                disp('seeding_time', self._convert_seconds),
                disp('last_activity', self._convert_timestamp),
                disp('category', self._convert_category),
                disp('tracker', self._convert_tracker),
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
    
    # Convert Speed
    @staticmethod
    def _convert_speed(byte):
        return ('%s/s' % Torrent._convert_bytes(byte))
    
    # Convert Timestamp
    @staticmethod
    def _convert_timestamp(timestamp):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
    
    # Convert Category
    @staticmethod
    def _convert_category(categories):
        return ','.join(categories)
    
    # Convert Tracker
    @staticmethod
    def _convert_tracker(trackers):
        return ','.join(
            [urlparse_(x).hostname if urlparse_(x).hostname is not None else x for x in trackers]
        )
    
    # Convert Status
    @staticmethod
    def _convert_status(status):
        return status.name
