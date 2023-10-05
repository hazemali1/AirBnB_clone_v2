#!/usr/bin/python3
from fabric.api import *
import os
"""
fabric
"""


env.hosts = ['100.25.15.141', '100.25.19.252']
def do_deploy(archive_path):
    """
    deploy
    """
    if os.path.exists(archive_path) is False:
        return False
    try:
        archive_path = archive_path[9:]
        put(archive_path, "/tmp/{}".format(archive_path))
        run("mkdir -p /data/web_static/releases/{}".format(archive_path))
        s = ""
        for i in archive_path:
            if i == '.':
                break
            s += i
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_path, s))
        run("rm /tmp/{}".format(archive_path))
        run("cp /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(s, s))
        run("rm -rf /data/web_static/releases/{}/web_static".format(s))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(s))
        return True
    except SyntaxError:
        return False
