AutoRemove-Torrents
====================
AutoRemove-Torrents是一个自动删除种子的脚本程序。它能根据你设置的策略，自动删除BT客户端内的种子。目前支持的客户端有qBittorrent、Transmission和μTorrent。

安装
========
依赖项
------
* `Python 3`_

.. _Python 3: https://www.python.org/

脚本程序使用Python 3编写，因此在执行下面步骤之前，请确认您的机器已经正确安装Python 3。

步骤
------
1. 从Github上下载代码。如果你已经安装Git，请执行::

    git clone https://github.com/jerrymakesjelly/autoremove-torrents.git

   如果你不是开发者，没有安装Git也没关系，你仍然可以点击页面右上方的绿色 **Clone or download** 按钮，选择 **Download ZIP** 来下载源代码，或者干脆点击 `这里`_ 。然后解压下载的压缩包。

   无论你用何种方式下载了源代码，完成后，将工作目录切换到 `autoremove-torrents` 目录下::

     cd autoremove-torrents

#. 安装依赖库::

    pip3 install -r requirements.txt

#. 编写配置文件

   AutoRemove-Torrents使用基于YAML语言的配置文件。首先在当前目录下创建一个 `config.yml` 文件::

    vim ./config.yml

   然后就可以自由创建自己的规则了。一个配置文件示例如下::

    my_task:
      client: qbittorrent
      host: http://127.0.0.1
      username: YOUR_USERNAME
      password: YOUR_PASSWORD
      strategies:
        strategy1:
          trackers:
            - ipt.com
          seeding_time: 1209600
          ratio: 1
          delete_data: true

   关于配置文件的编写说明，请参考 `Wiki`_。

#. 运行::

    python3 main.py

   如果只是想查看哪些种子符合删除条件，但并不打算删除它们，请在后面加上 `--view` 参数。

.. _这里: https://github.com/jerrymakesjelly/autoremove-torrents/archive/master.zip
.. _Wiki: https://127.0.0.1

定时运行
=========
Windows
---------
打开你的 `cmd` 或 `PowerShell`，借助 `schtasks` 命令，可以配置Windows任务计划程序。一个例子如下::

  schtasks /create /sc minute /mo 30 /tn autoremove-torrents /tr "C:\Users\someone\AppData\Local\Programs\Python\Python36\python.exe C:\autoremove-torrents\main.py -c C:\autoremove-torrents\config.yml"

该命令设置了一个名称为 `autoremove-torrents` 的任务，该任务每30分钟执行一次。

由于各计算机的运行环境不同，在设置之前，请确认 `Python` 和 `autoremove-torrents` 的安装路径。关于 `schtasks` 命令的使用方法，请参阅 `schtasks | Microsoft Docs`_。

`-c` 参数指定了配置文件的路径。

Linux/Unix
--------------
同样，类Unix系统也有任务计划程序，这里我们用 `Cron` 程序来实现任务的定时运行。

1. 编辑 `crontab` 文件::

    crontab -e

#. 在 `crontab` 文件末尾添加一行设置用于执行定时任务。一个例子如下::

    */30 * * * * /usr/bin/python3 /home/someone/autoremove-torrents/main.py -c /home/someone/autoremove-torrents/config.yml

   该任务每30分钟执行一次。在设置之前，请确认 `Python` 和 `autoremove-torrents` 的安装路径。一个查看 `Python` 程序安装路径的方法是执行命令 `which python3`。

   `-c` 参数指定了配置文件的路径。

   有关 `Cron` 程序和 `crontab` 文件的更多信息，请参阅 `Cron - ArchWiki`_。

#. 保存 `crontab` 文件。

.. _schtasks | Microsoft Docs: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/schtask
.. _Cron - ArchWiki: https://wiki.archlinux.org/index.php/Cron_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)

作者与许可协议
===============
软件由 jerrymakesjelly 编写。遵循 `MIT许可协议`_。

.. _MIT许可协议: https://github.com/jerrymakesjelly/autoremove-torrents/blob/master/LICENSE