from autoremovetorrents.filter.status import StatusFilter

def test_all_status(load_data):
    status_filt = StatusFilter(True, [], [])

    assert [x.name for x in status_filt.apply(load_data['input'])] \
        == load_data['output']['categories']['all_categories']

def test_status(load_data):
    status_filt = StatusFilter(False, ['checking', 'queued'], [])

    assert [x.name for x in status_filt.apply(load_data['input'])] \
        == load_data['output']['status']['checking_and_queued']

def test_excluded_status(load_data):
    status_filt = StatusFilter(False, [], ['downloading'])

    assert status_filt.apply(load_data['input']) == []

def test_status_and_excluded_status(load_data):
    status_filt = StatusFilter(True, [], ['uploading'])

    assert [x.name for x in status_filt.apply(load_data['input'])] \
        == load_data['output']['status']['except_uploading']