import sys
import os
import yaml
from autoremovetorrents import logger
from autoremovetorrents.task import Task
from autoremovetorrents.exception.connectionfailure import ConnectionFailure
from autoremovetorrents.exception.loginfailure import LoginFailure
from autoremovetorrents.exception.nosuchclient import NoSuchClient
from autoremovetorrents.exception.nosuchtorrent import NoSuchTorrent
from autoremovetorrents.exception.remotefailure import RemoteFailure
from autoremovetorrents.compatibility.open_ import open_

def test_client(env_dist):
    # Init logger
    logger.Logger.init()
    lg = logger.Logger.register(__name__)

    # Mapping of exceptions
    exception_map = {
        ConnectionFailure: 'ConnectionFailure',
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
            with open_(file_path, encoding='utf-8') as f:
                conf = yaml.safe_load(f)

            # Make take and run
            try:
                Task(file, conf['task'], True).execute()
                if 'exceptions' in conf and len(conf['exceptions']) > 0: # No exceptions was raised
                    raise AssertionError("It didn't raise exceptions as expected")
            except Exception as e:
                # Check if the excpetion is expected
                found = False
                for e in exception_map:
                    if sys.exc_info()[0] == e:
                        if 'exceptions' in conf and exception_map[e] in conf['exceptions']:
                            lg.info('An expected exception was raised: %s.' % exception_map[e])
                            found = True
                            break # An expected exception
                if not found:
                    raise e # Unexpected exception
