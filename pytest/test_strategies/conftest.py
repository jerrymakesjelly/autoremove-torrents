#-*- coding:utf-8 -*-

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__))+"/../..")

import pytest
import json
from autoremovetorrents.torrent import Torrent
from autoremovetorrents.torrentstatus import TorrentStatus

@pytest.fixture(scope="module")
def load_data():
    # Load input data
    input = []
    with open(os.path.join(os.path.realpath(os.path.dirname(__file__)),'data.json'), encoding='utf-8') as f:
        data = json.load(f)
    for torrent in data:
        input.append(Torrent(
            torrent['hash'],
            torrent['name'],
            torrent['category'],
            torrent['tracker'],
            TorrentStatus(torrent['state']),
            torrent['size'],
            torrent['ratio'],
            torrent['uploaded'],
            torrent['added_on'],
            torrent['seeding_time']
        ))

    # Load output data
    with open(os.path.join(os.path.realpath(os.path.dirname(__file__)),'output.json'), encoding='utf-8') as f:
        output = json.load(f)
    
    return {
        'input':input,
        'output':output
    }
