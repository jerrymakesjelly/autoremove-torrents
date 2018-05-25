#-*- coding:utf-8 -*-
from autoremovetorrents.filter.tracker import TrackerFilter

def test_all_trackers(load_data):
    tracker_filt = TrackerFilter(True, [], [])
    assert [x.name for x in tracker_filt.apply(load_data['input'])] \
        == load_data['output']['categories']['all_categories']

def test_trackers(load_data):
    tracker_filt = TrackerFilter(False, ['tracker.site1.com'], [])
    assert [x.name for x in tracker_filt.apply(load_data['input'])] \
        == load_data['output']['categories']['category_1']

def test_excluded_trackers(load_data):
    tracker_filt = TrackerFilter(False, [], ['www.github.com'])
    assert [x.name for x in tracker_filt.apply(load_data['input'])] \
        == []

def test_all_trackers_and_trackers(load_data):
    tracker_filt = TrackerFilter(True, ['www.github.com'], [])
    assert [x.name for x in tracker_filt.apply(load_data['input'])] \
        == load_data['output']['categories']['all_categories']

def test_all_trackers_and_excluded_trackers(load_data):
    tracker_filt = TrackerFilter(True, [], ['www.site2.org'])
    assert [x.name for x in tracker_filt.apply(load_data['input'])] \
        == load_data['output']['categories']['category_1_and_category_3']

def test_trackers_and_excluded_trackers(load_data):
    tracker_filt = TrackerFilter(False, ['tracker.site1.com', 'www.site2.org'], ['www.site2.org'])
    assert [x.name for x in tracker_filt.apply(load_data['input'])] \
        == load_data['output']['categories']['category_1']