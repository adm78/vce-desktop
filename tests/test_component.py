#!/usr/bin/python

'''This script is used to test the composition class'''

from component import Component

Water = Component("water")
print Water.PropCoeff["Cv_liquid"]

Methanol = Component("methanol")
print Methanol.PropCoeff["chemical_formula"]
