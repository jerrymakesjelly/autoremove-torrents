.. _config:

Configuration
=============

Before we run ``autoremove-torrents``, we need to create a ``config.yml`` to save our configurations.

The script uses the YAML language as the language of the configuration file. The YAML language has a clear structure, so I think it's more friendly than the JSON and easy to learn.

Look at the example please, the task block can be divided into 3 parts.

.. code-block:: yaml

   # A task block
   my_task:          # Part 1: Task Name
     # Part 2: Login Information
     client: qbittorrent
     host: http://127.0.0.1:9091
     username: admin
     password: adminadmin
     # Part 3: Strategies Block (Remove Conditions)
     strategies:
       strategy1:    # Part I: Strategy Name
         # Part II: Filters
         categories:
           - IPT
         # Part III: Remove Condition
         ratio: 1
         seeding_time: 1209600
       strategy2:
         all_categories: true
         excluded_categories:
           - IPT
         seeding_time: 259200
       # Add more strategies here...
     # Part 4: Decide whether to remove and delete data (optional)
     delete_data: true

   # Add more tasks here...


Centainly, the configuration file can contain more than one task blocks, and a task block can contain more than one strategy blocks. Each task block represents a BT client, and each strategy block represents a kind of torrents.

Part 1: Task Name
-----------------

Just name your task.

.. note::

   No spaces are allowed before the task name.


Part 2: Login Information
-------------------------

This script works with your client's WebUI, and this part is your login inforamtion. 

* ``client``: Your client name. Now it supports qbittorrent/transmission/μTorrent.
* ``host``: The URL of your client's WebUI, and the URL must have a socket (http:// or https://).
* ``username``: The username of the WebUI.
* ``password``: The password of the WebUI.

Part 3: Strategy Block
----------------------
This part contains strategy blocks. Each strategy block can be divided into 3 parts, too.

Part I: Strategy Name
+++++++++++++++++++++

Just name your strategy like the task name.

Part II: Filters
++++++++++++++++

This strategy is available only for the torrents you chosen. There are 9 filters available.

* ``all_trackers``/``all_categories``/``all_status``: Choose all the trackers/categories/status.
* ``categories``: Choose torrents in these categories.
* ``excluded_categories``: Don't choose torrents in these categories.
* ``trackers``: Choose torrents in these trackers.
* ``excluded_trackers``: Don't choose torrents in these trackers.
* ``status``: Choose torrents in these status. Available status is as follows:

.. list-table::
   :header-rows: 1

   * - Status
     - Remarks
   * - Downloading
     - /
   * - Uploading
     - /
   * - Checking
     - /
   * - Queued
     - /
   * - Paused
     - Transmission doesn't have this status.
   * - Stopped
     - qBittorrent doesn't have this status.
   * - Error
     - /
   * - StalledUpload
     - μTorrent doesn't have this status.
   * - StalledDownload
     - μTorrent doesn't have this status.

* ``excluded_status``: Don't choose these torrents in these status. Available status is shown in the table above.

The result of each filter is a set of torrents. 

.. note::

   When two or three of ``categories``, ``trackers`` and ``status`` filter are specificed, the program will take the intersection of these sets, and subtracts set ``excluded_categories``, ``excluded_trackers`` and ``excluded_status``.


.. note::

   1. Don't write sockets in ``trackers``. The ``trackers`` field only needs hostname, for example, just fill ``tracker.site1.com`` for ``https://tracker.site1.com``.
   2. In 1.4.4 and later version, if there's only one item in ``categories``, ``trackers`` or ``status``, it's not necessary to use list structure. A single-line text is enough, for example:

   .. code-block:: yaml

      categories: cata1
   

   .. code-block:: yaml

      status: uploading
   

   3. The ``StalledUp`` and ``StalledDown`` is the new status in version 1.4.5. In this program, ``Uploading`` inlcudes the torrents in ``StalledUpload`` status, and ``Downloading`` includes the torrents in ``StalledDownload`` status.

Part III: Remove Condition
++++++++++++++++++++++++++

There are 2 ways to set removing condition.

1. Use Removing Condition Keywords Directly
###########################################

Use the removing condition keywords directly. There are 18 remove conditions. 

.. note::

   As long as a chosen torrent satisfies one of these conditions, it will be removed.

The first 15 conditions are here.

.. list-table::
   :header-rows: 1
   
   * - Condition
     - Unit
     - Description
   * - ``ratio``
     -
     - Maximum ratio
   * - ``create_time``
     - Second
     - The maximum time elapsed since the torrent was added to the client. When a torrent reaches the limit, it will be removed (no matter what state it is).
   * - ``seeding_time``
     - Second
     - Maximum seeding time of a torrent.
   * - ``max_downloadspeed``
     - KiB/s
     - Maximum download speed of a torrent. Torrents that exceed the limitation will be removed.
   * - ``min_uploadspeed``
     - KiB/s
     - Minimum upload speed of a torrent. Torrents below this speed will be removed.
   * - ``max_average_downloadspeed``
     - KiB/s
     - Maximum average download speed. Just like ``max_downloadspeed``.
   * - ``min_average_uploadspeed``
     - KiB/s
     - Minimum average upload speed. Just like ``min_uploadspeed``.
   * - ``max_size``
     - GiB
     - Torrent size limitation. Remove those torrents whose size exceeds the limit.
   * - ``max_seeder``
     - 
     - Maximum number of seeders. When the seeders exceeds the limitation, the torrent will be removed.
   * - ``min_leecher``
     - 
     - Minimum number of leechers. When the number of leechers is less than the settings, the torrent will be removed.
   * - ``max_connected_seeder``
     -
     - Maximum number of connected seeders. Just like ``max_seeder``.
   * - ``min_connected_leecher``
     -
     - Minimum number of connected leechers. Just like ``min_leecher``.
   * - ``last_activity``
     - Second
     - The maximum time allowed since a torrent has stopped being active, that is, the maximum time without uploading or downloading. When the torrent reaches the limit, it will be removed.
   * - ``max_progress``
     - Percent (%)
     - The maximum download progress. The maximum value is 100.
   * - ``upload_ratio``
     - 
     - The maximum upload ratio. Note that the upload ratio here is different from the ratio. For each torrent, the upload ratio is ``uploaded size`` divided by its ``size``.

Beside these condition, the other 3 remove conditions are here. The rest of the torrents will be removed if they trigger these conditions.

* ``seed_size``: Calculate the total size of the torrents you chosen. If the total size exceeds the limit, some of the torrents will be removed. The following two properties must be specificed.
  
  - ``limit``: Limit of the total size, in GiB.
  - ``action``: Determine which torrents will be removed. Can be the following values:

  .. list-table::
     :header-rows: 1
  
     * - Value
       - Description
     * - remove-old-seeds
       - Try to remove old seeds.
     * - remove-new-seeds
       - Try to remove new seeds.
     * - remove-big-seeds
       - Try to remove large seeds.
     * - remove-small-seeds
       - Try to remove small seeds.
     * - remove-active-seeds
       - Try to remove active seeds.
     * - remove-inactive-seeds
       - Try to remove inactive seeds.


* ``maximum_number``: Set the maximum number of torrents. When the number of chosen torrents is exceed the maximum number, some of the torrents will be deleted, just like the condition `seed_size`. The following two properties must be specified:
  
  - ``limit``: Maximum number limitation
  - ``action``: Determine which torrents will be removed. The values and its meanings are in the table above.

* ``free_space``: Check the free space on disk is enough or not. When the free space is not enough, some of the chosen torrents will be deleted, just like the condition `seed_size`. The following three properties should be specified:
  
  - ``min``: Minimum free space, in `GiB`. When the free space of the specified directory is less than this value, the removing strategy will be trigger.
  - ``path``: Directory that needs to be monitored
  - ``action``: Removing strategy, which determines which torrents will be removed. The values and its meanings are in the table above.

Here is an example. It removes the torrents which ratio is greater than 1 or seeding time is more than 1209600 seconds:

.. code-block:: yaml

   ratio: 1
   seeding_time: 1209600


Here is another example. It removes the torrents which seeding time is greater than 259200 seconds:

.. code-block:: yaml

   seeding_time: 259200


Here is another another example. When the free space in directory `/home/myserver/downloads` is less than 10GiB, the program will try to remove the big torrents:

.. code-block:: yaml    

   free_space:
     min: 10
     path: /home/myserver/downloads
     action: remove-big-seeds


2. Use ``remove`` Keyword
#########################

Use the ``remove`` keyword. The ``remove`` keyword is a new keyword in version 1.4.0, which supports the complex removing condition. The ``remove`` keyword is followed by an expression, which consists of the following syntax:

1. ``<Parameter> <Comparison Operator> <Value>``

   ``Parameter``: Available parameters are as follows, and they are case-insensitive. More parameters will be added to the program later.

   .. list-table::
      :header-rows: 1
       
      * - Parameter
        - Unit
        - Description
      * - ``average_downloadspeed``
        - KiB/s
        - Average download speed.
      * - ``average_uploadspeed``
        - KiB/s
        - Average upload speed.
      * - ``connected_leecher``
        - /
        - The number of connected leecher.
      * - ``connected_seeder``
        - /
        - The number of connected seeder.
      * - ``create_time``
        - Second
        - The elapsed time since the torrent was added to the client.
      * - ``download_speed``
        - KiB/s
        - Download speed.
      * - ``last_activity``
        - Second
        - The elapsed time since the torrent has stopped being active (without uploading or downloading).
      * - ``leecher``
        - /
        - The number of leechers.
      * - ``progress``
        - %
        - The download progress.
      * - ``ratio``
        - /
        - Ratio
      * - ``seeder``
        - /
        - The number of seeders.
      * - ``seeding_time``
        - Second
        - Seeding time.
      * - ``size``
        - GiB
        - The torrent size.
      * - ``upload_ratio``
        - /
        - uploaded size / size
      * - ``upload_speed``
        - /
        - Upload Speed

   ``Comparison Operator``: Available parameters are as follows. This program doesn't provide the ``equal`` sign, because the status data of the torrents change quickly, and usually it's meaningless to set a specific value.

   .. list-table::
      :header-rows: 1
       
      * - Comparison Operator
        - Description
      * - ``<``
        - Less Than
      * - ``>``
        - Greater Than

   ``Value``: Specify a numeric value. Supports integers and floats.

   This syntax selects the eligible torrents directly, and removes them directly or works with the following compound expressions. Here is an example, it removes the torrents which seeding time is greater than 259200 seconds:

   .. code-block:: yaml

      remove: seeding_time > 259200
    

2. ``<Expression 1> and <Expression 2>`` and ``<Expression 1> or <Expression 2>``

   This syntax is a compound expression.

   * ``and``: Select torrents that meet both the ``Expression 1`` and ``Expression 2`` (intersection).
   * ``or``: Select torrents that meet one or both of the ``Expression 1`` and ``Expression 2`` (Union).

   Here is an example. It removes the torrents which ratio is greater than 2 **and** seeding time is more than 60000 seconds:

   .. code-block:: yaml

      remove: ratio > 2 and seeding_time > 60000
      

   Here is another example. It removes the torrents which ratio is less than 1 **or** seeding time is more than 60000:

   .. code-block:: yaml

      remove: ratio < 1 or seeding_time > 60000
      

3. ``(<Expression>)``

   When an expression is enclosed in parentheses, it is still an expression. Using parentheses can change the priority. And you can use multiple parentheses for nesting.

   Here is an example. It removes torrents which seeding time is more than 60000 seconds, **or** those torrents which ratio is greater than 3 **and** added time is more than 1400000 seconds:

   .. code-block:: yaml

      remove: seeding_time > 60000 or (ratio > 3 and create_time > 1400000)
      

Part 4: Delete data
-------------------

Determine whether to delete data at the same time. If this field isn't specificed, the default value is ``false``.

The Last Step...
----------------

Remember to check your configuration file and make sure it works as you think. Use the following command line to see the torrents that will be removed (but not really remove them).

.. code-block:: bash

   python3 main.py --view
