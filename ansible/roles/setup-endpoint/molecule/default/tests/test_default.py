import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

@pytest.mark.parametrize('pkg', ['nginx'])
def test_system_dependency_installation(host, pkg):
    package = host.package(pkg)

    assert package.is_installed

def test_nginx_configs(host):
    pass