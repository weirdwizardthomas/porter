import socket
from contextlib import contextmanager


@contextmanager
def socket_context(*args, **kw):
    s = socket.socket(*args, **kw)
    try:
        yield s
    finally:
        s.close()
