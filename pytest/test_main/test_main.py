import os
from autoremovetorrents.main import main

def test_main():
    basic_dir = os.path.realpath(os.path.dirname(__file__))
    print('Basic directory: %s' % basic_dir)
    
    # Open file of command lines
    with open(os.path.join(basic_dir, 'command_lines.txt')) as f:
        lines = f.readlines()
        # Get command lines
        for line in lines:
            print('Command line: %s' % line)
            argv = line.split()
            main(argv) # Execute it