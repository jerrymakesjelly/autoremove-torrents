Auto Remove Torrents
======================
|PyPI| |GithubActionsCI| |ReadTheDocs| |Coverage| |Codacy| |Downloads| |MIT|

This program can help you to remove your torrents. Now you don't need to worry about your disk space - according to your strategies, the program will check each torrent if it satisfies the remove condition; If so, delete it automatically.

This program supports qBittorrent/Transmission/μTorrent. If you like, star it :star2: :)

Documentation: https://autoremove-torrents.readthedocs.io/en/latest/

Readme version in other languages: `简体中文`_.

.. _简体中文: https://github.com/jerrymakesjelly/autoremove-torrents/blob/master/README-cn.rst

.. |Codacy| image:: https://api.codacy.com/project/badge/Grade/6e5509ecb4714ed697c65f35d71cff65
    :target: https://www.codacy.com/app/jerrymakesjelly/autoremove-torrents?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jerrymakesjelly/autoremove-torrents&amp;utm_campaign=Badge_Grade
.. |GithubActionsCI| image:: https://github.com/jerrymakesjelly/autoremove-torrents/actions/workflows/build.yml/badge.svg?branch=master
   :target: https://github.com/jerrymakesjelly/autoremove-torrents/actions
.. |ReadTheDocs| image:: https://readthedocs.org/projects/autoremove-torrents/badge/?version=latest
   :target: https://autoremove-torrents.readthedocs.io/en/latest/?badge=latest
.. |Codacy| image:: https://app.codacy.com/project/badge/Grade/ab6f14fa9d9845b8bc8edecaf8f705e4
   :target: https://www.codacy.com/gh/jerrymakesjelly/autoremove-torrents/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jerrymakesjelly/autoremove-torrents&amp;utm_campaign=Badge_Grade
.. |Coverage| image:: https://app.codacy.com/project/badge/Coverage/ab6f14fa9d9845b8bc8edecaf8f705e4
    :target: https://www.codacy.com/gh/jerrymakesjelly/autoremove-torrents/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jerrymakesjelly/autoremove-torrents&amp;utm_campaign=Badge_Coverage
.. |MIT| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/jerrymakesjelly/autoremove-torrents/blob/master/LICENSE
.. |PyPI| image:: https://badge.fury.io/py/autoremove-torrents.svg
    :target: https://badge.fury.io/py/autoremove-torrents
.. |Downloads| image:: https://img.shields.io/pypi/dm/autoremove-torrents.svg
    :target: https://pypi.org/project/autoremove-torrents/

Requirements
-------------
* Python 2.7 or Python 3

That's all. It's a simple but smart program.


Quick Start
-------------
Installation
+++++++++++++++++++
Install from pip
^^^^^^^^^^^^^^^^^
::

    pip install autoremove-torrents

or

Install from GitHub
^^^^^^^^^^^^^^^^^^^^
::

    git clone https://github.com/jerrymakesjelly/autoremove-torrents.git
    cd autoremove-torrents
    python3 setup.py install


Write your configuration file
++++++++++++++++++++++++++++++
In order to satisfactory your needs, you have to learn how to write a configuration file. 

You can put the configuration file anywhere on your disk. The autoremove-torrents looks for ``config.yml`` in the Shell's current working directory::

    vim ./config.yml


The grammar is quite easy, for example::

    my_task:
      client: qbittorrent
      host: http://127.0.0.1
      username: admin
      password: adminadmin
      strategies:
        my_strategy:
          categories: IPT
          remove: seeding_time > 1209600 or ratio > 1
      delete_data: true

The program will delete those torrents whose categories are ``IPT``, seeding time is above 1209600 seconds **or** ratio is greater than 1. Read the `documents`_ to learn more.

.. _documents: https://autoremove-torrents.readthedocs.io/en/latest

Run
++++
::

    autoremove-torrents

If you just want to see which torrents can be removed but don't want to really remove them, use ``--view`` command line argument.


Setting up scheduled tasks
-----------------------------
If you want to check whether there is any torrent can be removed every 15 minutes, the crontab can help you. Look at the example::

    crontab -e

And then, add a line at the end of the file (please confirm the path of the autoremove-torrents and your program)::

*/15 * * * * /usr/bin/autoremove-torrents --conf=/home/jerrymakesjelly/autoremove-torrents/config.yml --log=/home/jerrymakesjelly/autoremove-torrents/logs

The ``--conf`` indicates the path to the configuration file.
The ``--log`` argument specifies the path to store the log files (Must be existed).

Screenshot
-----------
|Screenshot|

.. |Screenshot| image:: https://user-images.githubusercontent.com/6760674/40576720-a78097fe-612d-11e8-9dda-8aac0c5011a2.png

Changelog
----------
**Thu, 27 Aug 2020**: Version 1.5.3.

* Fix psutil's compatibility in Synology (use to check the free spaces). (#61)
* Enable to output debug logs by specifying ``--debug`` or ``-d`` argument. (#76)
* Fix API imcompatibility issue caused by the trailing ``/`` in host URL. (#81)
* Add uploaded size and downloaded size conditions. (#79)

**Fri, 27 Mar 2020**: Version 1.5.2.

* Support Deluge. (#8)
* Use batch delete to improve efficiency.
* Fix multi-language support in config file. (#69)
* Set the client names to be case-insensitive.

**Sat, 29 Feb 2020**: Version 1.5.1.

* Fix missing status ``StalledUpload`` and ``StalledDownload`` in version 1.5.0. (#66)

**Fri, 28 Feb 2020**: Version 1.5.0.

* Fix a problem: cannot login to client with numeric username or password. (#64)
* Fix a problem: tasks could not be executed in a Transmission without label properties.
* Fix a problem: removing conditions may not work for unlabeled and trackerless torrents.
* Fix a problem: missing status ``Queued`` in μTorrent.
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

**Mon, 3 Feb 2020**: Migrate documents to Read the Docs.

**Sun, 26 Jan 2020**: Version 1.4.9.

* Add `free_space` condition.

**Tue, 7 Jan 2020**: Version 1.4.8.

* Fix bug that cannot delete torrents in qBittorrent v4.2.1+. Sorry for any inconvenience. (#53)

**Mon, 6 Jan 2020**: Version 1.4.7.

* Add support for new API in qBittorrent 4.2.1. (#46) **Note: This version has a bug. Please upgrade to v1.4.8 or higher.**

**Tue, 17 Sep 2019**: Version 1.4.6.

* Fix problem that the tracker filter needs to specific ports when the tracker URL includes port number. (#38)

**Thu, 6 Jun 2019**: Version 1.4.5.

* Added status `StalledUpload` and `StalledDownload`. (#34)

**Wed, 22 May 2019**: Version 1.4.4.

* Fixed a bug that when condition `seed_size` / `maximum_number` is used together with condtion `ratio` / `create_time` / `seeding_time`, the task will fail. (#33)
* New feature: if the content of `filter` has only one line, now it is allowed to write down directly without using list.

**Sun, 19 May 2019**: Version 1.4.3.

* Supported Python 2.7. (#29)
* Stopped supporting Python 3.4. (kennethreitz/requests#5092)

**Mon, 13 May 2019**: Version 1.4.2.

* Fixed missing parser files. (#32)
* Fixed association of operators. (#32) Now the operator `and` and `or` are guaranteed to be left-associative.

**Mon, 6 May 2019**: Version 1.4.1.

* Fixed missing dependency: `ply`.
* Fixed the warning of duplicate definition in condition `remove`.

**Mon, 6 May 2019**: Updated Wiki.

* Added the description of `remove` condition into Simplified-Chinese Wiki.

**Wed, 1 May 2019**: Version 1.4.0.

* Removed torrent status restriction in ``seeding_time`` and ``ratio`` condition (#19).
    - Before this version, ``seeding_time`` and ``ratio`` condition will only remove those torrents whose status are seeding. We set this restriction to provide a method for users to avoid a torrent being removed by changing its status (e.g. pause seeding).
    - But now we have a ``status`` filter, this restriction becomes unnecessary, and its behavior may be different from users expectation.
* Supported custom remove expressions (#15).
    - Now we can write the condition that we want directly and clearly, e.g. ``remove: ratio > 1``.
    - Composite condition expressions are also supported, e.g. ``remove: (seeding_time < 86400 and ratio > 1) or (seeding_time > 86400 and ratio > 3)``. Visit Wiki to learn more.
    - The old remove conditions are still available.

**Wed, 17 Apr 2019**: Version 1.3.0.

* Fixed bug: Program gets stuck when there are a lot of torrents in qBittorrent client (`Issue #22 <https://github.com/jerrymakesjelly/autoremove-torrents/issues/22>`_).
* Fixed bug: Duplicated logging in status filter.
* Log system was updated:
    - Log path can be specified (Use ``--log`` argument, e.g. ``--log=/home/jerrymakesjelly/logs``) (`Issue #23 <https://github.com/jerrymakesjelly/autoremove-torrents/issues/23>`_).
    - Logs are stored in different files by day (Format: ``autoremove.%Y-%m-%d.log``).
* Changed the word ``seed`` to ``torrent`` (`Issue #25 <https://github.com/jerrymakesjelly/autoremove-torrents/issues/25>`_).
* Removed uncessary debug messages.

**Mon, 10 Jan 2019**: Version 1.2.5.

* Fixed bug: Incorrect number of torrents in multiple strategies (`Issue #10 <https://github.com/jerrymakesjelly/autoremove-torrents/issues/10>`_, thanks to @momokoo for the report and PR).
* Fixed bug: Incorrect number of torrents in qBittorrent (`Issue #13 <https://github.com/jerrymakesjelly/autoremove-torrents/issues/13>`_).

**Thu, 31 May 2018**: Version 1.2.4.

* Fixed startup failure.

**Wed, 30 May 2018**: Version 1.2.3. Added new features.

* Allowed to use environment variables to specify *host*, *username* and *password*.
* Allowed *username* and *password* to be empty (or one of them is empty) to log in a WebUI without username and/or password.
* Now the program won't quit directly when a task goes failed.

**Sun, 27 May 2018**: Version 1.2.2. Added new features :smile:

* Added new filter: Torrent Status
* Added new condition: Maximum number of torrents

**Sat, 26 May 2018**: Version 1.2.1. Fixed issue in *setup.py*.

**Sat, 26 May 2018**: Version 1.2.0. Refactoring was completed, and was published to PyPI.

* New features will be added soon.
* Now we can install it via *pip*.

**Mon, 14 May 2018**: Version 1.1.0. Created *setup.py*.

You can now use the *autoremove-torrents* command directly instead of *python3 main.py*.

**Wed, 28 Mar 2018**: (Correct document) The *delete_data* field shouldn't be indented.

**Thu, 22 Mar 2018**: First version :bowtie:

TODO List
-----------
Depend on users' feedback. If you have any problem, please submit `issues`_.

.. _issues: https://github.com/jerrymakesjelly/autoremove-torrents/issues

`Click here`_ to see the TODO List.

.. _Click here: https://github.com/jerrymakesjelly/autoremove-torrents/issues/63
