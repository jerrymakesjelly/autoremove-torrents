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

class Strategy(object):
    def __init__(self, name, conf):
        # Logger
        self._logger = logger.Logger.register(__name__)

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
        self._all_status = conf['all_status'] if 'all_status' in conf \
            else not 'status' in conf

    # Apply Filters
    def _apply_filters(self):
        filter_conf = [
            {'all':self._all_categories, 'ac':'categories', 're':'excluded_categories'}, # Category filter
            {'all':self._all_trackers, 'ac':'trackers', 're':'excluded_trackers'}, # Tracker filter
            {'all':self._all_status, 'ac':'status', 're':'excluded_status'} # Status filter
        ]
        filter_name = ['Category', 'Tracker', 'Status']
        filter_obj = [CategoryFilter, TrackerFilter, StatusFilter]
        for i in range(0, len(filter_conf)):
            # Logging
            self._logger.debug('Filter `%s` is working to process %d torrent(s): Accept All: %s, Accept: %s, Reject: %s.' \
                % (
                    filter_name[i],
                    len(self.remain_list),
                    'Yes' if filter_conf[i]['all'] else 'No',
                    str(len(self._conf[filter_conf[i]['ac']])) if filter_conf[i]['ac'] in self._conf else 'Not Specified',
                    str(len(self._conf[filter_conf[i]['re']])) if filter_conf[i]['re'] in self._conf else 'Not Specified',
                ))
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
            'ratio', 'seed_size', 'maximum_number', 'nothing'
        ]
        condition_obj = [
            SeedingTimeCondition, CreateTimeCondition,
            RatioCondition, TorrentSizeCondition, TorrentNumberCondition, EmptyCondition
        ]
        for i in range(0, len(condition_field)):
            # Apply each condition
            if condition_field[i] in self._conf:
                # Logging
                self._logger.debug('Remove condition `%s` was specified to process %d torrent(s).' \
                    % (condition_field[i], len(self.remain_list)))
                # Applying condition processor
                cond = condition_obj[i](self._conf[condition_field[i]])
                cond.apply(self.remain_list)
                # Logging
                self._logger.debug('The following %d torrent(s) would be remained.' % len(cond.remain))
                for torrent in cond.remain:
                    self._logger.debug(torrent)
                self._logger.debug('The follwing %d torrent(s) would be removed.' % len(cond.remove))
                for torrent in cond.remove:
                    self._logger.debug(torrent)
                # Output
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
        self._logger.info("Total: %d torrent(s). %d torrent(s) can be removed." %
            (len(self.remain_list)+len(self.remove_list), len(self.remove_list)))
        if len(self.remove_list) > 0:
            self._logger.info('To be deleted:')
            for torrent in self.remove_list:
                self._logger.info(torrent)
        #self._logger.debug('To be remained:')
        #for torrent in self.remain_list:
        #    self._logger.debug(torrent)
        #return self.remove_list