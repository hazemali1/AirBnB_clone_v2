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
    if int(number) == 0:
        n = 1
    else:
        n = int(number)
    num = 0
    li = []
    for i in os.listdir("versions/"):
        num += 1
        q = i[11:-4]
        li.append(q)
    li.sort()
    for x in range(num - n):
        local("rm versions/web_static_{}.tgz".format(li[x]))
    numb = 0
    lis = []
    with cd('/data/web_static/releases'):
        for i in os.listdir("."):
            numb += 1
            w = i[11:-4]
            lis.append(w)
        lis.sort()
        for x in range(numb - n):
            run("rm web_static_{}.tgz".format(li[x]))
