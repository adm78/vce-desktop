#!/usr/bin/python
'''This package contains the base component class.'''

import os
import sys
import numpy as np
import utils 
import propfunct as pf
import inspect

class Component:
    def __init__(self,name):
        
        '''If a compontent object is created then we grab the
        required values/coefficients from the database. This data can
        then be used to calc. any desired property for a given
        temperature and pressure.'''

        self.name = name # chemical name or abbrev
        self.Prop = self.getPropDict(self.name) #get the property dictionary

    #Component Methods
    def getPropDict(self,name):

        '''This function pulls all physical data from the database and
        returns it in the form of a dictionary.'''
        
        #find the data base entry
        prop_file_path = self.getLocation(name)

        #Load the data/handle the data
        Prop = self.getFromDatabase(prop_file_path)
        
        return Prop
    
    def getLocation(self,name):

        '''A simple location finder. Returns the absolute path of the database
        entry for the target component by name. Every component entry
        is on the top level of the properties directory for now so all
        we do is check that a file exits. Should avoid a bunch of
        re-coding later.

        '''
        target_filename = name + '.dat'
        full_path = os.path.abspath(os.path.join(utils.getVCEPropertiesPath(),target_filename))
        if not os.path.exists(full_path):
            sys.exit("Component.getLocation Error: " + full_path + " does not exist.")

        return full_path
        
    def getFromDatabase(self,prop_file_path):
        
        '''grabs all physical prop data from file, saving each as a Physical
        property object (or extension of this class). If you add a new
        property then you must add the appropriate 'elif' check
        below

        '''
        
        PropertyData = {}
        data_file = open(prop_file_path,'r')

        #parse each line and handle the data accordingly 
        for line_number, line in enumerate(data_file.readlines()):
            if line_number !=0: #ignore the header

                unit = line.split()[-1]
                
                if line.startswith("AMW"):

                    coeffs = float(line.split()[1])
                    PropertyData["AWM"] = pf.PhysicalProperty(unit=unit,coeffs=coeffs)

                elif line.startswith("chemical_formula"):
                    PropertyData["chemical_formula"] = line.split()[1]

                elif line.startswith("melting_point"):
                        
                    coeffs = float(line.split()[1])
                    PropertyData["melting_point"] = pf.PhysicalProperty(unit=unit,coeffs=coeffs)

                elif line.startswith("boiling_point"):

                    coeffs = float(line.split()[1])
                    PropertyData["boiling_point"] = pf.PhysicalProperty(unit=unit,coeffs=coeffs)

                # standard physical properties with Tmin and Tmax
                elif line.startswith("Pvap_liq"):
                    
                    eqn = int(line.split()[1])
                    coeffs = np.array(line.split()[2:len(line.split())-3],dtype=float) 
                    Tmin = float(line.split()[len(line.split())-3])
                    Tmax = float(line.split()[len(line.split())-2])
                    PropertyData["Pvap_liquid"] = pf.Vapour_pressure_liq(eqn=eqn,coeffs=coeffs,
                                                                    Tmin=Tmin,Tmax=Tmax,
                                                                    unit=unit)

                elif line.startswith("Cp_liquid"): 
                    
                    eqn = int(line.split()[1])
                    coeffs = np.array(line.split()[2:len(line.split())-3],dtype=float) 
                    Tmin = float(line.split()[len(line.split())-3])
                    Tmax = float(line.split()[len(line.split())-2])
                    PropertyData["Cp_liquid"] = pf.Cp_liq(eqn=eqn,coeffs=coeffs,
                                                                    Tmin=Tmin,Tmax=Tmax,
                                                                    unit=unit)

                else: 
                    print "Component.getFromDatabase Error: Unexpected physical property"
                    print "with name", line.split()[0], " in database file "
                    print prop_file_path
                    sys.exit()

        data_file.close()
        return PropertyData


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

    
        

