#-*- coding:utf-8 -*-
from enum import Enum
TorrentStatus = Enum('TorrentStatus', ('Downloading', 'Uploading', 'Checking', 'Queued', 'Paused', 'Stopped', 'Unknown'))