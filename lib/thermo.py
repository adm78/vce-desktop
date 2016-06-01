#!/usr/bin/python

import sys
import numpy as np
import scipy.constants as const

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
class Vapour_pressure_liq(PhysicalProperty):
    
    def __init__(self,eqn=1,coeffs=[1],
                 Tmin=None,Tmax=None,unit="-"):

        PhysicalProperty.__init__(self,coeffs=coeffs,
                                  Tmin=Tmin,Tmax=Tmax,unit=unit)
        self.eqn = eqn
        
    def value(self,T):

        '''Returns the full vapour pressure in equilibrium with a pure liquid of the
        same species'''

        if self.eqn == 1:
            value = self.coeffs[0]

        elif self.eqn == 2:

            #compute Vp = exp(A + (B/T) + C*lnT + D*T**E)
            p1 = self.coeffs[0] + (self.coeffs[1]/T)
            p2 = self.coeffs[2]*np.log(T) + self.coeffs[3]*T**self.coeffs[4]
            value = np.exp(p1 + p2)

        else:
            print "Vapour_pressure_liq.value Error: equation number", eqn, " does"
            print "not match any known Vapour_pressure_liq equation!"
            sys.exit()

        return value
#-------------------------------------------------------------------------
def IdealGasPressure(n=40.8969,T=298.15,V=1,molar_conc=None,
                     mass_conc=None,amw=None,unit=False):

    ''' Returns the ideal gas pressure.

    Runs through args in order of priority:
    1) molar_conc , T
    2) mass_conc, amw, T
    3) n, V, T

    !args
    n = moles of gas present / [moles]
    T = gas temperature / [K]
    V = gas volume / [m**3]
    molar_conc = molar concentration / [mol.m**{-3}]
    mass_conc = mass concentration / [g.m**{-3}]
    amw = average molecular weight / [g.mol**{-1}] 
    
    '''

    R = const.R

    if molar_conc != None:
        P = molar_conc*R*T
    elif mass_conc != None:
        if amw == None:
            print "thermo.IdealGasPressure Error: if mass_conce arg is provided"
            print "then amw must also be specified!"
            sys.exit()
        else:
            P = mass_conc*R*T/amw
    else:
        P = n*R*T/V

    if unit:
        return P, "Pa"
    else:
        return P

#-------------------------------------------------------------------------    
def IdealGasVolume(n=40.8969,T=298.15,
                   P=101325.0,unit=False):

    ''' Returns the ideal gas volume.

    !args
    n = moles of gas present / [moles]
    T = gas temperature / [K]
    P = gas pressure / [Pa]
    
    '''

    R = const.R
    V = n*R*T/P

    if unit:
        return V, "m^3"
    else:
        return V

#-------------------------------------------------------------------------    
def IdealGasTemperature(n=40.8969,V=1,
                        P=101325.0,unit=False):

    ''' Returns the ideal gas volume.

    !args
    n = moles of gas present / [moles]
    V = gas volume / [m^3]
    P = gas pressure / [Pa]
    
    '''

    R = const.R
    T = P*V/(n*R)

    if unit:
        return T, "[K]"
    else:
        return T

#-------------------------------------------------------------------------    
def IdealGasConc(P=101325.0,T=298.15,unit=False):

    ''' Returns the ideal gas molar concentration.

    !args
    n = moles of gas present / [moles]
    T = gas temperature / [K]
    P = gas pressure / [Pa]
    
    '''

    R = const.R
    C = P/(R*T)

    if unit:
        return C, "[mol*m^{-3}]"
    else:
        return C
