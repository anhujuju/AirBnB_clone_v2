#!/usr/bin/python3
""" create tgz from /web_static"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """ Package """
    datu = 'web_static_' + datetime.strftime(datetime.now(), "%Y%m%d%I%M%S")
    tgz = datu + '.tgz'
    
    local('mkdir -p versions')
    dire = 'versions/'
    file = local('tar -cvzf {}{} web_static'.format(dire, tgz))
    if archive.failed:
        return None
    if archive.succeeded:
        return direc + tgz
