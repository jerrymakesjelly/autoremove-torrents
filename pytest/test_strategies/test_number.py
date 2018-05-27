from autoremovetorrents.condition.torrentnumber import TorrentNumberCondition

def test_number_and_remove_old_seeds(load_data):
    tn_cond = TorrentNumberCondition({'limit':15, 'action':'remove-old-seeds'})
    tn_cond.apply(load_data['input'])

    assert [x.name for x in tn_cond.remove] == \
        load_data['output']['torrent_number']['remove-old-seeds']

def test_number_and_remove_new_seeds(load_data):
    tn_cond = TorrentNumberCondition({'limit':15, 'action':'remove-new-seeds'})
    tn_cond.apply(load_data['input'])

    assert [x.name for x in tn_cond.remove] == \
        load_data['output']['torrent_number']['remove-new-seeds']

def test_number_and_remove_big_seeds(load_data):
    tn_cond = TorrentNumberCondition({'limit':15, 'action':'remove-big-seeds'})
    tn_cond.apply(load_data['input'])

    assert [x.name for x in tn_cond.remove] == \
        load_data['output']['torrent_number']['remove-big-seeds']

def test_number_and_remove_small_seeds(load_data):
    tn_cond = TorrentNumberCondition({'limit':15, 'action':'remove-small-seeds'})
    tn_cond.apply(load_data['input'])

    assert [x.name for x in tn_cond.remove] == \
        load_data['output']['torrent_number']['remove-small-seeds']


