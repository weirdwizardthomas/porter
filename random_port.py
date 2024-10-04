import socket

import const
from socket_context import socket_context


def get_random_port() -> int:
    with socket_context(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(const.PORT_0_ADDRESS)
        address = s.getsockname()
    _, port = address
    return port
