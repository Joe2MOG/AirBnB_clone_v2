#!/usr/bin/python3
"""Deploy a web_static archive to web servers."""

import os

from fabric.api import env, local, put, run, sudo


hosts = [
    os.getenv("WEB01_IP"),
    os.getenv("WEB02_IP")
]
env.hosts = [host for host in hosts if host]

if not env.hosts:
    env.hosts = ["127.0.0.1"]


def is_local():
    """Return True when deployment is running on the local machine."""
    return env.host_string in ("", "localhost", "127.0.0.1")


def execute(command):
    """Run a command locally or on the current remote server."""
    if is_local():
        return local(command)
    return run(command)


def execute_sudo(command):
    """Run a privileged command locally or remotely."""
    if is_local():
        if os.geteuid() == 0:
            return local(command)
        return local("sudo {}".format(command))
    return sudo(command)


def upload_archive(archive_path, archive_name):
    """Copy an archive to /tmp locally or remotely."""
    if is_local():
        local(
            "cp {} /tmp/{}".format(
                archive_path,
                archive_name
            )
        )
    else:
        put(archive_path, "/tmp/")


def ensure_nginx():
    """Ensure Nginx serves /hbnb_static/ from the current release."""
    config = "/etc/nginx/sites-available/default"

    command = (
        "grep -q 'location /hbnb_static/' {0} || "
        "sed -i '/server_name .*;/a\\        "
        "location /hbnb_static/ {{ "
        "alias /data/web_static/current/; "
        "}}' {0}"
    ).format(config)

    execute_sudo(command)
    execute_sudo("nginx -t")
    execute_sudo("service nginx restart")


def do_deploy(archive_path):
    """Deploy a web_static archive to the configured web server."""
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        release_name = archive_name.split(".")[0]
        release_path = (
            "/data/web_static/releases/{}/".format(
                release_name
            )
        )

        upload_archive(archive_path, archive_name)

        execute("mkdir -p {}".format(release_path))

        execute(
            "tar -xzf /tmp/{} -C {}".format(
                archive_name,
                release_path
            )
        )

        execute("rm /tmp/{}".format(archive_name))

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

        execute("rm -rf /data/web_static/current")

        execute(
            "ln -s {} /data/web_static/current".format(
                release_path
            )
        )

        ensure_nginx()

        print("New version deployed!")
        return True

    except Exception:
        return False
