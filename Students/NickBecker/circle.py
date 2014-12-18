#!/usr/bin/env python

import math


class Circle(object):
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        self._radius = value
        self._diameter = self._radius * 2

    def get_diameter(self):
        self._diameter = self._radius * 2
        return self._diameter

    def set_diameter(self, value):
        self._diameter = value
        self._radius = value / 2

    def get_area(self):
        self._area = math.pi * self._radius ** 2
        return self._area

    radius = property(get_radius, set_radius)
    diameter = property(get_diameter, set_diameter)
    area = property(get_area)
