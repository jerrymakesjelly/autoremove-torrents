import sys
import os
import yaml
from collections import namedtuple
from autoremovetorrents import logger
from autoremovetorrents.strategy import Strategy
from autoremovetorrents.exception.illegalcharacter import IllegalCharacter
from autoremovetorrents.exception.syntaxerror import ConditionSyntaxError
from autoremovetorrents.exception.nosuchcondition import NoSuchCondition
from autoremovetorrents.compatibility.open_ import open_
from autoremovetorrents.compatibility.disk_usage_ import SUPPORT_SHUTIL

def test_strategies(mocker, test_data, test_env, test_status):
    # Init logger
    logger.Logger.init()
    lg = logger.Logger.register(__name__)

    # Exceptions mapping
    exception_map = {
        IllegalCharacter: 'IllegalCharacter',
        ConditionSyntaxError: 'ConditionSyntaxError',
        NoSuchCondition: 'NoSuchCondition'
    }

    # Check each case
    base_dir = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'cases')
    lg.info('Base directory: %s' % base_dir)

    for item in os.listdir(base_dir):
        if os.path.isdir(os.path.join(base_dir, item)):
            # Enter a directory
            lg.info("Entering directory '%s'..." % item)

            for conf_file in os.listdir(os.path.join(base_dir, item)):
                conf_path = os.path.join(base_dir, item, conf_file)
                if os.path.isfile(conf_path):
                    # Load file
                    lg.info('Loading file: %s' % conf_file)
                    with open_(conf_path, encoding='utf-8') as f:
                        conf = yaml.safe_load(f)

                    try:
                        # Mock current time
                        mocker.patch('time.time', return_value=test_env['time.time'])

                        # Mock disk usage
                        if SUPPORT_SHUTIL:
                            mocker.patch('shutil.disk_usage',
                                return_value=namedtuple(
                                    'usage',
                                    ['total', 'used', 'free'],
                                )(**test_env['shutil.disk_usage'])
                            )
                        else:
                            mocker.patch('psutil.disk_usage',
                                return_value=namedtuple(
                                    'sdiskusage',
                                    ['total', 'used', 'free', 'percent'],
                                )(**test_env['psutil.disk_usage'])
                            )

                        # Make strategy and run
                        stgy = Strategy(conf_file, conf['test'])
                        stgy.execute(test_status, test_data)

                        # Check result
                        if 'remain' in conf:
                            assert set([x.name for x in stgy.remain_list]) == set(conf['remain'] if conf['remain'] is not None else [])
                        if 'remove' in conf:
                            assert set([x.name for x in stgy.remove_list]) == set(conf['remove'] if conf['remove'] is not None else [])
                    except Exception as e:
                        if 'exceptions' in conf and exception_map[sys.exc_info()[0]] in conf['exceptions']:
                            pass
                        else:
                            raise e

            # Leave the directory
            lg.info("Leaving directory '%s'..." % item)