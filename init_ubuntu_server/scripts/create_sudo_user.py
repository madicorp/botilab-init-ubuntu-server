# -*- coding: utf-8 -*-
from fabric.operations import run


def create_sudo_user(username, pwd):
    # Create the new admin user (default group=username); add to admin group
    run('adduser {username} --disabled-password --gecos ""'.format(username=username))

    # Set the password for the new admin user
    run('echo "{username}:{password}" | chpasswd'.format(username=username, password=pwd))

    # Add group to sudoers
    run('echo "%{group} ALL=(ALL) ALL" >> /etc/sudoers'.format(group=username))
