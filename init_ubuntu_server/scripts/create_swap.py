# -*- coding: utf-8 -*-
from fabric.operations import sudo

from init_ubuntu_server.scripts.fab_utils import create_or_replace_line_in_file


def _create_or_replace_in_sysctl_conf(template, value):
    create_or_replace_line_in_file(template, value, '/etc/sysctl.conf')


def create_swap():
    # Inspired by https://www.digitalocean.com/community/tutorials/how-to-add-swap-on-ubuntu-14-04
    sudo('fallocate -l 4G /swapfile')
    sudo('chmod 600 /swapfile')
    sudo('mkswap /swapfile')
    sudo('swapon /swapfile')
    # Make the swap permanent
    create_or_replace_line_in_file('echo /swapfile', '\tnone\tswap\tsw\t0\t0', '/etc/fstab')

    # How often data are swap out of RAM to the swap space
    sudo('sysctl vm.swappiness=10')
    _create_or_replace_in_sysctl_conf('vm.swappiness={}', 10)

    # Cache the inode information longer
    sudo('sysctl vm.vfs_cache_pressure=50')
    _create_or_replace_in_sysctl_conf('vm.vfs_cache_pressure={}', 50)
