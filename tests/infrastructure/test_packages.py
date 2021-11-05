"""
Package List:
    - ansible
    - docker
    - docker-compose
    - jenkins
    - git
    - curl
    - wget
    - python3
    - python3-testinfra
"""
def test_is_ansible_installed(host):
    ansible = host.package("ansible")
    assert ansible.is_installed

def test_is_docker_installed(host):
    docker = host.package("docker")
    assert docker.is_installed
    
def test_is_docker_compose_installed(host):
    dc = host.package("docker-compose")
    assert dc.is_installed

def test_is_jenkins_installed(host):
    jenkins = host.package("jenkins")
    assert jenkins.is_installed

def test_is_git_installed(host):
    git = host.package("git")
    assert git.is_installed

def test_is_curl_installed(host):
    curl = host.package("curl")
    assert curl.is_installed

def test_is_wget_installed(host):
    curl = host.package("wget")
    assert curl.is_installed

def test_is_python3_installed(host):
    p3 = host.package("python3")
    assert p3.is_installed

def test_is_python3_testinfra_installed(host):
    p3ti = host.package("python3-testinfra")
    assert p3ti.is_installed
