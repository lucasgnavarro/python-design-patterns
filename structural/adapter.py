#!/usr/bin/env python3
# -*- coding : utf-8 -*-

__author__ = "Lucas Navarro (lucasgnavarro@gmail.com)"
__copyright__ = "Copyright (C) 2018- Lucas Navarro"

# Python Version 3.6
#
# Example of Adapter design pattern
import sys
import os
from time import sleep
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from utils import clean_line


class Tablet:
    max_input_voltage = 5.5

    def check_voltage(self, voltage):
        _v_is_valid = True
        if voltage > self.max_input_voltage:
            _v_is_valid = False
            print('Voltage is invalid, max permitted {0:.2f}V'.format(self.max_input_voltage))

        return _v_is_valid

    def charge(self, input_voltage=0.0):
        if self.check_voltage(input_voltage):
            for percentage in range(1, 11):
                self.print_charge_percentage(percentage)

            # when charge is complete
            clean_line()
            print('Charge is complete')

    def print_charge_percentage(self, percentage):
        _pretty_battery = list('[         ]')
        for i in range(1, percentage):
            _pretty_battery[i] = '='
        sleep(0.2)

        if percentage > 1:
            clean_line()

        print('Charging : ' + "".join(_pretty_battery) + '>')


class Socket:
    output_voltage = None


class EUSocket(Socket):
    output_voltage = 230


class USSocket(Socket):
    output_voltage = 120


class ARSocket(Socket):
    output_voltage = 220


# Adapter
class ARAdapter:
    input_voltage = ARSocket.output_voltage
    output_voltage = Tablet.max_input_voltage


if __name__ == '__main__':

    tablet = Tablet()
    tablet.charge(EUSocket.output_voltage)  # Oops, this not work

    # implements the adapter
    tablet2 = Tablet()
    tablet.charge(ARAdapter.output_voltage)
