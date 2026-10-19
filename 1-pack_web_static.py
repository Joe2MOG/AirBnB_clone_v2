#!/usr/bin/python3
"""Create a compressed archive of the web_static directory."""

from datetime import datetime
from os import makedirs
from os.path import exists

from fabric.api import local


def do_pack():
    """Generate a .tgz archive from the web_static directory."""
    if not exists("versions"):
        makedirs("versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    print("Packing web_static to {}".format(archive_path))

    result = local(
        "tar -cvzf {} web_static".format(archive_path)
    )

    if result.failed:
        return None

    return archive_path
