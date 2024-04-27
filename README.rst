Auto Remove Torrents
======================
|PyPI| |GithubActionsCI| |ReadTheDocs| |Coverage| |Codacy| |Downloads| |MIT|

This program can help you to remove your torrents. Now you don't need to worry about your disk space - according to your strategies, the program will check each torrent if it satisfies the remove condition; If so, delete it automatically.

This program supports qBittorrent/Transmission/μTorrent. If you like, star it :star2: :)

Documentation: https://autoremove-torrents.readthedocs.io/en/latest/

Readme version in other languages: `简体中文`_.

.. _简体中文: https://github.com/jerrymakesjelly/autoremove-torrents/blob/master/README-cn.rst

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

We recommend you to use Python 3.6 or higher version of Python.


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

.. |Screenshot| image:: https://user-images.githubusercontent.com/6760674/174464634-15743d59-f1dc-41c9-bff6-6d90becaeb67.gif

Changelog
--------------

**Sat, 27 Apr 2024**: Version 1.5.5.

* Fix the compatibility issues in qBittorrent 4.5 and later. (#157) (#173) (#174) (#182) (#186) Thanks to @Siriussee!
    - See the API changes in qbittorrent/qBittorrent#17563.

We also fix the unittest workflow for the lastest qBittorrent. Thanks to @amefs!

`More changelogs`_

.. _More changelogs: https://autoremove-torrents.readthedocs.io/en/latest/changelog.html

TODO List
-----------
Depend on users' feedback. If you have any problem, please submit `issues`_.

.. _issues: https://github.com/jerrymakesjelly/autoremove-torrents/issues

`Click here`_ to see the TODO List.

.. _Click here: https://github.com/jerrymakesjelly/autoremove-torrents/issues/63
