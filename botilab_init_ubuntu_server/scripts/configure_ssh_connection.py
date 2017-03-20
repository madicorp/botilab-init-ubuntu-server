# -*- coding: utf-8 -*-
from fabric.operations import run

from init_ubuntu_server.scripts.fab_utils import get_result, create_or_replace_line_in_file


def copy_current_user_public_key(username):
    current_user_public_key = get_result('cat ~/.ssh/id_rsa.pub')
    user_ssh_location = '/home/{}/.ssh'.format(username)
    authorized_keys_location = '{}/authorized_keys'.format(user_ssh_location)
    run('mkdir -p {}'.format(user_ssh_location))
    run('touch {}'.format(authorized_keys_location))
    run("echo '{}' >> {}".format(current_user_public_key, authorized_keys_location))
    run("chmod 700 {}".format(user_ssh_location))
    run("chown -R {username}:{username} {user_ssh_location}".format(username=username,
                                                                    user_ssh_location=user_ssh_location))
    run("chmod 600 {}".format(authorized_keys_location))


def configure_ssh_file(sshd_config_location='/etc/ssh/sshd_config'):
    password_auth_format = 'PasswordAuthentication {}'
    create_or_replace_line_in_file(password_auth_format, 'no', sshd_config_location)
    permit_root_login_format = 'PermitRootLogin {}'
    create_or_replace_line_in_file(permit_root_login_format, 'no', sshd_config_location)
    run('service ssh restart')
