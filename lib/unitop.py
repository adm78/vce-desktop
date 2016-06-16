#!/usr/bin/python

'''general unit operations class'''

from component import Component
import numpy as np
from scipy.optimize import fsolve, minimize, fmin, brentq
import sys
import matplotlib.pyplot as plt
#------------------------------------------------------------------------------

class UnitOp:
    #basic unit operations class

    def __init__(self,temperature=333,pressure=100000,molar_inflow=39.59,components=None,mole_fracs=None):
                
        self.molar_inflow = molar_inflow
        self.temperature = temperature
        self.pressure = pressure
        
        self.components = components#[Component("methanol"), Component("water")]        
        self.mole_fracs = mole_fracs


class FlashTank(UnitOp):
    # calculates outlet streams' compositions / size of tank required 

    def __init__(self,temperature=333,pressure=100000,molar_inflow=39.59,components=None,mole_fracs=None):
    
        UnitOp.__init__(self,temperature=temperature,pressure=pressure,molar_inflow=molar_inflow,components=components,mole_fracs=mole_fracs)
        
        self.vle = np.zeros(len(self.components))
        self.xi = np.zeros(len(self.components))
        self.yi = np.zeros(len(self.components))

    def getVLEConst(self):
    
        print "determining VLE constants for each component..." 
        for i, component in enumerate(self.components):
            const = component.Pvap(self.temperature,state="liquid")/self.pressure
            #print "Pvap = ", component.Pvap(self.temperature,state="liquid",unit=True)
            self.vle[i] = const
        
        print 'VLE constants: ', self.vle
        

    def binary_flash(self):
        
        '''determining output stream compositions in a binary mixture since Rachford-Rice
        seems iffy here...'''

        self.xi[0] = (1-self.vle[1])/(self.vle[0]-self.vle[1])
        print "xi[0] = ", self.xi[0]
        self.xi[1] = 1.0 - self.xi[0]
        self.beta = (self.mole_fracs[0] - self.xi[0])/(self.vle[0] - self.xi[0])
        self.yi[0] = self.vle[0]*self.mole_fracs[0]
        self.yi[1] = 1.0 - self.yi[0]

        print "xi = ", self.xi
        print "yi = ", self.yi
        print "beta = ", self.beta
        
        
        
    
    def rach_rice(self):
        
        print "determining the ratio of vapour to inlet flowrate..."

        beta_guess = 0.5
                
        def f(beta):
            return np.sum((self.mole_fracs*(self.vle - 1.0))/(1.0 + beta*(self.vle - 1.0)))
            
        # print "f(0.0) = ", f(0.0)
        # print "f(0.5) = ", f(0.5)
        # print "f(1.0) = ", f(1.0)
        
        #fig, axrr = plt.subplots(111)
        # x = np.linspace(0.0,1.0,1000)
        # residual = f(x)
        
        # plt.plot(x,residual)
        # plt.grid(True)
        # plt.xlabel("beta")
        # plt.ylabel("f(beta)")
        # plt.show()
        
        self.beta = brentq(f,0.0,1.0)    
        print "solved beta = ", self.beta       
        
        for i in range(0, len(self.components)):
            self.xi[i] = self.mole_fracs[i] / (1.0 + self.beta * (self.vle[i] - 1.0))
            self.yi[i] = self.vle[i] * self.xi[i]
        
        print 'Liquid mol fractions ', self.xi
        print 'Vapour mol fractions ', self.yi


# generate test components


# optest = FlashTank(temperature=363.0,pressure=1.0e05)
# optest.vle_const()
# optest.rach_rice()

    

    
