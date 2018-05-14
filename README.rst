﻿Auto Remove Torrents
======================

.. image:: https://api.codacy.com/project/badge/Grade/b2d4a371eb964a309af7fc8740769cb7
   :alt: Codacy Badge
   :target: https://app.codacy.com/app/jerrymakesjelly/autoremove-torrents?utm_source=github.com&utm_medium=referral&utm_content=jerrymakesjelly/autoremove-torrents&utm_campaign=badger
|TravisCI| |MIT|

This script can help you to remove your torrents. Now you don't need to worry about your disk space - according to your strategies, for each category and tracker, the script will check each torrent if it satisfies the remove condition; If so, delete it automatically.

This smart script supports qBittorrent/Transmission/μTorrent. If you like, star it :sparkles: :)

.. |TravisCI| image:: https://www.travis-ci.org/jerrymakesjelly/autoremove-torrents.svg?branch=master
   :target: https://www.travis-ci.org/jerrymakesjelly/autoremove-torrents
.. |MIT| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/jerrymakesjelly/autoremove-torrents/blob/master/LICENSE

Requirements
-------------
* Python 3

That's all. It's a simple but smart script.


Installation
-------------
Download the codes and set up
+++++++++++++++++++
::

    git clone https://github.com/jerrymakesjelly/autoremove-torrents.git
    python3 setup.py install


Write your configuration file
++++++++++++++++++++++++++++++
In order to satisfactory your needs, you have to learn how to write a configuration file. 

You can put the configuration file anywhere on your disk. The autoremove-torrents looks for *config.yml* in the Shell's current working directory.::

    cd autoremove-torrents
    vim ./config.yml


The grammar is quite easy, for example::

    my_task:
      client: qbittorrent
      host: http://127.0.0.1
      username: admin
      password: adminadmin
      strategies:
        my_strategy:
          categories:
            - IPT
          seeding_time: 1209600
          ratio: 1
      delete_data: true


The script will delete those torrents whose categories are IPT, seeding time is above 1209600 seconds **or** ratio is greater than 1. Visit `Wiki`_ to learn more.

.. _Wiki: https://github.com/jerrymakesjelly/autoremove-torrents/wiki

Run
++++
::

    autoremove-torrents

If you just want to see which torrents can be removed but don't want to really remove them, use --view command line argument.


Setting up scheduled tasks
-----------------------------
If you want to check whether there is any torrent can be removed every 15 minutes, the crontab can help you. Look at the example::

    crontab -e

And then, add a line at the end of the file (please confirm the path of the autoremove-torrents and your script)::

*/15 * * * * /usr/bin/autoremove-torrents --conf=/home/jerrymakesjelly/autoremove-torrents/config.yml

The *conf=* indicates the path to the configuration file.


Changelog
----------
**Mon, 14 May 2018**: Created *setup.py*.

    You can now use the *autoremove-torrents* command directly instead of *python3 main.py*.

**Wed, 28 Mar 2018**: (Correct document) The *delete_data* field shouldn't be indented.

**Thu, 22 Mar 2018**: First version :bowtie:

TODO List
-----------
Depend on users' feedback.

* Support Deluge and rtorrent in the future

* Add remove condition: Disk free space

* Add remove condition: Max/Min average UL/DL speed

* The file *autoremove.py* is too long to maintain, I should reconstruct it using OOP.

If you have any problem, please submit `Issues`_.

.. _Issues: https://github.com/jerrymakesjelly/autoremove-torrents/issues