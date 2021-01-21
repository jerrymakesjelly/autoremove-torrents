#-*- coding:utf-8 -*-

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__))+"/../..")

import pytest
import json
from autoremovetorrents.clientstatus import ClientStatus
from autoremovetorrents.portstatus import PortStatus
from autoremovetorrents.torrent import Torrent
from autoremovetorrents.torrentstatus import TorrentStatus
from autoremovetorrents.compatibility.open_ import open_

@pytest.fixture(scope="module")
def test_data():
    # Load input data
    input_torrents = []
    with open_(os.path.join(os.path.realpath(os.path.dirname(__file__)),'data.json'), encoding='utf-8') as f:
        data = json.load(f)
    for torrent in data:
        torrent_obj = Torrent()
        torrent_obj.hash = torrent['hash']
        torrent_obj.name = torrent['name']
        torrent_obj.category = [torrent['category']] if len(torrent['category']) > 0 else []
        torrent_obj.tracker = torrent['tracker']
        torrent_obj.status = TorrentStatus[torrent['state']]
        torrent_obj.stalled = torrent['is_stalled']
        torrent_obj.size = torrent['size']
        torrent_obj.ratio = torrent['ratio']
        torrent_obj.uploaded = torrent['uploaded']
        torrent_obj.create_time = torrent['added_on']
        torrent_obj.seeding_time = torrent['seeding_time']
        torrent_obj.upload_speed = torrent['upspeed']
        torrent_obj.average_upload_speed = torrent['up_speed_avg']
        torrent_obj.downloaded = torrent['downloaded']
        torrent_obj.download_speed = torrent['dlspeed']
        torrent_obj.average_download_speed = torrent['dl_speed_avg']
        torrent_obj.last_activity = torrent['last_activity']
        torrent_obj.seeder = torrent['num_complete']
        torrent_obj.connected_seeder = torrent['num_seeds']
        torrent_obj.leecher = torrent['num_incomplete']
        torrent_obj.connected_leecher = torrent['num_leechs']
        torrent_obj.progress = torrent['progress']
        input_torrents.append(torrent_obj)

    return input_torrents

@pytest.fixture(scope="module")
def test_env():
    with open_(os.path.join(os.path.realpath(os.path.dirname(__file__)), 'environment.json'), encoding='utf-8') as f:
        env = json.load(f)
    return env

@pytest.fixture(scope="module")
def test_status():
    cs = ClientStatus()
    with open_(os.path.join(os.path.realpath(os.path.dirname(__file__)), 'clientstatus.json'), encoding='utf-8') as f:
        data = json.load(f)

        cs.download_speed = data['download_speed']
        cs.total_downloaded = data['total_downloaded']
        cs.upload_speed = data['upload_speed']
        cs.total_uploaded = data['total_uploaded']
        cs.port_status = PortStatus[data['port_status']]
        cs.free_space = lambda _: data['free_space']

    return cs
