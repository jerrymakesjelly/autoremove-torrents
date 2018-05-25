#-*- coding:utf-8 -*-
from autoremovetorrents.condition.torrentsize import TorrentSizeCondition

# General Tester
def size_tester(data, limit, action):
    # Apply condition
    ts_cond = TorrentSizeCondition({'limit': limit, 'action': action})
    ts_cond.apply(data['input'])

    # Check result
    return set([x.name for x in ts_cond.remove]) \
        == set(data['output']['torrent_size'][action])

# Test remove-old-seeds Action
def test_size_and_remove_old_seeds(load_data):
    assert size_tester(load_data, 50, 'remove-old-seeds')

# Test remove-new-seeds Action
def test_size_and_remove_new_seeds(load_data):
    assert size_tester(load_data, 50, 'remove-new-seeds')

# Test remove-big-seeds Action
def test_size_and_remove_big_seeds(load_data):
    assert size_tester(load_data, 50, 'remove-big-seeds')

# Test remove-small-seeds Action
def test_size_and_remove_small_seeds(load_data):
    assert size_tester(load_data, 50, 'remove-small-seeds')