#-*- coding:utf-8 -*-
from autoremovetorrents.condition.createtime import CreateTimeCondition

def test_create_time(load_data):
    # Apply condition
    ct_cond = CreateTimeCondition(17124)
    ct_cond.apply(load_data['input'], 1526738305)

    # Check result
    assert [x.name for x in ct_cond.remove] == load_data['output']['create_time']

# Used UNIX Time Stamp: 1526738305