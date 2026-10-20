#!/usr/bin/python3
"""Create and deploy a web_static archive to remote web servers."""

from datetime import datetime
from os import makedirs
from os.path import basename, exists

from fabric.api import env, local, put, run


env.hosts = [
    "WEB01_IP",
    "WEB02_IP"
]


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


def deploy():
    """Create an archive and deploy it to all web servers."""
    archive_path = do_pack()

    if archive_path is None:
        return False

    return do_deploy(archive_path)
