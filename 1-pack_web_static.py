#!/usr/bin/python3
"""
This is a Fabric script that generates a .tgz archive from
the files of the web_static folder of AIrBnB-clone_v2
repo, using the function do_pack.
"""


from fabric.api import local
import os
from datetime import datetime

def do_pack():
    """Function to compress directory
    Return: path to archive on success; None on fail
    """
    # Get current time
    pathnow = datetime.now()
    pathnow = pathnow.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_' + pathnow + '.tgz'

    # Create archive
    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static/'.format(archive_path))

    # Check if archiving was successful
    if result.succeeded:
        return archive_path
    return None