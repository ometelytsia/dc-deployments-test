import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_user_created(host):
    user = host.user('testuser')
    assert user.exists


@pytest.mark.parametrize('exe', [
    '/usr/bin/git',
    '/usr/bin/javac',
    '/usr/lib/jvm/java/bin/java'
])
def test_package_exes(host, exe):
    assert host.file(exe).exists
