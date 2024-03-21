#!/usr/bin/python3
"""Fabric script generate a .tgz archive from contents of web_static folder"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """generate a .tgz archive from contents of web_static folder"""

    local('mkdir -p versions/')

    Current = datetime.now()
    Time = ""
    Time += "{}{}{}".format(Current.year, Current.month, Current.day)
    Time += "{}{}{}".format(Current.hour, Current.minute, Current.second)

    file_name = "versions/web_static_{}.tgz".format(Time)

    Archive = local('tar -cvzf {} web_static/'.format(file_name), capture=True)

    if Archive.succeeded:
        archive_size = os.path.getsize(file_name)
        print('{} -> {} bytes'.format(file_name, archive_size))
        return file_name
    else:
        return None
