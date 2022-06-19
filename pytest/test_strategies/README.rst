About Test Data
================

To check the correctness of the strategies' implementation, we have prepared a torrent list and some environment parameters. They're stored in `data.json`, `environment.json` and `clientstatus.json`, respectively.

The tester will set some of interfaces return specific values and feed the torrent list into autoremove-torrents. And then, the tester will check whether the autoremove-torrents removes the expected torrents.

Environment
------------

This file mocks the environment. Currently the time and the free space are set to fixed values.

.. list-table::
   :header-rows: 1

   * - Key
     - Value
   * - `time.time`
     - 1527438305 (Sun May 27 2018 16:25:05 GMT+0000)
   * - `psutil.disk_usage`
     - 107374182400 (100 GiB)
   * - `shutil.disk_usage`
     - 107374182400 (100 GiB)

Client Status
--------------

We also mocked the client status, mainly for testing the `remote_free_space`.

.. list-table::
   :header-rows: 1

   * - Key
     - Value
   * - Download Speed
     - 5386771 (approx. 5.14 MiB/s)
   * - Upload Speed
     - 45239782 (approx. 43.14 MiB/s)
   * - Total Downloaded
     - 136217978800 (approx. 126.86 GiB)
   * - Total Uploaded
     - 38697636454675 (approx. 35.20 TiB)
   * - Free Space
     - 107374182400 (100 GiB)
   * - Port Status
     - Open

Torrent List
-------------

Currently we created 16 torrents for testing.

In order to facilitate writing test cases, we recorded the results of the torrent list sorted by certain fields, for future reference.

Sort by Create Time, Ascending
+++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - added_on
     - Category
     - Tracker
     - State
   * - Torrent - 9
     - 1525969391
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 4
     - 1525970567
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 5
     - 1526712743
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 2
     - 1526720005
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 6
     - 1526721182
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 8
     - 1526721182
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 10
     - 1526721182
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 3
     - 1526731573
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 7
     - 1526733335
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 1
     - 1526736631
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 11
     - 1526738139
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 12
     - 1526738305
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 16
     - 1527335739
     - 
     - 
     - Stopped
   * - Torrent - 14
     - 1527335909
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 13
     - 1527339181
     - 
     - 
     - Checking
   * - Torrent - 15
     - 1527343104
     - 
     - 
     - Paused

Sort by Downloading Time, Ascending
++++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - downloading_time
     - Category
     - Tracker
     - State
   * - Torrent - 13
     - 1
     -
     - 
     - Checking
   * - Torrent - 14
     - 2
     -
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 15
     - 3
     -
     - 
     - Paused
   * - Torrent - 16
     - 4
     -
     - 
     - Stopped
   * - Torrent - 10
     - 120
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 9
     - 4932
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 2
     - 5022
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 8
     - 23033
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 3
     - 25933
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 4
     - 39203
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 1
     - 41322
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 5
     - 42003
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 12
     - 43222
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 6
     - 43233
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 11
     - 43322
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 7
     - 66992
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading

Sort by Finishing Time, Ascending
++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - completion_on
     - Category
     - Tracker
     - State
   * - Torrent - 9
     - 1525969428
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 4
     - 1525970677
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 5
     - 1526723020
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 8
     - 1526731123
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 3
     - 1526732525
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 10
     - 1526735607
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 6
     - 1526736296
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 7
     - 1526738269
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 16
     - 1527335868
     - 
     - 
     - Stopped
   * - Torrent - 14
     - 1527335960
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 13
     - 1527342372
     - 
     - 
     - Checking
   * - Torrent - 15
     - 1527350573
     - 
     - 
     - Paused
   * - Torrent - 1
     - 4294967295
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 2
     - 4294967295
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 11
     - 4294967295
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 12
     - 4294967295
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading

Sort by Download Speed Limit, Ascending
++++++++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - dl_limit
     - Category
     - Tracker
     - State
   * - Torrent - 1
     - 0
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 2
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 3
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 4
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 5
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 6
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 7
     - 0
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 8
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 9
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 10
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 11
     - 0
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 12
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 13
     - 0
     - 
     - 
     - Checking
   * - Torrent - 14
     - 0
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 15
     - 0
     - 
     - 
     - Paused
   * - Torrent - 16
     - 0
     - 
     - 
     - Stopped

Sort by Average Download Speed, Ascending
++++++++++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - dl_speed_avg
     - Category
     - Tracker
     - State
   * - Torrent - 2
     - 188567
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 1
     - 499524
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 15
     - 2708163
     - 
     - 
     - Paused
   * - Torrent - 12
     - 3792899
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 10
     - 4306811
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 6
     - 4633382
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 4
     - 5019202
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 3
     - 5584975
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 9
     - 6112945
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 11
     - 6403655
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 16
     - 7002425
     - 
     - 
     - Stopped
   * - Torrent - 8
     - 7062911
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 5
     - 7858040
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 7
     - 9855309
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 14
     - 9987804
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 13
     - 10211715
     - 
     - 
     - Checking

Sort by Current Download Speed, Ascending
++++++++++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - dlspeed
     - Category
     - Tracker
     - State
   * - Torrent - 3
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 4
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 5
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 6
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 7
     - 0
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 8
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 9
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 10
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 13
     - 0
     - 
     - 
     - Checking
   * - Torrent - 14
     - 0
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 15
     - 0
     - 
     - 
     - Paused
   * - Torrent - 16
     - 0
     - 
     - 
     - Stopped
   * - Torrent - 12
     - 269870
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 11
     - 302084
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 2
     - 1583918
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 1
     - 2270401
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading

Sort by Amount of Downloaded Data, Ascending
+++++++++++++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - downloaded
     - Category
     - Tracker
     - State
   * - Torrent - 4
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 9
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 14
     - 312891624
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 3
     - 347198660
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 16
     - 1139339147
     - 
     - 
     - Stopped
   * - Torrent - 12
     - 1716876766
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 13
     - 1747429022
     - 
     - 
     - Checking
   * - Torrent - 15
     - 2127119819
     - 
     - 
     - Paused
   * - Torrent - 11
     - 2321882559
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 1
     - 5710905998
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 7
     - 7240240790
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 8
     - 7621738011
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 5
     - 9628171953
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 6
     - 13201638292
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 10
     - 14846696889
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 2
     - 19053990510
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading

Sort by Amount of Downloaded Data in Current Session, Ascending
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - downloaded_session
     - Category
     - Tracker
     - State
   * - Torrent - 4
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 9
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 14
     - 312891624
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 3
     - 347198660
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 16
     - 1139339147
     - 
     - 
     - Stopped
   * - Torrent - 12
     - 1716876766
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 13
     - 1747429022
     - 
     - 
     - Checking
   * - Torrent - 15
     - 2127119819
     - 
     - 
     - Paused
   * - Torrent - 11
     - 2321882559
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 1
     - 5710905998
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 7
     - 7240240790
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 8
     - 7621738011
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 5
     - 9628171953
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 6
     - 13201638292
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 10
     - 14846696889
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 2
     - 19053990510
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading

Sort by ETA (Estimated Time of Arrival), Ascending
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - eta
     - Category
     - Tracker
     - State
   * - Torrent - 1
     - 4173
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 2
     - 4778
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 12
     - 6187
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 11
     - 41004
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 3
     - 8640000
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 4
     - 8640000
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 5
     - 8640000
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 6
     - 8640000
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 7
     - 8640000
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 8
     - 8640000
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 9
     - 8640000
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 10
     - 8640000
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 13
     - 8640000
     - 
     - 
     - Checking
   * - Torrent - 14
     - 8640000
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 15
     - 8640000
     - 
     - 
     - Paused
   * - Torrent - 16
     - 8640000
     - 
     - 
     - Stopped

Sort by Last Active Time, Ascending
++++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - last_activity
     - Category
     - Tracker
     - State
   * - Torrent - 9
     - 1526730151
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 5
     - 1526742178
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 3
     - 1526742212
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 7
     - 1526742523
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 1
     - 1526742631
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 2
     - 1526742632
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 6
     - 1526742633
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 8
     - 1526742634
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 10
     - 1526742635
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 11
     - 1526742636
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 12
     - 1526742637
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 14
     - 1527350136
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 15
     - 1527351309
     - 
     - 
     - Paused
   * - Torrent - 13
     - 1527351767
     - 
     - 
     - Checking
   * - Torrent - 16
     - 1527352055
     - 
     - 
     - Stopped
   * - Torrent - 4
     - Never Active
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading

.. list-table::
   :header-rows: 1

   * - Name
     - num_complete
     - Category
     - Tracker
     - State
   * - Torrent - 1
     - 1
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 2
     - 1
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 11
     - 1
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 12
     - 1
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 15
     - 1
     - 
     - 
     - Paused
   * - Torrent - 9
     - 8
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 4
     - 9
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 14
     - 28
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 5
     - 36
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 3
     - 40
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 13
     - 57
     - 
     - 
     - Checking
   * - Torrent - 8
     - 70
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 16
     - 72
     - 
     - 
     - Stopped
   * - Torrent - 6
     - 73
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 7
     - 74
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 10
     - 115
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading

Sort by Number of Leechers, Ascending
++++++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - num_incomplete
     - Category
     - Tracker
     - State
   * - Torrent - 14
     - 1
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 4
     - 2
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 5
     - 2
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 13
     - 2
     - 
     - 
     - Checking
   * - Torrent - 9
     - 5
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 7
     - 7
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 8
     - 8
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 6
     - 16
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 10
     - 23
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 3
     - 24
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 16
     - 48
     - 
     - 
     - Stopped
   * - Torrent - 15
     - 58
     - 
     - 
     - Paused
   * - Torrent - 12
     - 80
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 11
     - 87
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 2
     - 98
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 1
     - 111
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading

Sort by Number of Connected Leechers, Ascending
++++++++++++++++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - num_leechs
     - Category
     - Tracker
     - State
   * - Torrent - 3
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 4
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 7
     - 0
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 9
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 13
     - 0
     - 
     - 
     - Checking
   * - Torrent - 14
     - 0
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 5
     - 1
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 15
     - 1
     - 
     - 
     - Paused
   * - Torrent - 16
     - 1
     - 
     - 
     - Stopped
   * - Torrent - 8
     - 3
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 6
     - 8
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 10
     - 9
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 12
     - 81
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 2
     - 94
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 11
     - 96
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 1
     - 111
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading

Sort by Number of Connected Seeders, Ascending
+++++++++++++++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - num_seeds
     - Category
     - Tracker
     - State
   * - Torrent - 2
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 3
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 4
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 5
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 6
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 7
     - 0
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 8
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 9
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 10
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 11
     - 0
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 13
     - 0
     - 
     - 
     - Checking
   * - Torrent - 14
     - 0
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 15
     - 0
     - 
     - 
     - Paused
   * - Torrent - 16
     - 0
     - 
     - 
     - Stopped
   * - Torrent - 1
     - 1
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 12
     - 1
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading

Sort by Priority, Ascending
++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - priority
     - Category
     - Tracker
     - State
   * - Torrent - 3
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 4
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 5
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 6
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 7
     - 0
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 8
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 9
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 10
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 13
     - 0
     - 
     - 
     - Checking
   * - Torrent - 14
     - 0
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 15
     - 0
     - 
     - 
     - Paused
   * - Torrent - 16
     - 0
     - 
     - 
     - Stopped
   * - Torrent - 2
     - 1
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 1
     - 2
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 11
     - 3
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 12
     - 4
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading

Sort by Progress, Ascending
++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - progress
     - Category
     - Tracker
     - State
   * - Torrent - 11
     - 0.1686464548110962
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 1
     - 0.41469237208366394
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 12
     - 0.42562440037727356
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 2
     - 0.6825178861618042
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 3
     - 1
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 4
     - 1
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 5
     - 1
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 6
     - 1
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 7
     - 1
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 8
     - 1
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 9
     - 1
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 10
     - 1
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 13
     - 1
     - 
     - 
     - Checking
   * - Torrent - 14
     - 1
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 15
     - 1
     - 
     - 
     - Paused
   * - Torrent - 16
     - 1
     - 
     - 
     - Stopped

Sort by Ratio, Ascending
+++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - ratio
     - Category
     - Tracker
     - State
   * - Torrent - 14
     - 0.3445761398841408
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 16
     - 0.3471540015468283
     - 
     - 
     - Stopped
   * - Torrent - 13
     - 1.0864970777622807
     - 
     - 
     - Checking
   * - Torrent - 1
     - 1.4996836633275643
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 15
     - 1.5625674295877547
     - 
     - 
     - Paused
   * - Torrent - 6
     - 1.774056700159135
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 10
     - 2.1814983806934514
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 9
     - 2.299265075053725
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 3
     - 2.3415569000179897
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 12
     - 2.362675595785889
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 11
     - 2.4767990644956646
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 7
     - 2.6040875125369967
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 2
     - 2.7093276943696765
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 5
     - 3.0506702583191805
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 8
     - 4.290462671611765
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 4
     - 4.3127607705602315
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading

Sort by Remaining Size to Be Finished, Ascending
+++++++++++++++++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - remaining
     - Category
     - Tracker
     - State
   * - Torrent - 3
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 4
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 5
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 6
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 7
     - 0
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 8
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 9
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 10
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 13
     - 0
     - 
     - 
     - Checking
   * - Torrent - 14
     - 0
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 15
     - 0
     - 
     - 
     - Paused
   * - Torrent - 16
     - 0
     - 
     - 
     - Stopped
   * - Torrent - 12
     - 2315255556
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 1
     - 8055324533
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 2
     - 8863615408
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 11
     - 11445911552
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading

Sort by Seeding Time, Ascending
++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - seeding_time
     - Category
     - Tracker
     - State
   * - Torrent - 13
     - 1
     - 
     - 
     - Checking
   * - Torrent - 14
     - 2
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 15
     - 3
     - 
     - 
     - Paused
   * - Torrent - 16
     - 4
     - 
     - 
     - Stopped
   * - Torrent - 10
     - 856
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 9
     - 6085
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 2
     - 7025
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 8
     - 8041
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 6
     - 11328
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 11
     - 30667
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 5
     - 34818
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 12
     - 39155
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 3
     - 41683
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 4
     - 58388
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 1
     - 61382
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 7
     - 73801
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading

Sort by Last Seen Complete, Ascending
++++++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - seen_complete
     - Category
     - Tracker
     - State
   * - Torrent - 4
     - 1526614351
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 9
     - 1526730169
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 2
     - 1526739352
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 7
     - 1526739648
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 3
     - 1526741130
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 5
     - 1526742181
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 8
     - 1526742225
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 11
     - 1526742464
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 1
     - 1526742547
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 6
     - 1526742572
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 10
     - 1526742579
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 12
     - 1526742614
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 16
     - 1527345392
     - 
     - 
     - Stopped
   * - Torrent - 13
     - 1527349645
     - 
     - 
     - Checking
   * - Torrent - 14
     - 1527349962
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 15
     - 1527351233
     - 
     - 
     - Paused

Sort by Size, Ascending
++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - size
     - Category
     - Tracker
     - State
   * - Torrent - 14
     - 312186667 (0.29 GiB)
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 3
     - 347000034 (0.32 GiB)
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 16
     - 1132013553 (1.05 GiB)
     - 
     - 
     - Stopped
   * - Torrent - 13
     - 1746686185 (1.63 GiB)
     - 
     - 
     - Checking
   * - Torrent - 15
     - 2126568405 (1.98 GiB)
     - 
     - 
     - Paused
   * - Torrent - 9
     - 3022394751 (2.81 GiB)
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 12
     - 4030908717 (3.75 GiB)
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 7
     - 7239185152 (6.74 GiB)
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 8
     - 7619309310 (7.10 GiB)
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 5
     - 9627866528 (8.96 GiB)
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 4
     - 10152029087 (9.45 GiB)
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 6
     - 13200820552 (12.29 GiB)
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 1
     - 13762548460 (12.817 GiB)
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 11
     - 13767802684 (12.822 GiB)
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 10
     - 14844911534 (13.83 GiB)
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 2
     - 27918469580 (26.00 GiB)
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading

Sort by Total Size, Ascending
++++++++++++++++++++++++++++++

This size includes the size of unselected files.

.. list-table::
   :header-rows: 1

   * - Name
     - total_size
     - Category
     - Tracker
     - State
   * - Torrent - 14
     - 312186667
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 3
     - 347000034
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 16
     - 1132013553
     - 
     - 
     - Stopped
   * - Torrent - 13
     - 1746686185
     - 
     - 
     - Checking
   * - Torrent - 15
     - 2126568405
     - 
     - 
     - Paused
   * - Torrent - 9
     - 3022394751
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 12
     - 4030908717
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 7
     - 7239185152
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 8
     - 7619309310
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 5
     - 9627866528
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 4
     - 10152029087
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 6
     - 13200820552
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 1
     - 13762548460
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 11
     - 13767802684
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 10
     - 14844911534
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 2
     - 27918469580
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading

Sort by Upload Speed Limit, Ascending
++++++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - up_limit
     - Category
     - Tracker
     - State
   * - Torrent - 1
     - 0
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 2
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 3
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 4
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 5
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 6
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 7
     - 0
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 8
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 9
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 10
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 11
     - 0
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 12
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 13
     - 0
     - 
     - 
     - Checking
   * - Torrent - 14
     - 0
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 15
     - 0
     - 
     - 
     - Paused
   * - Torrent - 16
     - 0
     - 
     - 
     - Stopped

Sort by Average Upload Speed, Ascending
++++++++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - up_speed_avg
     - Category
     - Tracker
     - State
   * - Torrent - 6
     - 37146
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 1
     - 78804
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 10
     - 152048
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 12
     - 254117
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 3
     - 456008
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 14
     - 482248
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 11
     - 586125
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 13
     - 661650
     - 
     - 
     - Checking
   * - Torrent - 8
     - 801737
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 2
     - 808605
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 7
     - 812996
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 4
     - 832684
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 5
     - 851779
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 9
     - 900793
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 16
     - 924258
     - 
     - 
     - Stopped
   * - Torrent - 15
     - 950107
     - 
     - 
     - Paused

Sort by Amount of Uploaded Data, Ascending
+++++++++++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - uploaded
     - Category
     - Tracker
     - State
   * - Torrent - 14
     - 107814988
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 16
     - 395526144
     - 
     - 
     - Stopped
   * - Torrent - 3
     - 812985418
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 13
     - 1898576526
     - 
     - 
     - Checking
   * - Torrent - 15
     - 3323768148
     - 
     - 
     - Paused
   * - Torrent - 12
     - 4056422836
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 11
     - 5750836550
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 9
     - 6949286694
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 1
     - 8564552428
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 7
     - 18854220629
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 6
     - 23420454865
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 5
     - 29372377819
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 10
     - 32388045222
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 8
     - 32700782429
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 4
     - 43783272788
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 2
     - 51623504177
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading

Sort by Amount of Uploaded Data in Current Session, Ascending
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - uploaded_session
     - Category
     - Tracker
     - State
   * - Torrent - 4
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 9
     - 26198016
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 14
     - 107814988
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 16
     - 395526144
     - 
     - 
     - Stopped
   * - Torrent - 3
     - 812985418
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 13
     - 1898576526
     - 
     - 
     - Checking
   * - Torrent - 15
     - 3323768148
     - 
     - 
     - Paused
   * - Torrent - 12
     - 4056422836
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 11
     - 5750836550
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 1
     - 8564552428
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 7
     - 18854220629
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 6
     - 23420454865
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 5
     - 29372377819
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 10
     - 32388045222
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 8
     - 32700782429
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 2
     - 51623504177
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading

Sort by Current Upload Speed, Ascending
++++++++++++++++++++++++++++++++++++++++++

.. list-table::
   :header-rows: 1

   * - Name
     - upspeed
     - Category
     - Tracker
     - State
   * - Torrent - 3
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 4
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 5
     - 0
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 7
     - 0
     - Category - 1
     - https://tracker.site1.com/announce
     - Uploading
   * - Torrent - 9
     - 0
     - Category - 3
     - http://tracker.site3.com/?action=announce
     - Uploading
   * - Torrent - 13
     - 0
     - 
     - 
     - Checking
   * - Torrent - 14
     - 0
     - 
     - https://www.site2.org/tracker/announce
     - Queued
   * - Torrent - 15
     - 0
     - 
     - 
     - Paused
   * - Torrent - 16
     - 8055
     - 
     - 
     - Stopped
   * - Torrent - 8
     - 87463
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 6
     - 121201
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 10
     - 327541
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Uploading
   * - Torrent - 11
     - 442042
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 12
     - 668038
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading
   * - Torrent - 1
     - 984644
     - Category - 1
     - https://tracker.site1.com/announce
     - Downloading
   * - Torrent - 2
     - 2886504
     - Category - 2
     - https://www.site2.org/tracker/announce
     - Downloading

