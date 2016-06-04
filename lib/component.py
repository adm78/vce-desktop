#!/usr/bin/python
'''This package contains the base component class.'''

import inspect
import database

class Component:
    def __init__(self,name):
        
        '''If a compontent object is created then we grab the
        required values/coefficients from the database. This data can
        then be used to calc. any desired property for a given
        temperature and pressure.'''

        self.name = name # chemical name or abbrev
        self.Prop = database.getPropDict(self.name) #get the property dictionary
        self.AMW = self.Prop["AMW"].value
        self.AMWUnit = self.Prop["AMW"].unit

    #Component Methods
    def checkValidState(self,state):
        # as it says on the tin, fatal error on test failure
        if (state != "liquid") and (state != "solid") and (state != "gas"):
            print "component.checkValidState Error: unknown state of matter"
            print state, "passed as an arg!"
            sys.exit()
        else:
            return True
    
    def getStateDependentValue(self,fname,T,
                               state="gas",unit=False):
        
        '''get the value/unit based on the function called
        and the state'''
        prop_name = fname + "_" + state
        prop_value = self.Prop[prop_name].value(T)
        prop_unit = self.Prop[prop_name].unit

        return prop_value, prop_unit 


    def getStateDependentUnit(self,fname,state="gas"):
        
        '''get the unit based on the function called
        and the state'''
        fname = ''.join(fname.split())[:-4] #strip the "Unit" from the f name
        prop_name = fname + "_" + state
        return self.Prop[prop_name].unit #return the correct unit

    def Cp(self,T,state="gas",unit=False):

        fname = inspect.stack()[0][3] #get the name of the func being called
        self.checkValidState(state) #check the state is valid
        Cp, Cp_unit = self.getStateDependentValue(fname,T,state,unit)  #get the value/units

        if unit:
            return Cp, Cp_unit
        else:
            return Cp

    def CpUnit(self,state="gas"):

        #return only the unit 
        fname = inspect.stack()[0][3]
        return self.getStateDependentUnit(fname,state)

    def Pvap(self,T,state="gas",unit=False):
        
        fname = inspect.stack()[0][3] #get the name of the function being called
        self.checkValidState(state) # check the state is okay
        Pvap, Pvap_unit = self.getStateDependentValue(fname,T,state,unit) 

        if unit:
            return Pvap, Pvap_unit
        else:
            return Pvap

    def PvapUnit(self,state="gas"):
        
        #return only the unit 
        fname = inspect.stack()[0][3]
        return self.getStateDependentUnit(fname,state)

    def rho(self,T,state="liquid",
            unit=False,mass=False):
        
        '''returns the mass or molar density of a component depending
        on the args.'''

        fname = inspect.stack()[0][3] #get the name of the function being called
        self.checkValidState(state) # check the state is okay
        rho, rho_unit = self.getStateDependentValue(fname,T,state,unit) 

        #check if the value is to be converted to mass form
        if mass: 
            if rho_unit == "kmol*m^{-3}":
                rho= rho*self.AMW
                rho_unit = "kg*m^{-3}"
            else:
                print "Component.rho Error: cannot convert molar density "
                print "to mass form with the molar units present!"
                print "For now liquid denity data must be in kmol*m^{-3}."
                print "Current molar units:", rho_unit
                sys.exit()
            
        
        if unit:
            return rho, rho_unit
        else:
            return rho

    def rhoUnit(self,state="liquid"):
        
        #return only the unit 
        fname = inspect.stack()[0][3]
        return self.getStateDependentUnit(fname,state)    
        

