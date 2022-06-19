.. _changelog:

ChangeLog
==========

Version 1.5.4
--------------

*Release Date: Sunday, 19 June 2022*

Changes
++++++++

* Remove outgoing port status info. (#101) (#135)
    - We have confirmed a bug, which is, the outgoing port status checker will fail and report 'portTested: http error 400: Bad Request' when we are using Transmission and check the outgoing port status in IPv6 network.
    - Since there are no configurations relying on this status, we remove it.

* Change ``last_activity``'s behaviour. (#93) (#98) (#109)
    - By default, it won't remove those torrents that have never been active anymore.
    - These torrents that have never been active can be removed by the following configuration:
        + ``last_activity: never`` or ``last_activity: none`` for ``last_activity`` condition.
        + ``last_activity = never`` or ``last_activity = none`` for ``remove`` expression.

Features
+++++++++

* Add ``remove-slow-upload-seeds`` and ``remove-fast-upload-seeds`` actions to keyword ``action``. (#127) Thanks to @vincent906!
* Support equality (``=``) comparison in ``remove`` expression.
* Add ``downloading_time`` condition. (#88) Thanks to @dantebarba!

Fix
++++

* Fix a bug that Downloaded/Uploaded Size conditions and ``free_space``/``remote_free_space`` cannot handle decimals correctly. (#133) Thanks to @sfwn!
* Fix a bug that ``last_activity`` condition doesn't work in Deluge 2.0.3 and above. (#119)

Version 1.5.3
--------------

*Release Date: Thursday, 27 August 2020*

Features
+++++++++

* Enable to output debug logs by specifying ``--debug`` or ``-d`` argument. (#76)
* Add uploaded size and downloaded size conditions. (#79)

Fix
++++

* Fix psutil's compatibility in Synology (use to check the free spaces). (#61)
* Fix API imcompatibility issue caused by the trailing ``/`` in host URL. (#81)

Version 1.5.2
--------------

*Release Date: Friday, 27 March 2020*

Change
+++++++

* Set the client names to be case-insensitive.

Features
+++++++++

* Support Deluge. (#8)
* Use batch delete to improve efficiency.

Fix
++++

* Fix multi-language support in config file. (#69)

Version 1.5.1
--------------

*Release Date: Saturday, 29 February 2020*

Fix
++++

* Fix missing status ``StalledUpload`` and ``StalledDownload`` in version 1.5.0. (#66)

Version 1.5.0
--------------

*Release Date: Friday, 28 February 2020*

Features
+++++++++

* Add new status ``Error`` to filter ``status``.
* Add support for Transmission labels. (#24)
* Add removing conditions: Maximum Download Speed ``max_downloadspeed`` and Minimum Upload Speed ``min_uploadspeed``.
* Add removing conditions: Maximum Average Download Speed ``max_average_downloadspeed`` and Minimum Average Upload Speed ``min_average_uploadspeed``. (#49)
* Add removing conditions: Maximum Torrent Size ``max_size``. (#21)
* Add removing conditions: Maximum Number of Seeders ``max_seeder`` and Minimum Number of Leechers ``min_leecher``. (#62)
* Add removing conditions: Maximum Number of Connected Seeders ``max_connected_seeder`` and Minimum Number of Connected Leechers ``min_connected_leecher``.
* Add a removing condition: Last Activity ``last_activity``, which removes torrents without upload or download speed for a period of time. (#1) (#9)
* Add a removing condition: Maximum Download Progress ``max_progress``.
* Add actions: add ``remove-active-seeds`` and ``remove-inactive-seeds`` to ``free_space``, ``maximum_number`` and ``seed_size`` in order to try to remove active or inactive torrents based on the last active time. (#9)
* Add a removing condition: Upload Ratio ``upload_ratio``, which can remove torrents based on the ratio of uploaded size to torrent size. (#55)

Fix
++++

* Fix a problem: cannot login to client with numeric username or password. (#64)
* Fix a problem: tasks could not be executed in a Transmission without label properties.
* Fix a problem: removing conditions may not work for unlabeled and trackerless torrents.
* Fix a problem: missing status ``Queued`` in μTorrent.

Documents Migration
--------------------

*Date: Monday, 3 February 2020*

* Migrate documents to Read the Docs.

Version 1.4.9
--------------

*Release Date: Sunday, 26 January 2020*

Feature
++++++++

* Add `free_space` condition. Thanks to @drawwon!

Version 1.4.8
--------------

*Release Date: Tuesday, 7 January 2020*

Fix
++++

* Fix bug that cannot delete torrents in qBittorrent v4.2.1+. Sorry for any inconvenience. (#53)

Version 1.4.7
--------------

*Release Date: Monday, 6 January 2020*

Feature
++++++++

* Add support for new API in qBittorrent 4.2.1. (#46)

.. note::

   Note: This version has a bug. Please upgrade to v1.4.8 or higher.

Version 1.4.6
--------------

*Release Date: Tuesday, 17 September 2019*

Fix
++++

* Fix problem that the tracker filter needs to specific ports when the tracker URL includes port number. (#38)

Version 1.4.5
--------------

*Release Date: Thursday, 6 June 2019*

Feature
++++++++

* Added status `StalledUpload` and `StalledDownload`. (#34)

Version 1.4.4
--------------

*Release Date: Wednesday, 22 May 2019*

Feature
++++++++

* New feature: if the content of `filter` has only one line, now it is allowed to write down directly without using list.

Fix
++++

* Fixed a bug that when condition `seed_size` / `maximum_number` is used together with condtion `ratio` / `create_time` / `seeding_time`, the task will fail. (#33)

Version 1.4.3
--------------

*Release Date: Sunday, 19 May 2019*

Changes
++++++++

* Supported Python 2.7. (#29)
* Stopped supporting Python 3.4. (kennethreitz/requests#5092)

Version 1.4.2
--------------

*Release Date: Monday, 13 May 2019*

Fix
++++

* Fixed missing parser files. (#32)
* Fixed association of operators. (#32) Now the operator `and` and `or` are guaranteed to be left-associative.

Version 1.4.1
--------------

*Release Date: Monday, 6 May 2019*

Fix
++++

* Fixed missing dependency: `ply`.
* Fixed the warning of duplicate definition in condition `remove`.

Wiki Update
------------

*Date: Monday, 6 May 2019*

* Added the description of `remove` condition into Simplified-Chinese Wiki.

Version 1.4.0
--------------

*Release Date: Wednesday, 1 May 2019*

Changes
++++++++

* Removed torrent status restriction in ``seeding_time`` and ``ratio`` condition (#19).
    - Before this version, ``seeding_time`` and ``ratio`` condition will only remove those torrents whose status are seeding. We set this restriction to provide a method for users to avoid a torrent being removed by changing its status (e.g. pause seeding).
    - But now we have a ``status`` filter, this restriction becomes unnecessary, and its behavior may be different from users expectation.

Features
+++++++++

* Supported custom remove expressions (#15).
    - Now we can write the condition that we want directly and clearly, e.g. ``remove: ratio > 1``.
    - Composite condition expressions are also supported, e.g. ``remove: (seeding_time < 86400 and ratio > 1) or (seeding_time > 86400 and ratio > 3)``. Visit Wiki to learn more.
    - The old remove conditions are still available.

Version 1.3.0
--------------

*Release Date: Wednesday, 17 April 2019*

Changes
++++++++

* Log system was updated:
    - Log path can be specified (Use ``--log`` argument, e.g. ``--log=/home/jerrymakesjelly/logs``) (#23).
    - Logs are stored in different files by day (Format: ``autoremove.%Y-%m-%d.log``).
* Changed the word ``seed`` to ``torrent`` (#25).
* Removed uncessary debug messages.

Fix
++++

* Fixed bug: Program gets stuck when there are a lot of torrents in qBittorrent client (#22).
* Fixed bug: Duplicated logging in status filter.

Version 1.2.5
--------------

*Release Date: Monday, 10 January 2019*

Fix
++++

* Fixed bug: Incorrect number of torrents in multiple strategies (#10). Thanks to @momokoo!
* Fixed bug: Incorrect number of torrents in qBittorrent (#13).

Version 1.2.4
--------------

*Release Date: Thursday, 31 May 2018*

Fix
++++

* Fixed startup failure.

Version 1.2.3
--------------

*Release Date: Wednesday, 30 May 2018*

Change
+++++++

* Now the program won't quit directly when a task goes failed.

Features
+++++++++

* Allowed to use environment variables to specify *host*, *username* and *password*.
* Allowed *username* and *password* to be empty (or one of them is empty) to log in a WebUI without username and/or password.

Version 1.2.2
--------------

*Release Date: Sunday, 27 May 2018*

Features
+++++++++

* Added new filter: Torrent Status
* Added new condition: Maximum number of torrents

Version 1.2.1
--------------

*Release Date: Saturday, 26 May 2018*

Fix
++++

* Fixed issue in *setup.py*.

Version 1.2.0
--------------

*Release Date: Saturday, 26 May 2018*

* Published to PyPI!
* Refactoring was completed.
    - New features will be added soon.
    - Now we can install it via *pip*.

Version 1.1.0
--------------

*Release Date: Monday, 14 May 2018*

* Created *setup.py*.
    - You can now use the *autoremove-torrents* command directly instead of *python3 main.py*.

Correct Document
-----------------

*Date: Wednesday, 28 March 2018*

* The *delete_data* field shouldn't be indented.

FIRST VERSION
--------------

*Release Date: Thursday, 22 March 2018*

* First version :bowtie:
