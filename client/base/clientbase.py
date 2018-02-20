#-*- coding:utf-8 -*-

class ClientBase(object):
    def __init__(self):
        pass
    
    # Torrents List Generator
    def _torrents_list(self, torrents_list):
        return torrents_list
    
    # Torrent Properties Generator
    def _torrent_properties(self, hash, name, category, tracker, status, size, ratio, uploaded, create_time, seeding_time):
        return {
            'hash': hash,
            'name': name,
            'category': category,
            'tracker': tracker,
            'status': status,
            'size': size,
            'ratio': ratio,
            'uploaded': uploaded,
            'create_time': create_time,
            'seeding_time': seeding_time
        }