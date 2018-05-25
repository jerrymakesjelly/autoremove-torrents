#-*- coding:utf-8 -*-
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__))+"/../..")

import pytest

@pytest.fixture(scope="module")
def env_dist():
    # Load Environment Settings
    env = {}
    for x in os.environ:
        env[x] = os.environ[x].strip()
    # Add test data
    env['DELETE_DATA'] = False
    env['STRATEGIES'] = {'test_strategies': {'all_categories':True, 'all_trackers': True, 'nothing': True}}
    return env