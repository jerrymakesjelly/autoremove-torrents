#-*- coding:utf-8 -*-

from .compatibility.urlparse_ import urlparse_
from .util.convertbytes import convert_bytes
from .util.convertseconds import convert_seconds
from .util.convertspeed import convert_speed
from .util.converttimestamp import convert_timestamp

class Torrent(object):
    def __init__(self):
        # Proper attributes:
        # hash, name, category, tracker, status, size, ratio, uploaded, create_time, seeding_time,
        # last_activity, progress, tags, download_speed, upload_speed, seeder, leecher,
        # connected_seeder, connected_leecher, average_upload_speed, average_download_speed
        self.hash = ""
        self.name = ""
        self.category = []
        self.tags = []
        self.tracker = []
        self.status = None
        self.size = 0
        self.ratio = 0.0
        self.uploaded = 0
        self.create_time = 0
        self.seeding_time = 0
        self.download_speed = 0
        self.upload_speed = 0
        self.seeder = 0
        self.connected_seeder = 0
        self.leecher = 0
        self.connected_leecher = 0
        self.average_upload_speed = 0
        self.average_download_speed = 0
        self.last_activity = 0
        self.progress = 0.0

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
            "\tCreate Time:%s\tSeeding Time:%s\tDownloading Time:%s\tLast Activity:%s\n" +
            "\tCategory:%s\tTags:%s\tTracker:%s") % \
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
                disp('downloading_time', convert_seconds),
                disp('last_activity', convert_seconds),
                disp('category', ','.join),
                disp('tags', ','.join),
                disp('tracker', lambda t: \
                    ','.join(
                        [urlparse_(x).hostname if urlparse_(x).hostname is not None else x for x in t]
                    )
                ),
            )
