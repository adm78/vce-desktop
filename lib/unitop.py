#!/usr/bin/python

'''general unit operations class'''

from component import Component
import numpy as np
from scipy.optimize import fsolve

#------------------------------------------------------------------------------

class UnitOp:
    #basic unit operations class

    def __init__(self,temperature=333,pressure=100000,molar_inflow=39.59,components=None,mole_fracs=None):
                
        self.molar_inflow = molar_inflow
        self.temperature = temperature
        self.pressure = pressure
        
        self.components = [Component("methanol"), Component("water")]        
        self.mole_fracs = np.array([0.6,0.4])


class FlashTank(UnitOp):
    # calculates outlet streams' compositions / size of tank required 

    def __init__(self,temperature=333,pressure=100000,molar_inflow=39.59,components=None,mole_fracs=None):
    
        UnitOp.__init__(self,temperature=temperature,pressure=pressure,molar_inflow=molar_inflow,components=components,mole_fracs=mole_fracs)
        
        self.vle = []
        self.xi = []
        self.yi = []

    def vle_const(self):
    
        print "determining VLE constants for each component..." 
        
        for component in self.components:
            const = component.Pvap(self.temperature,state="liquid",unit=False)/self.pressure
            self.vle.append(const)
        
        print 'VLE constants: ', self.vle
        
    def rach_rice(self):
        
        print "determining the ratio of vapour to inlet flowrate..."

        self.beta = 0.4

        print self.mole_fracs[0], self.mole_fracs[1]        
        print self.vle[0], self.vle[1]
        
        def f(x): 
            y = 0.096/(1-x*0.16) + 0.324/(1-x*0.81)
            return y
            
        x = fsolve(f,1.0)
        print x
        
        
        
        
        for i in range(0, len(self.components)):
            self.xi.append(self.mole_fracs[i] / (1 + self.beta * (self.vle[i] - 1)))
            self.yi.append(self.vle[i] * self.xi[i])
        
        print 'Liquid mol fractions ', self.xi
        print 'Vapour mol fractions ', self.yi
        
        print "Methanol Pvap (liq phase)", self.components[0].Pvap(self.temperature,state="liquid",unit=True)
        print "Water Pvap (liq phase)", self.components[1].Pvap(self.temperature,state="liquid",unit=True)


# generate test components


optest = FlashTank()
optest.vle_const()
optest.rach_rice()

    

    
