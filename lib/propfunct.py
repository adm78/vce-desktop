#!/usr/bin/python

import sys
import numpy as np

#-------------------------------------------------------------------------
class PhysicalProperty:

    #abstract physical property class
    
    def __init__(self,coeffs=[1],
                 Tmin=None,Tmax=None,unit="-"):
        
        self.coeffs = coeffs
        self.Tmin = Tmin
        self.Tmax = Tmax
        self.unit = unit

    def value(self,T):
        '''by default the value is just that of the first coeffient'''
        return self.coeffs[0]

#-------------------------------------------------------------------------
class Cp_liq(PhysicalProperty):

    def __init__(self,eqn=1,coeffs=[1],
                 Tmin=None,Tmax=None,unit="-"):

        PhysicalProperty.__init__(self,coeffs=coeffs,
                                  Tmin=Tmin,Tmax=Tmax,unit=unit)
        self.eqn = eqn
        
    def value(self,T):
        
        if self.eqn == 1:
            value = self.coeffs[0]

        elif self.eqn == 2:

            #compute Cp = A + BT + CT**2 + D*T**3 + ...
            value = 0.0
            for i, coeff in np.ndenumerate(self.coeffs):
                value += coeff*T**i[0]

        else:
            print "Cp_liq.value Error: equation number", eqn, " does"
            print "not match any known Cp_liq equation!"
            sys.exit()

        return value
            
#-------------------------------------------------------------------------


        
        
