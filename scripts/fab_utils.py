from fabric.context_managers import hide, settings
from fabric.operations import local, run


def get_result(cmd='echo "Hello, World!'):
    with hide('output', 'running', 'warnings'), settings(warn_only=True):
        result = local(cmd, capture=True)
        return result if result else ''


def _replace_line_in_file(old_pattern, new_value, file_location, cmd_launcher=run):
    cmd_launcher("sed -i 's/{}/{}/' {}".format(old_pattern, new_value, file_location))


def _file_contains_line(file_path, pattern):
    return run("cat {} | grep '{}'".format(file_path, pattern), warn_only=True, quiet=True)


def create_or_replace_line_in_file(template, value, file_path):
    template_filled_with_value = template.format(value)
    if _file_contains_line(file_path, template.format('*')):
        _replace_line_in_file(template.format('.*'),
                              template_filled_with_value,
                              file_path)
    else:
        run("echo '{}' >> {}".format(template_filled_with_value, file_path))
