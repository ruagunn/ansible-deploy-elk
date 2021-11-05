def test_sshd_service(host):
    assert host.service("sshd").is_running

def test_docker_service(host):
    assert host.service("docker").is_running
    
def test_jenkins_service(host):
    assert host.service("jenkins").is_running