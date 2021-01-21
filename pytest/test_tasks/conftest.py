import os
import json
import pytest
import requests_mock
import sys

sys.path.append(os.path.realpath(os.path.dirname(__file__))+"/../..")

from autoremovetorrents.compatibility.open_ import open_

@pytest.fixture(scope="function")
def qbittorrent_mocker(requests_mock):
    def runner():
        # Set root directory
        root_dir = os.path.join(os.path.realpath(os.path.dirname(__file__)))

        # Load mock URLs
        with open_(os.path.join(root_dir, 'mocks.json'), 'r', encoding='utf-8') as f:
            mocks = json.load(f)
            for url in mocks:
                # Mock GET and POST requests
                requests_mock.get(url, **mocks[url])
                requests_mock.post(url, **mocks[url])

    return runner