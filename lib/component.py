#!/usr/bin/python
'''This package contains the base component class.'''

import os
import sys
import numpy as np
import utils 

class Component:
    def __init__(self,name):
        
        '''If a compontent object is created then we grab the
        required values/coefficients from the database. This data can
        then be used to calc. any desired property for a given
        temperature and pressure.'''

        self.name = name # chemical name or abbrev
        self.PropCoeff = self.getPropCoefficientDict(self.name) #get the property dictionary

    #Component Methods
    def getPropCoefficientDict(self,name):

        '''This function pulls all physical data from the database and
        returns it in the form of a dictionary.'''
        
        #find the data base entry
        prop_file_path = self.getLocation(name)

        #Load the data/handle the data
        PropCoeff = self.getFromDatabase(prop_file_path)
        
        return PropCoeff
    
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
        
        '''grabs all physical prop data from file and puts it in a dictionary'''

        # altertaive method using the pandas packages. Might be worth
        # doing later if fiel sizes get substantial
        #mycols = ["variable","equation_number","c1","c2","c3","c4","c5"] 
        #df = pd.read_csv(prop_file_path,names=mycols,engine="python")
        # print df
        
        PropertyCoefficientDict = {}
        data_file = open(prop_file_path,'r')

        #parse each line and handle the data
        for line_number, line in enumerate(data_file.readlines()):
            if line_number !=0: #ignore the header

                if line.startswith("AMW"):
                    PropertyCoefficientDict["AWM"] = float(line.split(',')[1])
                elif line.startswith("chemical_formula"):
                    PropertyCoefficientDict["chemical_formula"] = line.split(',')[1]
                else: #take values, ignore carriage return and convert a numpy array of floats
                    PropertyCoefficientDict[line.split(',')[0]] = np.asarray(line.split(',')[1:len(line.split(','))-1],'float')

        data_file.close()
        return PropertyCoefficientDict


    def Cp(self,T,state):

        # get coefficients based on state
        if state == "solid":
            Cp_coeffs = self.PropCoeff["Cp_solid"]
        elif state == "liquid":
            Cp_coeffs = self.PropCoeff["Cp_liquid"]
        elif state == "gas":
            Cp_coeffs = self.PropCoeff["Cp_gas"]
        else:
            print "Component.Cp Error: unknown state of matter "
            print "'" + str(state) + "' passed as an argument!"
            sys.exit()


        # select the correct equation
        eq_number = int(Cp_coeffs[0])

        # computer the heat capacity value
        if eq_number == 1:
            Cp = np.sum(Cp_coeffs[1:-1])
        else:
            print "Component.Cp Error: only one Cp equation is"
            print "currently supported!"
            sys.exit()

        return Cp