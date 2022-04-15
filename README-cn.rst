自动删种程序
======================
|PyPI| |GithubActionsCI| |ReadTheDocs| |Coverage| |Codacy| |Downloads| |MIT|

这个程序可以帮助你删除种子。现在你再也不用担心你的磁盘空间了——通过你设置的策略，程序会帮你检查每一个种子是否满足删除的条件；如果是，那就自动地删除它。

这个程序支持 qBittorrent、Transmission 或 μTorrent。 如果你喜欢，可以点个星星 :star2: :)

文档：https://autoremove-torrents.readthedocs.io/zh_CN/latest/

.. |Codacy| image:: https://api.codacy.com/project/badge/Grade/6e5509ecb4714ed697c65f35d71cff65
    :target: https://www.codacy.com/app/jerrymakesjelly/autoremove-torrents?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jerrymakesjelly/autoremove-torrents&amp;utm_campaign=Badge_Grade
.. |GithubActionsCI| image:: https://github.com/jerrymakesjelly/autoremove-torrents/actions/workflows/build.yml/badge.svg?branch=master
   :target: https://github.com/jerrymakesjelly/autoremove-torrents/actions
.. |ReadTheDocs| image:: https://readthedocs.org/projects/autoremove-torrents-cn/badge/?version=latest
   :target: https://autoremove-torrents.readthedocs.io/zh_CN/latest/?badge=latest
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

环境要求
-------------

* Python 2.7 或 Python 3


快速开始
-------------
安装
+++++++++++++++++++
从 pip 安装
^^^^^^^^^^^^^^^^^
::

    pip install autoremove-torrents

或者

从 GitHub 安装
^^^^^^^^^^^^^^^^^^^^
::

    git clone https://github.com/jerrymakesjelly/autoremove-torrents.git
    cd autoremove-torrents
    python3 setup.py install


编写配置文件
++++++++++++++++++++++++++++++
为了让程序能按照你的想法去工作，你需要学习如何编写配置文件。

你可以把配置文件放在磁盘的任何地方。不过，在默认情况下，autoremove-torrents 只在 Shell 的当前工作目录去找 ``config.yml``::

    vim ./config.yml


语法也比较简单，下面是一个例子::

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


在这个例子中，程序会自动删除那些标签是 IPT，做种时间超过 1209600 秒 **或者** 分享率大于 1 的种子。请查看 `文档`_ 以获得更多信息。

.. _文档: https://autoremove-torrents.readthedocs.io/zh_CN/latest/

运行
++++
::

    autoremove-torrents

如果你只是想看看哪些种子会被删除但并不想真的就删除它们，请使用 ``--view`` 命令行参数（``autoremove-torrents --view``）。


设置计划任务
-----------------------------
如果你想每 15 分钟检查一次哪些种子可以被删除，Linux 的 ``crontab`` 程序可以帮你。首先::

    crontab -e

然后，在文件的最后加一行（请先确认 ``autoremove-torrents`` 在你系统中的路径）::

*/15 * * * * /usr/bin/autoremove-torrents --conf=/home/jerrymakesjelly/autoremove-torrents/config.yml --log=/home/jerrymakesjelly/autoremove-torrents/logs

``--conf`` 参数指示了配置文件的路径。
``--log`` 参数指定了存储日志文件的路径（必须存在）。

截图
-----------
|Screenshot|

.. |Screenshot| image:: https://user-images.githubusercontent.com/6760674/40576720-a78097fe-612d-11e8-9dda-8aac0c5011a2.png

更新日志
----------
**2020-08-27 周四**：1.5.3 版本。

* 修复 psutil 在群晖的兼容问题（用于检查磁盘剩余空间）。（#61）
* 可以通过 ``--debug`` 或 ``-d`` 命令行启用调试模式。（#76）
* 修复由主机 URL 末尾的 ``/`` 导致的 API 不兼容的问题。（#81）
* 添加上传量与下载量两个条件。（#79）

**2020-03-27 周五**：1.5.2 版本。

* 支持 Deluge （#8）；
* 使用批量删除提升删除效率；
* 修复配置文件中的多语言支持问题（#69）；
* 客户端名称不再对大小写敏感。

**2020-02-29 周六**：1.5.1 版本。

* 修复了 1.5.0 版本中丢失的状态 ``StalledUpload`` 和 ``StalledDownload``。（#66）

**2020-02-28 周五**：1.5.0 版本。

* 修复了无法登录使用纯数字用户名或密码的客户端的问题（#64）；
* 修复了在没有标签属性的 Transmission 中任务无法执行的问题；
* 修复了删种条件可能对未打标签以及没有Tracker的种子无效的问题；
* 修复了 status 中遗漏的 μTorrent 状态“排队中”（``Queued``）；
* ``status`` 中添加 ``Error`` 状态；
* 添加对 Transmission 标签的支持（#24）；
* 添加删除条件“最大下载速度” ``max_downloadspeed``、“最小上传速度” ``min_uploadspeed``；
* 添加删除条件“最小平均上传速度” ``min_average_uploadspeed``、“最大平均下载速度” ``max_average_downloadspeed`` （#49）；
* 添加删除条件“最大种子大小” ``max_size`` （#21）；
* 添加删除条件“最大做种数” ``max_seeder``、“最小下载数” ``min_leecher`` （#62）；
* 添加删除条件“最大已连接做种者” ``max_connected_seeder``、“最小已连接下载者” ``min_connected_leecher``；
* 添加删除条件“最后活动时间” ``last_activity``，以删除一段时间内没有上传或下载速度的种子（#1）（#9)；
* 添加删除条件“最大下载百分比” ``max_progress``；
* ``free_space``、``maximum_number``、``seed_size`` 的 ``action`` 中添加 ``remove-active-seeds``、``remove-inactive-seeds`` 动作，用于根据最后活动时间去尽量删除活跃的种子或者不活跃的种子（#9）；
* 添加了新的删除条件“上传比率” ``upload_ratio``，可以根据上传量占种子大小的比例删种（#55）；

**2020-02-03 周一**：迁移文档到 Read the Docs。

**2020-01-26 周日**: 1.4.9 版本。

* 添加了 `free_space` 条件（最小剩余空间）。

**2020-01-07 周二**: 1.4.8 版本。

* 修复了在 qBittorrent v4.2.1 中不能删除种子的问题。对造成的不便深感抱歉。 (#53)

**2020-01-06 周一**: 1.4.7 版本。

* 添加了 qBittorrent v4.2.1 中新 API 的支持。 (#46) **注意：这个版本有bug，请升级到1.4.8或者更高的版本。**

**2019-09-17 周二**: 1.4.6 版本。

* 修复了当 Tracker 的 URL 包含端口时，`tracker` 过滤器需要指定端口的问题。

**2019-06-06 周四**: 1.4.5 版本。

* 添加了 `StalledUpload` 与 `StalledDownload` 状态。

**2019-05-22 周三**: 1.4.4 版本。

* 修复了当 `seed_size` / `maximum_number` 条件与 `ratio` / `create_time` / `seeding_time` 条件同时使用时任务会失败的问题。(#33)
* 新特性：如果过滤器的内容只有一行，现在可以直接写出而不需要使用列表。

**2019-05-19 周日**: 1.4.3 版本。

* 添加对 Python 2.7 的支持。(#29)
* 停止支持 Python 3.4。(kennethreitz/requests#5092)

**2019-05-13 周一**: 1.4.2 版本。

* 修复了丢失的语法分析器文件。(#32)
* 修复了运算符的结合性。现在，运算符 `and` 和 `or` 保证是左结合的。（#32）

**2019-05-06 周一**: 1.4.1 版本。

* 修复了丢失的依赖项 `ply`。
* 修复了在`remove`条件中重复定义的警告。

**2019-05-06 周一**: 更新了文档。

* 增加了关于`remove`条件的描述。

**2019-05-01 周三**: 1.4.0 版本。

* 删除了 ``seeding_time`` 和 ``ratio`` 条件中的限制 (#19)。
    - 在之前的版本，``seeding_time`` 和 ``ratio`` 条件只会删除那些正在做种的种子。设置这个限制是为了给用户提供一个通过修改种子的状态（例如暂停做种）来避免种子被删除的方法。
    - 不过现在我们有状态过滤器（``status``），所以这个限制就显得多余了，而且可能会使它的行为跟用户预想的不一样。
* 支持自定义删除表达式 (#15)。
    - 现在我们可以直接而明确地写出我们想要的表达式了，例如 ``remove: ratio > 1``。
    - 复合的条件表达式也支持，例如 ``remove: (seeding_time < 86400 and ratio > 1) or (seeding_time > 86400 and ratio > 3)``。
    - 旧的写法仍然可用。

**2019-04-17 周三**: 1.3.0 版本。

* 修复了在 qBittorrent 拥有大量的种子时程序会卡住的问题 (`Issue #22 <https://github.com/jerrymakesjelly/autoremove-torrents/issues/22>`_)。
* 修复了状态过滤器在工作时会写入重复的日志的问题。
* 日志系统已更新： 
    - 日志路径可以被指定（使用 ``--log`` 参数，例如 ``--log=/home/jerrymakesjelly/logs``） (`Issue #23 <https://github.com/jerrymakesjelly/autoremove-torrents/issues/23>`_)。
    - 日志文件将按天存储在不同的文件中（格式：``autoremove.%Y-%m-%d.log``）。
* 全部单词 ``seed`` 修改为 ``torrent`` (`Issue #25 <https://github.com/jerrymakesjelly/autoremove-torrents/issues/25>`_)。
* 删去了所有不必要的调试日志。

**2019-01-10 周一**: 1.2.5 版本。

* 修复了在设置多个策略时种子数量不正确的问题 (`Issue #10 <https://github.com/jerrymakesjelly/autoremove-torrents/issues/10>`_, 感谢 @momokoo 报告此问题并提出 PR).
* 修复了在 qBittorrent 中种子数不正确的问题 (`Issue #13 <https://github.com/jerrymakesjelly/autoremove-torrents/issues/13>`_)。

**2018-05-31 周四**: 1.2.4 版本。

* 修复了启动失败的问题。

**2018-05-30 周三**: 1.2.3 版本。增加了一些功能。

* 允许使用环境变量去指定 ``host``、``username`` 和 ``password``。
* 允许 ``username`` 和 ``password`` 留空（或者其中之一留空），使得不用用户名或密码也可以登录 WebUI。
* 现在程序在一个任务失败时不会直接退出。

**2018-05-27 周日**: 1.2.2 版本。 增加了一些功能 :smile:

* 增加了新过滤器：种子状态。
* 增加了新条件：最大种子数量。

**2018-05-26 周六**: 1.2.1 版本。 修复了 ``setup.py`` 的问题。

**2018-05-26 周六**: 1.2.0 版本. 重构已完成，程序已发布至 PyPI。

* 新特性很快会被加入。
* 现在你可以通过 ``pip`` 安装程序。

**2018-05-14 周一**: 1.1.0 版本。 创建了 ``setup.py``。

现在你可以直接使用 ``autoremove-torrents`` 命令而不是 ``python3 main.py``。

**2018-03-28 周三**: （更正文档） ``delete_data`` 字段不应该被缩进。

**2018-03-22 周四**: 第一个版本 :bowtie:

计划列表
-----------
看你们的反馈。如果你有任何问题，欢迎提交 `issues`_。

.. _issues: https://github.com/jerrymakesjelly/autoremove-torrents/issues

`点击这里`_ 查看TODO列表。

.. _点击这里: https://github.com/jerrymakesjelly/autoremove-torrents/issues/63
