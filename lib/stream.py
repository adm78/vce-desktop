#!/usr/bin/python
'''This is the base Stream class. Very basic for now. We need to
decide on the minimum things that are required to be specified.
'''
import numpy as np
import sys

class Stream:

    def __init__(self, components, mole_fracs=None,
                 mass_fracs=None,mass_flowrate=None,
                 volumetric_flowrate=None,temperature=293,
                 pressure=None,enthalpy=None,state=None):
        
        '''Stream properties'''
        self.Components = components # a list of Component objects
        self.mole_fracs = mole_fracs  # (in order)
        self.mass_fracs =  mass_fracs # (in order)
        self.mass_flowrate = mass_flowrate
        self.volumetric_flowrate = volumetric_flowrate
        self.temperature = temperature
        self.pressure = pressure
        self.enthalpy = enthalpy
        self.state = state
        
        '''calculate missing data where possible'''
        self.calcMissingData()

            

    def calcMissingData(self):

        # we need an intelligent decision function here.
        # it should be able to look at the properties we have and 
        # decide what missing data can be computed.  
        pass

    def Cp(self,unit=False):

        '''A stream heat capacity function. Lets assume that heat capcities
        are given on a molar basis for now'''
        
        # locals
        T = self.temperature
        state = self.state
        Cp = 0.0
        
        # loop through components and add Cp 
        # to overall mole weighted Cp of stream
        for i, component in enumerate(self.Components):
            Cp += self.mole_fracs[i]*component.Cp(self.temperature,state=self.state)

            #ensure units are the same
            if i == 0:
                first_unit = component.CpUnit(state=self.state)
            else:
                if component.CpUnit(state=self.state) != first_unit:
                    print "Stream.Cp Error: units of Cp differ between components!"
                    sys.exit()

        if unit:
            return Cp, first_unit
        else:
            return Cp
    

    def CpUnit(self):
        #quick and dirty unit finder
        return self.Cp(unit=True)[1]


    def Pvap(self,unit=False):

        '''A stream heat capacity function. Lets assume that heat capcities
        are given on a molar basis for now'''
        
        # locals
        T = self.temperature
        state = self.state
        Pvap = 0.0
        
        # loop through components and add Cp 
        # to overall mole weighted Cp of stream
        for i, component in enumerate(self.Components):
            Pvap += self.mole_fracs[i]*component.Pvap(self.temperature,state=self.state)

            #ensure units are the same
            if i == 0:
                first_unit = component.PvapUnit(state=self.state)
            else:
                if component.PvapUnit(state=self.state) != first_unit:
                    print "Stream.Pvap Error: units of Pvap differ between components!"
                    sys.exit()

        if unit:
            return Pvap, first_unit
        else:
            return Pvap


    def PvapUnit(self):
        #quick and dirty unit finder
        return self.Pvap(unit=True)[1]

    
        
            


        
        
