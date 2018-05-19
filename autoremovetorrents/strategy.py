#-*- coding:utf-8 -*-

from . import logger
from .filter.category import CategoryFilter
from .filter.tracker import TrackerFilter
from .condition.seedingtime import SeedingTimeCondition
from .condition.createtime import CreateTimeCondition
from .condition.ratio import RatioCondition
from .condition.torrentsize import TorrentSizeCondition

class Strategy(object):
    def __init__(self, name, conf):
        # Logger
        self._logger = logger.register(__name__)

        # Save name
        self._name = name

        # Configuration
        self._conf = conf

        # Results
        self.remain_list = []
        self.remove_list = []

        # Filter ALL
        self._all_categories = conf['all_categories'] if 'all_categories' in conf \
            else not 'categories' in conf
        self._all_trackers = conf['all_trackers'] if 'all_trackers' in conf \
            else not 'trackers' in conf
    
    # Apply Filters
    def _apply_filters(self):
        filter_conf = [
            {'all':self._all_categories, 'ac':'categories', 're':'excluded_categories'}, # Category filter
            {'all':self._all_trackers, 'ac':'trackers', 're':'excluded_trackers'} # Tracker filter
        ]
        filter_obj = [CategoryFilter, TrackerFilter]
        for i in range(0, len(filter_conf)):
            # Apply each filter
            self.remain_list = filter_obj[i](
                filter_conf[i]['all'],
                self._conf[filter_conf[i]['ac']] if filter_conf[i]['ac'] in self._conf else [],
                self._conf[filter_conf[i]['re']] if filter_conf[i]['re'] in self._conf else []
            ).apply(self.remain_list)

    # Apply Conditions
    def _apply_conditions(self):
        # Condition collection
        condition_field = [
            'seeding_time', 'create_time', 
            'ratio', 'seed_size'
        ]
        condition_obj = [
            SeedingTimeCondition, CreateTimeCondition, 
            RatioCondition, TorrentSizeCondition
        ]
        for i in range(0, len(condition_field)):
            # Apply each condition
            if condition_field[i] in self._conf:
                cond = condition_obj[i](self._conf[condition_field[i]])
                cond.apply(self.remain_list)
                self.remain_list = cond.remain
                self.remove_list.extend(cond.remove)

    # Execute this strategy
    def execute(self, torrents):
        self._logger.info('Running strategy %s...' % self._name)

        self.remain_list = torrents
        # Apply Filters
        self._apply_filters()
        # Apply Conditions
        self._apply_conditions()
        # Print remove list
        self._logger.info("Total: %d seed(s). %d seed(s) can be removed." %
            (len(self.remain_list)+len(self.remove_list), len(self.remove_list)))
        if len(self.remove_list) > 0:
            self._logger.info('To be deleted:')
            for torrent in self.remove_list:
                self._logger.info(torrent.format_info())
        #self._logger.info('To be remained:')
        #for torrent in self.remain_list:
        #    self._logger.info(torrent.format_info())
        #return self.remove_list