#!/usr/bin/python3
"""Fabric script generate a .tgz archive from contents of web_static folder"""

from fabric.api import local
import os


env.hosts = [100.26.159.135, 54.157.147.219]

Packing = __import__('1-pack_web_static.py').do_pack


def do_deploy(archive_path):
    """Deploys a web_static into an IP"""

    if path.exists(archive_path):

        put(archive_path, '/tmp/')

        archive_name = archive_path.split('/')[-1]
        archive = file_name.split('.')[0]
        folder_name = '/data/web_static/releases/{}'.format(archive)

        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}'.format(archive_name, folder_name))

        run('rm /tmp/{}'.format(archive_name))

        run('mv {}/web_static/* {}'.format(folder_name, folder_name))
        run('rm -rf {}/web_static'.format(folder_name))

        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(folder_name))

        return True
    else:
        return False


def deploy():
    """Deploys the .tgz"""

    Path = Packing()
    return do_deploy(Path)
