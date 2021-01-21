#-*- coding:utf-8 -*-
from . import logger
from .condition.avgdownloadspeed import AverageDownloadSpeedCondition
from .condition.avguploadspeed import AverageUploadSpeedCondition
from .condition.connectedleecher import ConnectedLeecherCondition
from .condition.connectedseeder import ConnectedSeederCondition
from .condition.createtime import CreateTimeCondition
from .condition.downloaded import DownloadsCondition
from .condition.downloadspeed import DownloadSpeedCondition
from .condition.donothing import EmptyCondition
from .condition.freespace import FreeSpaceCondition
from .condition.lastactivity import LastActivityCondition
from .condition.leecher import LeecherCondition
from .condition.progress import ProgressCondition
from .condition.ratio import RatioCondition
from .condition.remotefreespace import RemoteFreeSpaceCondition
from .condition.seeder import SeederCondition
from .condition.seedingtime import SeedingTimeCondition
from .condition.size import SizeCondition
from .condition.torrentnumber import TorrentNumberCondition
from .condition.torrentsize import TorrentSizeCondition
from .condition.uploaded import UploadsCondition
from .condition.uploadratio import UploadRatioCondition
from .condition.uploadspeed import UploadSpeedCondition
from .conditionparser import ConditionParser
from .exception.unsupportedproperty import UnsupportedProperty
from .filter.category import CategoryFilter
from .filter.status import StatusFilter
from .filter.tracker import TrackerFilter

class Strategy(object):
    def __init__(self, name, conf):
        # Logger
        self._logger = logger.Logger.register(__name__)

        # Save name
        self._name = name

        # Configuration
        self._conf = conf

        # Results
        self.remain_list = set()
        self.remove_list = set()

        # Filter ALL
        self._all_categories = conf['all_categories'] if 'all_categories' in conf \
            else not 'categories' in conf
        self._all_trackers = conf['all_trackers'] if 'all_trackers' in conf \
            else not 'trackers' in conf
        self._all_status = conf['all_status'] if 'all_status' in conf \
            else not 'status' in conf

        # Print debug log
        self._logger.debug("Configuration of strategy '%s':" % self._name)
        self._logger.debug('Configurated filters and conditions: %s' % ', '.join(self._conf))

    # Apply Filters
    def _apply_filters(self):
        filter_conf = [
            {'all':self._all_categories, 'ac':'categories', 're':'excluded_categories'}, # Category filter
            {'all':self._all_status, 'ac':'status', 're':'excluded_status'}, # Status filter
            {'all':self._all_trackers, 'ac':'trackers', 're':'excluded_trackers'}, # Tracker filter
        ]
        filter_obj = [CategoryFilter, StatusFilter, TrackerFilter]

        for i in range(0, len(filter_conf)):
            # Initialize all of the filter arguments
            # User can use a single line to represent one item instead of using list
            accept_field = filter_conf[i]['ac']
            reject_field = filter_conf[i]['re']
            if accept_field not in self._conf:
                self._conf[accept_field] = []
            if reject_field not in self._conf:
                self._conf[reject_field] = []

            if not isinstance(self._conf[accept_field], list):
                self._conf[accept_field] = [self._conf[accept_field]] # Make it a list
            if not isinstance(self._conf[reject_field], list):
                self._conf[reject_field] = [self._conf[reject_field]]

            # Print debug log
            self._logger.debug('Applying filter %s...' % filter_obj[i].__name__)
            self._logger.debug('Filter configrations: ALL: %s; ACCEPTANCES: [%s]; REJECTIONS: [%s].' % (
                filter_conf[i]['all'],
                ', '.join(self._conf[accept_field]),
                ', '.join(self._conf[reject_field])
            ))
            self._logger.debug('INPUT: %d torrent(s) before applying the filter.' % len(self.remain_list))
            for torrent in self.remain_list:
                self._logger.debug(torrent)

            # Apply each filter
            self.remain_list = filter_obj[i](
                filter_conf[i]['all'],
                self._conf[accept_field],
                self._conf[reject_field]
            ).apply(self.remain_list)

            # Print debug log again
            self._logger.debug('OUTPUT: %d torrent(s) after applying the filter.' % len(self.remain_list))
            for torrent in self.remain_list:
                self._logger.debug(torrent)

    # Apply Conditions
    def _apply_conditions(self, client_status):
        # Condition collection
        conditions = {
            'create_time': CreateTimeCondition,
            'free_space': FreeSpaceCondition,
            'last_activity': LastActivityCondition,
            'max_average_downloadspeed': AverageDownloadSpeedCondition,
            'max_connected_seeder': ConnectedSeederCondition,
            'max_download': DownloadsCondition,
            'max_downloadspeed': DownloadSpeedCondition,
            'max_progress': ProgressCondition,
            'max_seeder': SeederCondition,
            'max_upload': UploadsCondition,
            'maximum_number': TorrentNumberCondition,
            'min_average_uploadspeed': AverageUploadSpeedCondition,
            'min_connected_leecher': ConnectedLeecherCondition,
            'min_leecher': LeecherCondition,
            'min_uploadspeed': UploadSpeedCondition,
            'nothing': EmptyCondition,
            'ratio': RatioCondition,
            'remote_free_space': RemoteFreeSpaceCondition,
            'remove': ConditionParser,
            'seed_size': TorrentSizeCondition,
            'seeding_time': SeedingTimeCondition,
            'max_size': SizeCondition,
            'upload_ratio': UploadRatioCondition,
        }
        for conf in self._conf:
            if conf in conditions:
                # Print debug log
                self._logger.debug('Applying condition %s...' % conditions[conf].__name__)
                self._logger.debug('INPUT: %d torrent(s) to be reserved before applying the condition.' % len(self.remain_list))
                for torrent in self.remain_list:
                    self._logger.debug(torrent)

                # Applying condition processor
                try:
                    cond = conditions[conf](self._conf[conf])
                    cond.apply(client_status, self.remain_list)
                except AttributeError as e:
                    raise UnsupportedProperty(
                        "%s. Your client may not support this property, so the condition %s does not work." % \
                        (str(e), conf)
                    )
                
                # Output
                self.remain_list = cond.remain
                self.remove_list.update(cond.remove)

                # Print updated list to debug log
                self._logger.debug('OUTPUT: %d torrent(s) to be reserved after applying the condition.' % len(self.remain_list))
                for torrent in self.remain_list:
                    self._logger.debug(torrent)
                self._logger.debug('OUTPUT: %d torrent(s) to be removed after applying the condition.' % len(self.remove_list))
                for torrent in self.remove_list:
                    self._logger.debug(torrent)

    # Execute this strategy
    def execute(self, client_status, torrents):
        self._logger.info('Running strategy %s...' % self._name)
        self.remain_list = torrents
        # Apply Filters
        self._apply_filters()
        # Apply Conditions
        self._apply_conditions(client_status)
        # Print remove list
        self._logger.info("Total: %d torrent(s). %d torrent(s) can be removed." %
            (len(self.remain_list)+len(self.remove_list), len(self.remove_list)))
        if len(self.remove_list) > 0:
            self._logger.info('To be deleted:')
            for torrent in self.remove_list:
                self._logger.info(torrent)