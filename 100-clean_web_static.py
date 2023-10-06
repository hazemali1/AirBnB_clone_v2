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
    if number == 0:
        number = 1
    num = 0
    l = []
    for i in os.listdir("versions/"):
        num += 1
        q = i[11:-4]
        l.append(q)
    l.sort()
    for x in range(num - int(number)):
        local("rm versions/web_static_{}.tgz".format(l[x]))

    num = 0
    l = []
    local("mkdir -p help")
    get(remote_path="/data/web_static/releases/*", local_path="help/")
    for i in os.listdir("help/"):
        num += 1
        q = i[11:-4]
        l.append(q)
    l.sort()
    for x in range(num - int(number)):
        run("rm /data/web_static/releases/web_static_{}.tgz".format(l[x]))
    local("rm -rf help")
