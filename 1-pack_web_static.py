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
                s = "web_static_" + t.year + t.month + t.day + t.hour + t.minute + t.second + ".tgz"
                local("mkdir -p versions")
                local("tar -cvzf versions/{}  web_static".format(s))
                return "versions/{}".format(s)
        except:
                return None