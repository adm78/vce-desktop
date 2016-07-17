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

    def __init__(self,temperature=333,pressure=100000,molar_inflow=39.59,
                 components=None,mole_fracs=None, debug=False):
    
        UnitOp.__init__(self,temperature=temperature,pressure=pressure,molar_inflow=molar_inflow,components=components,mole_fracs=mole_fracs)
        
        self.vle = np.zeros(len(self.components))
        self.xi = np.zeros(len(self.components))
        self.yi = np.zeros(len(self.components))

        self.debug = debug

    def getVLEConst(self):

        if self.debug:
            print "determining VLE constants for each component..."
            
        for i, component in enumerate(self.components):
            const = component.Pvap(self.temperature,state="liquid")/self.pressure
            self.vle[i] = const
            
        if self.debug:
            print 'VLE constants: ', self.vle
        

    # def binary_flash(self):
        
    #     '''determining output stream compositions in a binary mixture since Rachford-Rice
    #     seems iffy here...'''

    #     self.xi[0] = (1-self.vle[1])/(self.vle[0]-self.vle[1])
    #     print "xi[0] = ", self.xi[0]
    #     self.xi[1] = 1.0 - self.xi[0]
    #     self.beta = (self.mole_fracs[0] - self.xi[0])/(self.vle[0] - self.xi[0])
    #     self.yi[0] = self.vle[0]*self.mole_fracs[0]
    #     self.yi[1] = 1.0 - self.yi[0]

    #     print "xi = ", self.xi
    #     print "yi = ", self.yi
    #     print "beta = ", self.beta
        
        
        
    
    def rach_rice(self):

        if self.debug:
            print "determining the ratio of vapour to inlet flowrate..."

        
                
        def f(beta):
            return np.sum((self.mole_fracs*(self.vle - 1.0))/(1.0 + beta*(self.vle - 1.0)))
        
        def fabs(beta):
            return np.absolute(np.sum((self.mole_fracs*(self.vle - 1.0))/(1.0 + beta*(self.vle - 1.0))))

        def f_np(beta):
            residual = 0.0
            for i in range(len(self.components)):
                residual += self.mole_fracs[i]*(self.vle[i] - 1.0)/(1.0 + beta*(self.vle[i] - 1.0))
            return residual

        flash_state = self.checkFlashValidity()
        if flash_state == "liquid_phase":
            if self.debug:
                print "negative flash, beta set to zero"
            self.beta = 0.0
            self.xi = self.mole_fracs
            self.yi = self.vle * self.xi
            self.yi = self.yi/np.sum(self.yi)
            
        elif flash_state == "gas_phase":
            if self.debug:
                print "negative flash, beta set to unity"
            self.beta = 1.0
            self.yi = self.mole_fracs
            self.xi = self.mole_fracs/ (1.0 + self.beta * (self.vle - 1.0))
            self.xi = self.xi/np.sum(self.xi)
            
        else:
            if self.debug:
                print "we might have two phases!"
            try:
                self.beta = brentq(f,0.0,1.0)
            
            except ValueError:
                
                if self.debug:
                    print "trying fmin solver..."
                    # fig, ax = plt.subplots(1)
                    # beta = np.linspace(-50.0,50.0, 500)
                    # ax.plot(beta, f_np(beta))
                    # plt.grid(True)
                    # plt.show()
                            
                    
                beta_guess = 0.5
                self.beta = fmin(fabs, beta_guess, maxiter=10000)
                
                if self.debug:
                    print "fmin beta solution = ", self.beta

            if self.beta < 0.0:
                
                if self.debug:
                    print "negative flash, beta set to zero"
                    
                self.beta = 0.0
                self.xi = self.mole_fracs
                self.yi = self.vle * self.xi
                self.yi = self.yi/np.sum(self.yi)
                
            elif self.beta > 1.0:
                if self.debug:
                    print "negative flash, beta set to unity"
                    
                self.beta = 1.0
                self.yi = self.mole_fracs
                self.xi = self.mole_fracs/ (1.0 + self.beta * (self.vle - 1.0))
                self.xi = self.xi/np.sum(self.xi)

            else:
                if self.debug:
                    print "a real live flash has happended!"
                self.xi = self.mole_fracs/ (1.0 + self.beta * (self.vle - 1.0))
                self.yi = self.vle * self.xi
                
        if self.debug:
            print 'Liquid mol fractions ', self.xi
            print 'Vapour mol fractions ', self.yi

    def checkFlashValidity(self):

        '''checks if the flash can have a solution in the region 0 <
        beta < 1 and returns a string as:
        
        1.) "liquid_phase": beta_min and beta_max < 0, 
        assume beta = 0, xi = zi, yi = rachford eqn normed.
        2.) "gas_phase": beta_min and beta_max > 1, 
        assume beta = 1, yi = zi, xi = rachford eqn normed.
        3.) "two_phase": beta_min, beta_max lie on opposite 
        sides or 0, 1 or both, beta_mix may be in range 0 - 1, but may not be. 
        
        based on reading from on the negative flash from Whitson,
        Fluid Phase Equilibria 1989

        Doesn't seem to be behavinf as expected when all K values are < 1.0

        '''

        beta_min = 1.0/(1.0 - np.amax(self.vle))
        beta_max = 1.0/(1.0 - np.amin(self.vle))
        if self.debug:
            print "beta_max =", beta_max
            print "beta_min =", beta_min
        K_min = np.amin(self.vle)
        K_max = np.amax(self.vle)

        if K_min < 1.0 and K_max < 1.0:
            return "liquid_phase"
        elif K_min > 1.0 and K_max > 1.0:
            return "gas_phase"
        else:
            return "two_phase"

    

    
