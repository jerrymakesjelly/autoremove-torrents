#-*- coding:utf-8 -*-

from .compatibility.urlparse_ import urlparse_
from .util.convertbytes import convert_bytes
from .util.convertseconds import convert_seconds
from .util.convertspeed import convert_speed
from .util.converttimestamp import convert_timestamp

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
                disp('size', convert_bytes),
                disp('ratio'),
                disp('uploaded', convert_bytes),
                disp('connected_seeder'),
                disp('seeder'),
                disp('connected_leecher'),
                disp('leecher'),
                disp('status', lambda s: s.name),
                disp('download_speed', convert_speed),
                disp('average_download_speed', convert_speed),
                disp('upload_speed', convert_speed),
                disp('average_upload_speed', convert_speed),
                disp('create_time', convert_timestamp),
                disp('seeding_time', convert_seconds),
                disp('last_activity', convert_timestamp),
                disp('category', ','.join),
                disp('tracker', lambda t: \
                    ','.join(
                        [urlparse_(x).hostname if urlparse_(x).hostname is not None else x for x in t]
                    )
                ),
            )
