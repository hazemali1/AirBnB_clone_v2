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
    num = 0
    li = []
    for i in os.listdir("versions/"):
        num += 1
        q = i[11:-4]
        li.append(q)
    li.sort()
    for x in range(num - int(number)):
        local("rm versions/web_static_{}.tgz".format(li[x]))

    n = 0
    lis = []
    local("mkdir -p help")
    try:
        get(remote_path="/data/web_static/releases/web_static_*.tgz", local_path="help/")
    except:
        pass
    for i in os.listdir("help/"):
        n += 1
        qi = i[11:-4]
        lis.append(qi)
    lis.sort()
    for x in range(num - int(number)):
        run("rm /data/web_static/releases/web_static_{}.tgz".format(lis[x]))
    local("rm -rf help")
