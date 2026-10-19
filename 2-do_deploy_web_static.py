#!/usr/bin/python3
"""Deploy a web_static archive to remote web servers."""

from os.path import exists
from os.path import basename

from fabric.api import env, put, run


env.hosts = [
    "WEB01_IP",
    "WEB02_IP"
]


def do_deploy(archive_path):
    """Deploy a web_static archive to all configured web servers."""
    if not exists(archive_path):
        return False

    archive_name = basename(archive_path)
    release_name = archive_name.replace(".tgz", "")

    remote_archive = "/tmp/{}".format(archive_name)
    release_path = "/data/web_static/releases/{}/".format(
        release_name
    )

    try:
        put(archive_path, remote_archive)

        run("mkdir -p {}".format(release_path))

        run(
            "tar -xzf {} -C {}".format(
                remote_archive,
                release_path
            )
        )

        run("rm {}".format(remote_archive))

        run(
            "mv {}web_static/* {}".format(
                release_path,
                release_path
            )
        )

        run(
            "rm -rf {}web_static".format(
                release_path
            )
        )

        run("rm -rf /data/web_static/current")

        run(
            "ln -s {} /data/web_static/current".format(
                release_path
            )
        )

        print("New version deployed!")
        return True

    except Exception:
        return False
