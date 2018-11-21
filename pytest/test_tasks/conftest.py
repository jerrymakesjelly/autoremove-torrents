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
    return env