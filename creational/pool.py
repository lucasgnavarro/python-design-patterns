#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

__author__ = "Lucas Navarro (lucasgnavarro@gmail.com)"
__copyright__ = "Copyright (C) 2018- Lucas Navarro"

# Python Version 3.6
#
# Example of Pool design pattern

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from utils import print_line, clean_line


class CustomSocket:
    """
    For example purposes only, the socket does not have full functionality
    """

    def __init__(self):
        print('Creating CustomSocket in mem addr :{addr}'.format(addr=id(self)))

    def ping(self):
        print('Pong {addr}'.format(addr=id(self)))


class SocketPool:
    _socket_pool = None

    def __init__(self, pool_size):
        print_line()
        self._socket_pool = [CustomSocket() for _ in range(pool_size)]
        print_line()

    def get_socket(self):
        to_return = self._socket_pool.pop()
        print('Socket returned : Mem addr {0}'.format(id(to_return)))
        return to_return

    def release_socket(self, socket):
        print('Socket released : Mem addr {0}'.format(id(socket)))
        self._socket_pool.append(socket)

    def check_socket_availability(self):
        print_line()
        print('Sockets availability')
        for _socket in self._socket_pool:
            print('Socket {_socket} - Mem. Addr. {addr}'.format(_socket=_socket, addr=id(_socket)))
        print_line()

    def destroy(self):
        del self._socket_pool


if __name__ == '__main__':

    # We create the socket pool example
    pool = SocketPool(5)

    print('Get sockets')
    socket1 = pool.get_socket()
    socket2 = pool.get_socket()

    socket1.ping()

    # Print sockets availability
    pool.check_socket_availability()

    # Release one used socket
    pool.release_socket(socket1)

    # Print sockets availability after socket1 release
    pool.check_socket_availability()

