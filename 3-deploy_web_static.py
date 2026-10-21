#!/usr/bin/python3
"""Create and deploy web_static archives."""

import os
from datetime import datetime

from fabric.api import env, local, put, run


env.hosts = [
    "WEB01_IP",
    "WEB02_IP"
]


def do_pack():
    """Create a compressed archive of the web_static directory."""
    if not os.path.exists("versions"):
        os.makedirs("versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    print("Packing web_static to {}".format(archive_path))

    result = local(
        "tar -cvzf {} web_static".format(archive_path)
    )

    if result.failed:
        return None

    return archive_path


def do_deploy(archive_path):
    """Deploy a web_static archive to the configured web servers."""
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        release_name = archive_name.split(".")[0]

        put(archive_path, "/tmp/")

        run(
            "mkdir -p /data/web_static/releases/{}/".format(
                release_name
            )
        )

        run(
            "tar -xzf /tmp/{} -C "
            "/data/web_static/releases/{}/".format(
                archive_name,
                release_name
            )
        )

        run("rm /tmp/{}".format(archive_name))

        run(
            "mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(
                release_name,
                release_name
            )
        )

        run(
            "rm -rf /data/web_static/releases/{}/web_static".format(
                release_name
            )
        )

        run("rm -rf /data/web_static/current")

        run(
            "ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current".format(
                release_name
            )
        )

        print("New version deployed!")
        return True

    except Exception:
        return False


def deploy():
    """Create an archive and deploy it to all web servers."""
    archive_path = do_pack()

    if archive_path is None:
        return False

    return do_deploy(archive_path)
