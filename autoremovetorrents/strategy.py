#-*- coding:utf-8 -*-
from collections import defaultdict
from . import logger
from .compatibility.urlparse_ import urlparse_
from .condition.avgdownloadspeed import AverageDownloadSpeedCondition
from .condition.avguploadspeed import AverageUploadSpeedCondition
from .condition.connectedleecher import ConnectedLeecherCondition
from .condition.connectedseeder import ConnectedSeederCondition
from .condition.createtime import CreateTimeCondition
from .condition.downloadspeed import DownloadSpeedCondition
from .condition.donothing import EmptyCondition
from .condition.freespace import FreeSpaceCondition
from .condition.lastactivity import LastActivityCondition
from .condition.leecher import LeecherCondition
from .condition.progress import ProgressCondition
from .condition.ratio import RatioCondition
from .condition.seeder import SeederCondition
from .condition.seedingtime import SeedingTimeCondition
from .condition.size import SizeCondition
from .condition.torrentnumber import TorrentNumberCondition
from .condition.torrentsize import TorrentSizeCondition
from .condition.uploadratio import UploadRatioCondition
from .condition.uploadspeed import UploadSpeedCondition
from .conditionparser import ConditionParser
from .exception.unsupportedproperty import UnsupportedProperty
from .filter.category import CategoryFilter
from .filter.status import StatusFilter
from .filter.tracker import TrackerFilter

class Strategy(object):
    def __init__(self, name, conf, delete_data):
        # Logger
        self._logger = logger.Logger.register(__name__)

        # Save name
        self._name = name

        # Configuration
        self._conf = conf

        self._delete_data = delete_data
        # Default to not deleting cross-seeds
        self._delete_cross_seeds = conf['remove_cross_seeds'] if 'remove_cross_seeds' in conf else []

        # if all_trackers remove any cross-seeds. All other terms are
        # considered tracker hostnames.
        if self._delete_cross_seeds != "all_trackers" and type(self._delete_cross_seeds) != list:
            self._delete_cross_seeds = [self._delete_cross_seeds]

        # Results
        self.remain_list = set()
        self.remove_list = set()
        self.soft_remove_list = set()

        # Filter ALL
        self._all_categories = conf['all_categories'] if 'all_categories' in conf \
            else not 'categories' in conf
        self._all_trackers = conf['all_trackers'] if 'all_trackers' in conf \
            else not 'trackers' in conf
        self._all_status = conf['all_status'] if 'all_status' in conf \
            else not 'status' in conf

    # Apply Filters
    def _apply_filters(self):
        filter_conf = [
            {'all':self._all_categories, 'ac':'categories', 're':'excluded_categories'}, # Category filter
            {'all':self._all_status, 'ac':'status', 're':'excluded_status'}, # Status filter
            {'all':self._all_trackers, 'ac':'trackers', 're':'excluded_trackers'}, # Tracker filter
        ]
        filter_obj = [CategoryFilter, StatusFilter, TrackerFilter]
        for i in range(0, len(filter_conf)):
            # User can use a single line to represent one item instead of using list
            if filter_conf[i]['ac'] in self._conf and type(self._conf[filter_conf[i]['ac']]) != list:
                self._conf[filter_conf[i]['ac']] = [self._conf[filter_conf[i]['ac']]]
            if filter_conf[i]['re'] in self._conf and type(self._conf[filter_conf[i]['re']]) != list:
                self._conf[filter_conf[i]['re']] = [self._conf[filter_conf[i]['re']]]
            # Apply each filter
            self.remain_list = filter_obj[i](
                filter_conf[i]['all'],
                self._conf[filter_conf[i]['ac']] if filter_conf[i]['ac'] in self._conf else [],
                self._conf[filter_conf[i]['re']] if filter_conf[i]['re'] in self._conf else []
            ).apply(self.remain_list)

    # Apply Conditions
    def _apply_conditions(self):
        # Condition collection
        conditions = {
            'create_time': CreateTimeCondition,
            'free_space': FreeSpaceCondition,
            'last_activity': LastActivityCondition,
            'max_average_downloadspeed': AverageDownloadSpeedCondition,
            'max_connected_seeder': ConnectedSeederCondition,
            'max_downloadspeed': DownloadSpeedCondition,
            'max_progress': ProgressCondition,
            'max_seeder': SeederCondition,
            'maximum_number': TorrentNumberCondition,
            'min_average_uploadspeed': AverageUploadSpeedCondition,
            'min_connected_leecher': ConnectedLeecherCondition,
            'min_leecher': LeecherCondition,
            'min_uploadspeed': UploadSpeedCondition,
            'nothing': EmptyCondition,
            'ratio': RatioCondition,
            'remove': ConditionParser,
            'seed_size': TorrentSizeCondition,
            'seeding_time': SeedingTimeCondition,
            'max_size': SizeCondition,
            'upload_ratio': UploadRatioCondition,
        }
        for conf in self._conf:
            if conf in conditions:
                # Applying condition processor
                try:
                    cond = conditions[conf](self._conf[conf])
                    cond.apply(self.remain_list)
                except AttributeError as e:
                    raise UnsupportedProperty(
                        "%s. Your client may not support this property, so the condition %s does not work." % \
                        (str(e), conf)
                    )
                # Output
                self.remain_list = cond.remain
                self.remove_list.update(cond.remove)

    def _remove_cross_seeds(self, torrents):
        delete_hash = {torrent.hash for torrent in self.remove_list}
        remain = defaultdict(list)
        self._logger.info("Searching for cross-seeds to delete")
        for torrent in torrents:
            if torrent.hash not in delete_hash:
                remain[torrent.root_path].append(torrent)

        remove_list = set()
        soft_remove_list = set()
        for torrent in self.remove_list:
            if torrent.root_path in remain:
                cross_seeds = remain[torrent.root_path]
                marked_cross_seeds = set()
                for cross_seed in cross_seeds:
                    allowed_trackers = [urlparse_(tracker).hostname for tracker in cross_seed.tracker]
                    if self._delete_cross_seeds == "all_trackers" or any(allowed_tracker in self._delete_cross_seeds for allowed_tracker in allowed_trackers):
                        self._logger.info("Remove cross-seed: %s (trackers: %s)" % (cross_seed.name, ",".join(allowed_trackers)))
                        marked_cross_seeds.add(cross_seed)
                    else:
                        self._logger.info("Retain cross-seed: %s (trackers: %s)" % (cross_seed.name, ",".join(allowed_trackers)))

                if len(marked_cross_seeds) == len(cross_seeds):
                    # All cross-seededed torrents are marked for
                    # deletion we can safely allow the data to be
                    # deleted
                    #
                    # TODO: change remove_list to soft_remove_list
                    # (the data is removed by the original torrent)
                    remove_list.update(marked_cross_seeds)
                    remove_list.add(torrent)
                else:
                    # Only some of the cross-seeded torrents torrents
                    # have been marked for deletion. We cannot allow
                    # the torrents to be deleted from disk or the
                    # cross-seed will fail
                    soft_remove_list.update(marked_cross_seeds)
                    soft_remove_list.add(torrent)
            else:
                # Torrent is not cross-seeded, we can safely remove
                # the data
                remove_list.add(torrent)

        self.remove_list = remove_list
        self.soft_remove_list = soft_remove_list

    # Execute this strategy
    def execute(self, torrents):
        self._logger.info('Running strategy %s...' % self._name)
        self.remain_list = torrents
        # Apply Filters
        self._apply_filters()
        # Apply Conditions
        self._apply_conditions()

        # If we don't remove data, the cross-seeds should be handled
        # by another strategy. If we delete the data we should also
        # delete the cross-seed
        if self._delete_data:
            self._remove_cross_seeds(torrents)

        # Print remove list
        self._logger.info("Total: %d torrent(s). %d torrent(s) can be removed. %d torrent(s) can be safe removed (without data)." %
            (len(self.remain_list)+len(self.remove_list), len(self.remove_list), len(self.soft_remove_list)))
        if len(self.remove_list) > 0:
            self._logger.info('To be deleted:')
            for torrent in self.remove_list:
                self._logger.info(torrent)
        if len(self.soft_remove_list) > 0:
            self._logger.info('To be safe-deleted (without data):')
            for torrent in self.soft_remove_list:
                self._logger.info(torrent)
