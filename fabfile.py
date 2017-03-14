from scripts.configure_ssh_connection import copy_current_user_public_key, configure_ssh_file
from scripts.create_sudo_user import create_sudo_user


def init_ubuntu_server(username, pwd):
    create_sudo_user(username, pwd)
    copy_current_user_public_key(username)
    configure_ssh_file()
