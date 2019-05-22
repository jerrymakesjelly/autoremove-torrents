#-*- coding:utf-8 -*-

from . import logger
from .filter.category import CategoryFilter
from .filter.tracker import TrackerFilter
from .filter.status import StatusFilter
from .condition.seedingtime import SeedingTimeCondition
from .condition.createtime import CreateTimeCondition
from .condition.ratio import RatioCondition
from .condition.torrentsize import TorrentSizeCondition
from .condition.torrentnumber import TorrentNumberCondition
from .condition.donothing import EmptyCondition
from .conditionparser import ConditionParser

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

    # Apply Filters
    def _apply_filters(self):
        filter_conf = [
            {'all':self._all_categories, 'ac':'categories', 're':'excluded_categories'}, # Category filter
            {'all':self._all_trackers, 'ac':'trackers', 're':'excluded_trackers'}, # Tracker filter
            {'all':self._all_status, 'ac':'status', 're':'excluded_status'} # Status filter
        ]
        filter_obj = [CategoryFilter, TrackerFilter, StatusFilter]
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
            'remove': ConditionParser,
            'seeding_time': SeedingTimeCondition,
            'create_time': CreateTimeCondition,
            'ratio': RatioCondition,
            'seed_size': TorrentSizeCondition,
            'maximum_number': TorrentNumberCondition,
            'nothing': EmptyCondition
        }
        for conf in self._conf:
            if conf in conditions:
                # Applying condition processor
                cond = conditions[conf](self._conf[conf])
                cond.apply(self.remain_list)
                # Output
                self.remain_list = cond.remain
                self.remove_list.update(cond.remove)

    # Execute this strategy
    def execute(self, torrents):
        self._logger.info('Running strategy %s...' % self._name)
        self.remain_list = torrents
        # Apply Filters
        self._apply_filters()
        # Apply Conditions
        self._apply_conditions()
        # Print remove list
        self._logger.info("Total: %d torrent(s). %d torrent(s) can be removed." %
            (len(self.remain_list)+len(self.remove_list), len(self.remove_list)))
        if len(self.remove_list) > 0:
            self._logger.info('To be deleted:')
            for torrent in self.remove_list:
                self._logger.info(torrent)