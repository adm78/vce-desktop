#!/usr/bin/python

'''general unit operations class'''

from component import Component
import numpy as np
from scipy.optimize import fsolve, minimize, fmin
import sys

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
        
        self.vle = np.zeros(len(self.components))
        self.xi = np.zeros(len(self.components))
        self.yi = np.zeros(len(self.components))

    def vle_const(self):
    
        print "determining VLE constants for each component..." 
        
        for i, component in enumerate(self.components):
            const = component.Pvap(self.temperature,state="liquid")/self.pressure
            print "Pvap = ", component.Pvap(self.temperature,state="liquid",unit=True)
            self.vle[i] = const
        
        print 'VLE constants: ', self.vle
        
    def rach_rice(self):
        
        print "determining the ratio of vapour to inlet flowrate..."

        beta_guess = 0.6

        print self.mole_fracs[0], self.mole_fracs[1]        
        print self.vle[0], self.vle[1]
        
        # def f(x): 
        #     y = 0.096/(1-x*0.16) + 0.324/(1-x*0.81)
        #     return y
        
        def f(beta):
            residual = 0.0
            for i in range(len(self.components)):
                residual += self.mole_fracs[i]*(1.0-self.vle[i])/(1.0 + beta*(1.0 - self.vle[i]))
            #return np.sum((self.mole_fracs*(1 - self.vle))/(1.0 + beta*(1.0 - self.vle)))
            return residual

        self.beta = minimize(f,beta_guess,bounds=((0.0, 1.0),))#,options={"maxiter":100000})
       # self.beta = fmin(f,beta_guess)

        
        print self.beta
        sys.exit()
        
        print "beta = ",self.beta
        print "solve_log = ", solve_log
        print "message = ", message
        
        
        
        for i in range(0, len(self.components)):
            self.xi[i] = (self.mole_fracs[i] / (1.0 + self.beta * (self.vle[i] - 1.0)))
            self.yi[i] = (self.vle[i] * self.xi[i])
        
        print 'Liquid mol fractions ', self.xi
        print 'Vapour mol fractions ', self.yi
        
        print "Methanol Pvap (liq phase)", self.components[0].Pvap(self.temperature,state="liquid",unit=True)*self.mole_fracs[0]
        print "Water Pvap (liq phase)", self.components[1].Pvap(self.temperature,state="liquid",unit=True)*self.mole_fracs[1]


# generate test components


optest = FlashTank(temperature=363.0,pressure=2e04)
optest.vle_const()
optest.rach_rice()

    

    
