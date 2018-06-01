import os
from autoremovetorrents import logger
from autoremovetorrents.main import pre_processor

# Logger
lg = logger.register(__name__)

def test_main():
    basic_dir = os.path.realpath(os.path.dirname(__file__))
    lg.info('Basic directory: %s' % basic_dir)
    
    # Open file of command lines
    with open(os.path.join(basic_dir, 'command_lines.txt')) as f:
        lines = f.readlines()
        # Get command lines
        for line in lines:
            lg.info('Command line: %s' % line)
            argv = line.split()
            pre_processor(argv) # Execute it