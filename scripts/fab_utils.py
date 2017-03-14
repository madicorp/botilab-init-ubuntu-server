from fabric.context_managers import hide, settings
from fabric.operations import local, run


def get_result(cmd='echo "Hello, World!'):
    with hide('output', 'running', 'warnings'), settings(warn_only=True):
        result = local(cmd, capture=True)
        return result if result else ''


def replace_line_in_file(old_pattern, new_value, file_location, cmd_launcher=run):
    cmd_launcher("sed -i 's/{}/{}/' {}".format(old_pattern, new_value, file_location))
