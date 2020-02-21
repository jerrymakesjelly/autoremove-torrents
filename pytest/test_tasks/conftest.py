import os
import json
import pytest
import requests_mock
from autoremovetorrents.compatibility.open_ import open_

@pytest.fixture(scope="function")
def qbittorrent_mocker(requests_mock):
    def runner():
        # Set root directory
        root_dir = os.path.join(os.path.realpath(os.path.dirname(__file__)))

        # Mock qBittorrent API version
        # Force caller to use API v1.0
        requests_mock.get('mock://qbittorrent/api/v2/app/webapiVersion', status_code=404)
        requests_mock.get('mock://qbittorrent/version/api', text='10')

        # Mock qBittorrent version
        requests_mock.get('mock://qbittorrent/version/qbittorrent', text='Fake qBittorrent')
        #lg.info('qBittorrent version was mocked.')

        # Mock qBittorrent logging in interface
        requests_mock.post('mock://qbittorrent/login', text='Ok.')
        #lg.info('Logging in was mocked.')

        # Mock qBittorrent torrents list
        with open_(os.path.join(root_dir, 'qbittorrent-snapshots', '4-1-5.json'),
            'r', encoding='utf-8') as f:
            torrent_list = json.load(f)
            requests_mock.get('mock://qbittorrent/query/torrents', json=torrent_list)
            #lg.info('Torrents list was mocked.')
        
        # Mock qBittorent torrent details
        for torrent in torrent_list:
            with open_(os.path.join(
                root_dir, 'qbittorrent-snapshots', 
                'torrents', '%s.json' % torrent['hash'])) as fp:
                metadata = json.load(fp)
                requests_mock.get(
                    'mock://qbittorrent/query/propertiesGeneral/%s' % torrent['hash'],
                    json=metadata['properties'])
                requests_mock.get(
                    'mock://qbittorrent/query/propertiesTrackers/%s' % torrent['hash'],
                    json=metadata['trackers']
                )
                #lg.info('Torrent %s was mocked.', torrent['hash'])
    return runner