from random_port import get_random_port


def test_get_random_port():
    port = get_random_port()
    assert isinstance(port, int)
    assert 0 < port <= 65535


def test_port_reusability():
    port1 = get_random_port()
    port2 = get_random_port()
    assert port1 != port2
