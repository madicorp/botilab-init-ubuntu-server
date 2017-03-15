from fabric.operations import run

from scripts.fab_utils import replace_line_in_file


def _file_contains_line(file_path, pattern):
    return run("cat {} | grep '{}'".format(file_path, pattern), warn_only=True, quiet=True)


def _replace_in_10_periodic_config(template, value):
    periodic_file_path = '/etc/apt/apt.conf.d/10periodic'
    template_filled_with_value = template.format('"{}"'.format(value))
    if _file_contains_line(periodic_file_path, template.format('*')):
        print('contains')
        replace_line_in_file(template.format('.*'),
                             template_filled_with_value,
                             periodic_file_path)
    else:
        print('not contains')
        run("echo '{}' >> {}".format(template_filled_with_value, periodic_file_path))


def configure_auto_updates():
    run('sudo apt-get install unattended-upgrades')

    _replace_in_10_periodic_config("APT::Periodic::Update-Package-Lists {}", 1)
    _replace_in_10_periodic_config("APT::Periodic::Download-Upgradeable-Packages {}", 1)
    _replace_in_10_periodic_config("APT::Periodic::AutocleanInterval {}", 7)
    _replace_in_10_periodic_config("APT::Periodic::Unattended-Upgrade {}", 1)
