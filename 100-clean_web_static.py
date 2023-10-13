#!/usr/bin/python3
from fabric.api import *
import datetime
import os
"""
fabric
"""


env.hosts = ['100.25.15.141', '100.25.19.252']


def do_clean(number=0):
    """
    clean
    """
    if number == 0 or number == 1:
        number = 2
    with lcd('versions'):
        archives = sorted(os.listdir('.'))
        to_delete = archives[:-number]

        for archive in to_delete:
            local('rm -f {}'.format(archive))

    with cd('/data/web_static/releases'):
        archives = run('ls -tr').split()
        to_delete = archives[:-number]

        for archive in to_delete:
            run('rm -f {}'.format(archive))