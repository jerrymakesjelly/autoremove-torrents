#-*- coding:utf-8 -*-
from enum import Enum
TorrentStatus = Enum('TorrentStatus', ('Downloading', 'StalledDL', 'Uploading', 'StalledUP', 'Checking', 'Queued', 'Paused', 'Stopped', 'Unknown'))
