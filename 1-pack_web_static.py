#!/usr/bin/python3
from fabric.api import *
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
