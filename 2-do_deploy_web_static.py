#!/usr/bin/python3
"""Deploy a web_static archive to web servers."""

import os

from fabric.api import env, local, put, run


hosts = [
    os.getenv("WEB01_IP"),
    os.getenv("WEB02_IP")
]

env.hosts = [host for host in hosts if host]

if not env.hosts:
    env.hosts = ["127.0.0.1"]


def is_local():
    """Return True when deployment is running locally."""
    return env.host_string in ("", "localhost", "127.0.0.1")


def execute(command):
    """Execute a command locally or on the remote server."""
    if is_local():
        return local(command)

    return run(command)


def upload_archive(archive_path, archive_name):
    """Upload an archive to the /tmp directory."""
    if is_local():
        local(
            "cp {} /tmp/{}".format(
                archive_path,
                archive_name
            )
        )
    else:
        put(archive_path, "/tmp/")


def do_deploy(archive_path):
    """Deploy a web_static archive to the configured server."""
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        release_name = archive_name.replace(".tgz", "")

        release_path = (
            "/data/web_static/releases/{}/".format(
                release_name
            )
        )

        upload_archive(
            archive_path,
            archive_name
        )

        execute(
            "mkdir -p {}".format(
                release_path
            )
        )

        execute(
            "tar -xzf /tmp/{} -C {}".format(
                archive_name,
                release_path
            )
        )

        execute(
            "rm -f /tmp/{}".format(
                archive_name
            )
        )

        execute(
            "mv {}web_static/* {}".format(
                release_path,
                release_path
            )
        )

        execute(
            "rm -rf {}web_static".format(
                release_path
            )
        )

        execute(
            "rm -rf /data/web_static/current"
        )

        execute(
            "ln -s {} /data/web_static/current".format(
                release_path
            )
        )

        print("New version deployed!")
        return True

    except Exception:
        return False
