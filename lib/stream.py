#!/usr/bin/python
'''This is the base Stream class. Very basic for now. We need to
decide on the minimum things that are required to be specified.
'''
import numpy as np
import sys

class Stream:

    def __init__(self, components, mole_fracs=None,
                 mass_fracs=None,mass_flowrate=None,
                 volumetric_flowrate=None,temperature=273,
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

        
    def addComponent(self,component_name,mols=None,
                     mass=None,new_mole_frac=None,
                     new_mass_frac=None):

        ''' add a new component and update mix properties'''
        
        #update the component list
        newComponent = Component(component_name)
        self.Components.append(newComponent)                
                
        #update the mass/mole fraction lists by checking args
        #in order of priority, not yet functional
        if mols != None:
            pass
        elif mass != None:
            pass
        elif new_mole_frac !=None:
            pass
        elif new_mass_frac !=None:
            pass
        else:
            print "Stream.addComponent Error: quantity of component"
            print "to be added must be supplied as an arg!"
            sys.exit()
        

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

    
        
            


        
        
