from .. import logger
from .freespacebase import FreeSpaceConditionBase
from ..util.convertbytes import convert_bytes

class RemoteFreeSpaceCondition(FreeSpaceConditionBase):
    def __init__(self, settings):
        FreeSpaceConditionBase.__init__(self, settings)

        # Logger
        self._logger = logger.Logger.register(__name__)

        # Save path to be check
        self._path = settings['path']

    def apply(self, client_status, torrents):
        # Check free space on the server
        free_space = client_status.free_space(self._path)
        self._logger.info('Free space of %s on the server: %s' % (self._path, convert_bytes(free_space)))
        FreeSpaceConditionBase.apply(self, free_space, torrents)
