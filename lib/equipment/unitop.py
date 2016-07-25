#!/usr/bin/python

'''general unit operations class:

This is where we add the base functionality expected unit op type
object. 

'''

from component import Component
import numpy as np

#------------------------------------------------------------------------------

class UnitOp:
    #basic unit operations class

    def __init__(self,temperature=333,pressure=100000,molar_inflow=39.59,components=None,mole_fracs=None):
                
        self.molar_inflow = molar_inflow
        self.temperature = temperature
        self.pressure = pressure
        
        self.components = components#[Component("methanol"), Component("water")]        
        self.mole_fracs = mole_fracs

