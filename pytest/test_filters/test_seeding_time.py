#-*- coding:utf-8 -*-
from autoremovetorrents.condition.seedingtime import SeedingTimeCondition

def test_seeding_time(load_data):
    # Apply condition
    st_cond = SeedingTimeCondition(21600)
    st_cond.apply(load_data['input'])

    # Check result
    assert [x.name for x in st_cond.remove] == load_data['output']['seeding_time']