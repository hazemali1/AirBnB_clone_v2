#!/usr/bin/python3
from fabric.api import *
import os
import datetime
"""
fabric
"""


def do_pack():
    """
    do pack
    """
    try:
        t = datetime.datetime.now()
        s = "web_static_" + str(t.year) + str(t.month) + str(t.day)
        s += str(t.hour) + str(t.minute) + str(t.second) + ".tgz"
        local("mkdir -p versions")
        local("tar -cvzf versions/{}  web_static".format(s))
        return "versions/{}".format(s)
    except SyntaxError:
        return None


env.hosts = ['100.25.15.141', '100.25.19.252']


def do_deploy(archive_path):
    """
    deploy
    """
    if os.path.exists(archive_path) is False:
        return False
    try:
        archive_pat = archive_path[9:]
        put(archive_path, "/tmp/{}".format(archive_pat))
        s = ""
        for i in archive_pat:
            if i == '.':
                break
            s += i
        run("mkdir -p /data/web_static/releases/{}".format(s))
        d = "/data/web_static/releases/"
        run("tar -xzf /tmp/{} -C {}{}/".format(archive_pat, d, s))
        run("rm /tmp/{}".format(archive_pat))
        run("mv {}{}/web_static/* {}{}/".format(d, s, d, s))
        run("rm -rf /data/web_static/releases/{}/web_static".format(s))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(d, s))
        return True
    except SyntaxError:
        return False


def deploy():
    """
    call pack and deploy
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
