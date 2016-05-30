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

    
        

