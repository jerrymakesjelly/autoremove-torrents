import sys
import os
import yaml
from autoremovetorrents.task import Task
from autoremovetorrents.exception.connectionfailure import ConnectionFailure
from autoremovetorrents.exception.deletionfailure import DeletionFailure
from autoremovetorrents.exception.loginfailure import LoginFailure
from autoremovetorrents.exception.nosuchclient import NoSuchClient
from autoremovetorrents.exception.nosuchtorrent import NoSuchTorrent
from autoremovetorrents.exception.remotefailure import RemoteFailure

def test_task(env_dist):
    # Mapping of exceptions
    exception_map = {
        ConnectionFailure: 'ConnectionFailure',
        DeletionFailure: 'DeletionFailure',
        LoginFailure: 'LoginFailure',
        NoSuchClient: 'NoSuchClient',
        NoSuchTorrent: 'NoSuchTorrent',
        RemoteFailure: 'RemoteFailure'
    }

    # Set basic directory
    basic_dir = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'cases')
    print('Basic directory: %s' % basic_dir)

    for file in os.listdir(basic_dir):
        file_path = os.path.join(basic_dir, file)

        if os.path.isfile(file_path):
            # Load file
            print('Loading file: %s' % file)
            with open(file_path, encoding='utf-8') as f:
                conf = yaml.safe_load(f)

            # Make take and run
            try:
                task = Task(file, conf['task'])
                task.execute()
            except Exception:
                # Check if the excpetion is expected
                found = False
                for e in exception_map:
                    if sys.exc_info()[0] == e:
                        if exception_map[e] in conf['exceptions']:
                            print('An expected exception was raised: %s.' % exception_map[e])
                            found = True
                            break # An expected exception
                if not found:
                    raise AssertionError() # Unexpected exception
