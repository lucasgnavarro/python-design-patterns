#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Lucas Navarro (lucasgnavarro@gmail.com)"
__copyright__ = "Copyright (C) 2018- Lucas Navarro"

# Python Version 3.6
#
# Example of Decorator design pattern

from time import time


def timed(method):  # timing fn for decorate other fns
    def inner(*args, **kwargs):
        start = time()
        try:
            return method(*args, **kwargs)
        finally:
            end = time()
            print('Elapsed time -> {0:f}'.format(end-start))
    return inner


@timed
def main():
    print('Timing decorator Testing')

    to_print = []
    for i in range(1000000):
        to_print.append(i)


if __name__ == '__main__':
    main()
