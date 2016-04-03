#!/usr/bin/python
'''This package contains the base species class. For now our
properties are not functions of temperature. This level of complexity
will be added later!!!'''

class Species:
    def __init__(self,name,chem_form,rho,
                 k,cp,cv,mu,amw,mp,bp):
        
        ''' Properties'''
        self.name = name # chemical name or abbrev
        self.chem_form = chem_form # chemical formula 
        self.rho = rho # density
        self.k = k     # thermal cond.
        self.cp = cp   # heat capacity @const. p
        self.cv = cv   # heat capacity @const. v
        self.mu = mu   # viscosity
        self.amw = amw # avergage molecular weight
        self.mp = mp   # melting point
        self.bp = bp   # boiling point

        '''Units (should be objects at some point...)'''
        self.rho_unit = "kg.m$^{-3}$"
        self.k_unit = "W.m$^{-1}$.K$^{-1}$"
        self.cp_unit = "J.kg$^{-1}$.K$^{-1}$"
        self.mu_unit = "Pa.s"
        self.amw_unit = "g.mol$^{-1}$"
        self.mp_unit = "K"
        self.bp_unit = "K"

    def getPhysState(self,T):
        
        # Inputs
        # T = current temp in K
        
        if T > bp:
            return "g"
        elif T > mp:
            return "l"
        else:
            return "s"


    
