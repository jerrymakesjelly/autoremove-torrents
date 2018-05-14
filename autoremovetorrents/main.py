#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
import getopt
import traceback
from . import logger
from .autoremove import AutoRemover

def main():
    # View Mode
    view_mode = False
    # The path of the configuration file
    conf_path = 'config.yml'
    # Task
    task = None
    # Logger
    lg = logger.register(__name__)

    # Get arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'vc:t:', ['view', 'conf=', 'task='])
    except getopt.GetoptError:
        print('Invalid arguments.')
        sys.exit(2)
    for opt,arg in opts:
        if opt in ('-v', '--view'): # View mode (without deleting)
            view_mode = True
        elif opt in ('-c', '--conf'):
            conf_path = arg
        elif opt in ('-t', '--task'):
            task = arg
    
    # Run autoremove
    try:
        ar = AutoRemover(conf_path)
        result = ar.execute(task)
        if not view_mode:
            ar.remove(result)
    except Exception as exp:
        lg.error(traceback.format_exc().splitlines()[-1])
        lg.debug('Exception Logged', exc_info=True)
        lg.critical('An error occured. Please contact the administrator for more information.')

if __name__ == '__main__':
    main()