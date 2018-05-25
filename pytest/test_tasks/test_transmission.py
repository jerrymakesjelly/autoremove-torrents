#-*- coding:utf-8 -*-
from autoremovetorrents.task import Task

def test_transmission(env_dist):
    # Find host address, username and password in system environment variable
    if 'TRANSMISSION_HOST' in env_dist and 'TRANSMISSION_USERNAME' in env_dist and 'TRANSMISSION_PASSWORD' in env_dist:
        Task('test_transmission_task', {
            'client': 'transmission',
            'host': env_dist['TRANSMISSION_HOST'],
            'username': env_dist['TRANSMISSION_USERNAME'],
            'password': env_dist['TRANSMISSION_PASSWORD'],
            'delete_data': env_dist['DELETE_DATA'],
            'strategies': env_dist['STRATEGIES']
        }).execute()
    else:
        assert False # Transmission isn't in system environment