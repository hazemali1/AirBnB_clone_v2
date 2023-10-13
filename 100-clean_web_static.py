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
    lis = []
    with cd('/data/web_static/releases'):
        lis = run("ls -tr").split()
        p = []
        for k in lis:
            if k[:11] == "web_static_":
                p.append(k)
        numb = len(p)
        for x in range(numb - n):
            run("rm {}".format(p[x]))
