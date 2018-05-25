#-*- coding:utf-8 -*-
from autoremovetorrents.task import Task

def test_qbittorrent(env_dist):
    # Find host address, username and password in system environment variable
    if 'QBITTORRENT_HOST' in env_dist and 'QBITTORRENT_USERNAME' in env_dist and 'QBITTORRENT_PASSWORD' in env_dist:
        Task('test_qbittorrent_task', {
            'client': 'qbittorrent',
            'host': env_dist['QBITTORRENT_HOST'],
            'username': env_dist['QBITTORRENT_USERNAME'],
            'password': env_dist['QBITTORRENT_PASSWORD'],
            'delete_data': env_dist['DELETE_DATA'],
            'strategies': env_dist['STRATEGIES']
        }).execute()
    else:
        assert False # QBittorrent isn't in system environment