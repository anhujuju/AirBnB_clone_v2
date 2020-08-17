#!/usr/bin/python3
""" create tgz from /web_static"""

from fabric.api import local
from datetime import datetime
from os.path import isdir


def do_pack():
    """ Package """
    datu = 'web_static_' + datetime.strftime(datetime.now(), "%Y%m%d%I%M%S")
    tgz = datu + '.tgz'

    local('mkdir -p versions')
    dire = 'versions/'
    file = local('tar -cvzf {}{} web_static'.format(dire, tgz))
    if isdir('versions'):
        return direc + tgz
    else:
        return None
