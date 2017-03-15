from fabric.operations import run

from scripts.fab_utils import replace_line_in_file


def _replace_in_10_periodic_config(template, value):
    replace_line_in_file(template.format('.*'),
                         template.format('"{}"'.format(value)),
                         '/etc/apt/apt.conf.d/10periodic')


def configure_auto_updates():
    run('sudo apt-get install unattended-upgrades')

    _replace_in_10_periodic_config("APT::Periodic::Update-Package-Lists {}", 1)
    _replace_in_10_periodic_config("APT::Periodic::Download-Upgradeable-Packages {}", 1)
    _replace_in_10_periodic_config("APT::Periodic::AutocleanInterval {}", 7)
    _replace_in_10_periodic_config("APT::Periodic::Unattended-Upgrade {}", 1)
