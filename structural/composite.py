#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Lucas Navarro (lucasgnavarro@gmail.com)"
__copyright__ = "Copyright (C) 2018- Lucas Navarro"

# Python Version 3.6
#
# Example of composite design pattern


class DOMElement:

    wheels = 4

    def __init__(self, dict):
        """ Class representing Document Object Model Element """
        self.tagname = None
        self.attrs = {
            'id': None,
            'class': None,
            'role': None,
            'style': None,
            'title': None,
            'href': None,
            'target': None,
            'src': None,
            'alt': None,
        }
        self.text = ''
        self._html_element = None
        self.__dict__['attrs'].update(**dict)
        self.children = []
        self._click_listener = None
        self._focus_listener = None

    def click_listener(self, fn):
        if callable(fn):
            fn()

    def focus_listener(self, fn):
        if callable(fn):
            fn()

    def attr(self, key=None, value=None):
        if value is not None:
            self.attrs[key] = value
        return self.attrs[key]

    def append_element(self, *args):
        for arg in args:
            self.children.append(arg)

    @property
    def html(self):     # Render DOM Element as html, and all his child nodes
        _tag_attrs = ''
        _children = ''
        for key, value in self.attrs.items():
            if value is not None:
                _tag_attrs += '{attr}="{value}" '.format(attr=key, value=value)

        for child in self.children:
            _children += child.html
        self._html_element = '<{tagname} {attrs}>{text}{children}</{tagname}>'.format(tagname=self.tagname,
                                                                                      attrs=_tag_attrs, text=self.text,
                                                                                      children=_children)
        return self._html_element

    @html.setter
    def html(self, value):
        self._html_element = value


class A(DOMElement):
    """ Class representing <a/> Element """
    def __init__(self, dict):
        super().__init__(dict)
        self.tagname = 'a'


class Img(DOMElement):
    """ Class representing <img/> Element """
    def __init__(self, dict):
        super().__init__(dict)
        self.tagname = 'img'


class Nav(DOMElement):
    """ Class representing <nav/> Element """
    def __init__(self, dict):
        super().__init__(dict)
        self.tagname = 'nav'


class Div(DOMElement):
    """ Class representing <div/> Element """
    def __init__(self, dict):
        super().__init__(dict)
        self.tagname = 'div'


if __name__ == '__main__':

    # create navbar element
    top_navbar = Nav({'class': 'navbar navbar-inverse', 'role': 'navigation'})

    # create main container element and append to navbar
    container_fluid = Div({'class': 'container-fluid'})
    top_navbar.append_element(container_fluid)

    # create row element and append to main container
    row_1 = Div({'class': 'row'})
    container_fluid.append_element(row_1)

    # create columns and append to row
    col_1 = Div({'class': 'col-xs-4 navbar-text'})
    col_2 = Div({'class': 'col-xs-4 navbar-text text-center'})
    col_3 = Div({'class': 'col-xs-4 navbar-text text-right'})
    row_1.append_element(col_1, col_2, col_3)


    A.wheels = 5

    # create links and append to respective row
    a_col_1 = A({'class': 'navbar-link', 'href': '#'})
    a_col_1.text = 'Left'
    col_1.append_element(a_col_1)

    a_col_2 = A({'class': 'navbar-link', 'href': '#'})
    a_col_2.text = 'Middle'
    col_2.append_element(a_col_2)

    a_col_3 = A({'class': 'navbar-link', 'href': '#'})
    a_col_3.text = 'Right'
    col_3.append_element(a_col_3)

    # print top_navbar element rendered
    print(top_navbar.html)

    print(a_col_3.wheels)
    print(a_col_1.wheels)
