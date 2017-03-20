from init_ubuntu_server.scripts.configure_auto_updates import configure_auto_updates
from init_ubuntu_server.scripts.configure_ssh_connection import copy_current_user_public_key, configure_ssh_file
from init_ubuntu_server.scripts.create_sudo_user import create_sudo_user
from init_ubuntu_server.scripts.create_swap import create_swap


def init_ubuntu_server(username, pwd):
    create_swap()
    configure_auto_updates()
    create_sudo_user(username, pwd)
    copy_current_user_public_key(username)
    configure_ssh_file()
