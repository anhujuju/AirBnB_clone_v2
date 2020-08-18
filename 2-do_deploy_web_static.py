#!/usr/bin/python3
""" Deploys web static"""

from fabric.api import put, run, env, local
from os.path import exists
from os.path import isdir
from datetime import datetime


env.user = 'ubuntu'
env.hosts = ['34.75.41.244', '54.227.21.96']


def do_pack():
    """ Package """
    datu = 'web_static_' + datetime.strftime(datetime.now(), "%Y%m%d%I%M%S")
    tgz = datu + '.tgz'

    local('mkdir -p versions')
    dire = 'versions/'
    file = local('tar -cvzf {}{} web_static'.format(dire, tgz))
    if isdir('versions'):
        return dire + tgz
    else:
        return None

def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
