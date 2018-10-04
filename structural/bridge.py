#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = "Lucas Navarro (lucasgnavarro@gmail.com)"
__copyright__ = "Copyright (C) 2018- Lucas Navarro"

# Python Version 3.6
#
# Example of bridge design pattern
#


from abc import ABC, abstractmethod


class Website(ABC):

    def __init__(self, implementation):
        self._implementation = implementation

    def __str__(self):
        return 'Interface: {}; Implementation{}: '.format(self.__class__.__name__,
                                                          self._implementation.__class__.__name__)

    @abstractmethod
    def show_page(self):
        pass


class FreeWebsite(Website):

    def show_page(self):
        ads = self._implementation.get_ads()
        text = self._implementation.get_excerpt()
        call_to_action = self._implementation.get_call_to_action()
        print(ads)
        print(text)
        print(call_to_action)


class PaidWebsite(Website):

    def show_page(self):
        text = self._implementation.get_article()
        print(text)
        print('')


class Implementation(ABC):

    def get_excerpt(self):
        return 'excerpt from the article'

    def get_article(self):
        return 'full article'

    def get_ads(self):
        return 'some ads'

    @abstractmethod
    def get_call_to_action(self):
        pass


class ImplementationA(Implementation):

    def get_call_to_action(self):
        return 'Pay 10$ a month to remove ads'


class ImplementationB(Implementation):

    def get_call_to_action(self):
        return 'Remove Ads with just 10$ a month'


def main():
    a_free = FreeWebsite(ImplementationA())
    print(a_free)
    a_free.show_page()  # the client interacts only with the interface

    b_free = FreeWebsite(ImplementationB())
    print(b_free)
    b_free.show_page()

    a_paid = PaidWebsite(ImplementationA())
    print(a_paid)
    a_paid.show_page()

    b_paid = PaidWebsite(ImplementationB())
    print(b_paid)
    b_paid.show_page()


if __name__ == '__main__':
    main()
