#-*- coding:utf-8 -*-
from autoremovetorrents.condition.ratio import RatioCondition

def test_ratio(load_data):
    # Apply condition
    ratio_cond = RatioCondition(3)
    ratio_cond.apply(load_data['input'])

    # Check results
    assert [x.name for x in ratio_cond.remove] == load_data['output']['ratio']