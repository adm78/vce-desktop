#!/usr/bin/python

'''This script is used to test the composition class'''

from component import Component

Methanol = Component("methanol")
print "Methanol chemical formula = ", Methanol.Prop["chemical_formula"]
print "Methanol Cp (liq phase) coeffs =", Methanol.Prop["Cp_liquid"].coeffs
print "Methanol Cp (liq phase) eqn =", Methanol.Prop["Cp_liquid"].eqn
print "Methanol Cp (liq phase) Tmin =", Methanol.Prop["Cp_liquid"].Tmin, "K"
print "Methanol Cp (liq phase) Tmax =", Methanol.Prop["Cp_liquid"].Tmax, "K"
print "Methanol Cp (liq phase) unit =", Methanol.Prop["Cp_liquid"].unit
print "Methanol Cp (liq phase) value @273K = ", Methanol.Cp(273,state="liquid",unit=True)
print "Methanol Cp (liq phase) value @333K = ", Methanol.Cp(333,state="liquid",unit=True)
print "Methanol Cp (liq phase) value @273K (no unit display) = ", Methanol.Cp(273,state="liquid")
print "Methanol Cp (liq phase) value @273K (sep. unit display) = ", Methanol.Cp(273,state="liquid"),Methanol.CpUnit("liquid") 
print "Methanol Pvap (liq phase) value @273K = ", Methanol.Pvap(273,state="liquid",unit=True)
print "Methanol Pvap (liq phase) value @333K = ", Methanol.Pvap(333,state="liquid",unit=True)
print "Methanol Pvap (liq phase) value @333K (sep. unit display) = ", Methanol.Pvap(333,state="liquid"),Methanol.PvapUnit("liquid")
