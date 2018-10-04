#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Lucas Navarro (lucasgnavarro@gmail.com)"
__copyright__ = "Copyright (C) 2018- Lucas Navarro"

# Python Version 3.6
#
# Example of Singleton design pattern
#


class Singleton:

    __instance = None   # Instance reference
    name = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __str__(self):
        return 'Name: ' + self.name + ' | Mem Addr:' + str(id(self))


if __name__ == '__main__':
    # Singleton Test
    a = Singleton()
    a.name = 'One'
    print('A -> ' + str(a))

    b = Singleton()
    b.name = 'Another one'
    print('B -> ' + str(b))
    print('( A and B ) are the same -> ', (a is b))

