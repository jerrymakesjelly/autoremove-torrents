#-*- coding:utf-8 -*-

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__))+"/../..")

import pytest
import json
from autoremovetorrents.torrent import Torrent
from autoremovetorrents.torrentstatus import TorrentStatus
from autoremovetorrents.compatibility.open import _open

@pytest.fixture(scope="module")
def test_data():
    # Load input data
    input_torrents = []
    with _open(os.path.join(os.path.realpath(os.path.dirname(__file__)),'data.json'), encoding='utf-8') as f:
        data = json.load(f)
    for torrent in data:
        input_torrents.append(Torrent(
            torrent['hash'],
            torrent['name'],
            torrent['category'],
            torrent['tracker'],
            TorrentStatus[str(torrent['state']).capitalize()],
            torrent['is_stalled'],
            torrent['size'],
            torrent['ratio'],
            torrent['uploaded'],
            torrent['added_on'],
            torrent['seeding_time']
        ))

    return input_torrents

@pytest.fixture(scope="module")
def test_env():
    with _open(os.path.join(os.path.realpath(os.path.dirname(__file__)), 'environment.json'), encoding='utf-8') as f:
        env = json.load(f)
    return env