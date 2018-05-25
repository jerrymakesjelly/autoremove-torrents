#-*- coding:utf-8 -*-
from autoremovetorrents.strategy import Strategy

def test_strategy(load_data):
    # Reference to 'test_category', 'test_tracker', 'test_ratio' and 'test_seeding_time'
    # The result is the union of their results
    stgy = Strategy('test_strategy', 
        {
            'categories': ['Category - 1', 'Category - 3'],
            'trackers': ['tracker.site3.com'],
            'ratio': 3,
            'seeding_time': 21600
        })
    stgy.execute(load_data['input'])

    assert [x.name for x in stgy.remove_list] == \
        load_data['output']['test_strategy']