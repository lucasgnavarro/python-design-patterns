#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Lucas Navarro (lucasgnavarro@gmail.com)"
__copyright__ = "Copyright (C) 2018- Lucas Navarro"

# Python Version 3.6
#
# Example of Abstract Factory design pattern

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from utils import print_line, clean_line


class Vehicle:
    mph = 0
    max_mph = 120

    def accelerate(self):
        if self.mph < self.max_mph:
            self.mph += 1
            print('Accelerating to {0} Mph'.format(self.mph))

    def stop(self):
        if self.mph > 0:
            self.mph -= 1
            print('Stoping to {0} Mph'.format(self.mph))


class Car(Vehicle):

    def __init__(self):
        print_line()
        print('Car created')


class Bus(Vehicle):

    def __init__(self):
        print_line()
        print('Bus created')


class Motorcycle(Vehicle):

    def __init__(self):
        print_line()
        print('Motorcycle created')


class VehicleFactory:   # Factory class

    availables_vehicles = {
        'car': Car,
        'bus': Bus,
        'motorcycle': Motorcycle
    }

    def create_vehicle(self, vehicle_type=None):
        if vehicle_type is None or vehicle_type not in self.availables_vehicles:
            print('Vehicle choices are : {0}'.format(list(self.availables_vehicles.keys())) )
        else:
            return self.availables_vehicles[vehicle_type]()


if __name__ == '__main__':

    # Build the factory
    factory = VehicleFactory()

    # Create Car
    car = factory.create_vehicle(vehicle_type='car')
    car.accelerate()
    car.stop()

    # Create bus
    bus = factory.create_vehicle(vehicle_type='bus')
    bus.accelerate()
    bus.stop()

    #Build Motorcycle
    moto = factory.create_vehicle(vehicle_type='motorcycle')
    moto.accelerate()
    moto.stop()
