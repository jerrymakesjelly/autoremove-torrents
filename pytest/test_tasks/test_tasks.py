import yaml
import os
from autoremovetorrents import logger
from autoremovetorrents.task import Task
from autoremovetorrents.compatibility.open_ import open_

def test_task(qbittorrent_mocker):
    # Init loggger
    logger.Logger.init()
    lg = logger.Logger.register(__name__)

    # Set root directory
    root_dir = os.path.join(os.path.realpath(os.path.dirname(__file__)))
    lg.info('Root directory: %s', root_dir)

    qbittorrent_mocker()

    # Load files in directory
    for file in os.listdir(os.path.join(root_dir, 'cases')):
        file_path = os.path.join(root_dir, 'cases', file)

        if os.path.isfile(file_path):
            lg.info('Loading file: %s', file)
            with open_(file_path, 'r', encoding='utf-8') as f:
                conf = yaml.safe_load(f)

            # Run task
            instance = Task(file, conf['task'], False)
            instance.execute()
            assert len(instance.get_removed_torrents()) == conf['result']['num-of-removed']