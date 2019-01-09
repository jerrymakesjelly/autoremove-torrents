import sys
import os
import yaml
from autoremovetorrents import logger
from autoremovetorrents.task import Task
from autoremovetorrents.exception.connectionfailure import ConnectionFailure
from autoremovetorrents.exception.deletionfailure import DeletionFailure
from autoremovetorrents.exception.loginfailure import LoginFailure
from autoremovetorrents.exception.nosuchclient import NoSuchClient
from autoremovetorrents.exception.nosuchtorrent import NoSuchTorrent
from autoremovetorrents.exception.remotefailure import RemoteFailure

# Logger
lg = logger.register(__name__)

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
    lg.info('Basic directory: %s' % basic_dir)

    for file in os.listdir(basic_dir):
        file_path = os.path.join(basic_dir, file)

        if os.path.isfile(file_path):
            # Load file
            lg.info('Loading file: %s' % file)
            with open(file_path, encoding='utf-8') as f:
                conf = yaml.safe_load(f)
            # Replace system environment variables
            keys = ['num-of-remaining', 'num-of-removed']
            if 'result' in conf:
                for key in keys:
                    if key in conf['result'] and isinstance(conf['result'][key], str) \
                        and conf['result'][key] in env_dist:
                        conf['result'][key] = env_dist[conf['result'][key]]

            # Make take and run
            try:
                task = Task(file, conf['task'])
                task.execute()
                if 'exceptions' in conf and len(conf['exceptions']) > 0:
                    raise AssertionError("It didn't raise exceptions as expected")
                if 'result' in conf:
                    if len(task.get_remaining_torrents()) != int(conf['result']['num-of-remaining']):
                        raise AssertionError('The actual number of remaining seeds does not match the assumption: %d != %d.' \
                            % (len(task.get_remaining_torrents()), int(conf['result']['num-of-remaining'])))
                    if len(task.get_removed_torrents()) != int(conf['result']['num-of-removed']):
                        raise AssertionError('The actual number of removed seeds does not match the assumption: %d != %d.' \
                            % (len(task.get_remaining_torrents()), int(conf['result']['num-of-removed'])))
            except Exception as e:
                # Check if the excpetion is expected
                found = False
                for e in exception_map:
                    if sys.exc_info()[0] == e:
                        if exception_map[e] in conf['exceptions']:
                            lg.info('An expected exception was raised: %s.' % exception_map[e])
                            found = True
                            break # An expected exception
                if not found:
                    raise e # Unexpected exception
