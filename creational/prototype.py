#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Lucas Navarro (lucasgnavarro@gmail.com)"
__copyright__ = "Copyright (C) 2018- Lucas Navarro"

# Python Version 3.6
#
# Example of Prototype design pattern

from copy import deepcopy
from types import MethodType


class Shape:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.color = 'white'

    def get_mem_addr(self):
        return id(self)

    def clone(self, **kwargs):

        cloned_object = deepcopy(self)
        for key in kwargs:
            if callable(kwargs[key]):   # if is callable, we use MethodType to add it dynamically to cloned_object
                setattr(cloned_object, key, MethodType(kwargs[key], cloned_object))
            else:
                setattr(cloned_object, key, kwargs[key])

        return cloned_object


class Circle(Shape):

    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.type = 'Circle'


if __name__ == '__main__':

    ball = Circle(x=10, y=10)
    ball2 = ball.clone(color='red', x=55)

    print(ball.__dict__)
    print(ball.get_mem_addr())

    print(ball2.__dict__)
    print(ball2.get_mem_addr())
