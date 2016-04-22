#!/usr/bin/python

'''This script is used to test the composition class'''

from component import Component

Water = Component("water")
print "Water Cv (liquid phase) coefficients", Water.PropCoeff["Cv_liquid"]

Methanol = Component("methanol")
print "Methanol chemical formula = ", Methanol.PropCoeff["chemical_formula"]

print "Methanol Cp (gas phase) value = ", Methanol.Cp(273,"gas")
