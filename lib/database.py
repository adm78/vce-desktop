#!/usr/bin/python
'''This library contains the main database methods required to creat
compontents and querey the property database.'''

import utils
import thermo
import sys
import os
import numpy as np

def getPropDict(name):

    '''This is the public API used by the programing class. This function
    pulls all physical data from the database and returns it in the
    form of a dictionary.

    '''

    #find the data base entry
    prop_file_path = getLocation(name)

    #Load the data/handle the data
    Prop = getFromDatabase(prop_file_path)

    return Prop

def getLocation(name):

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

def getFromDatabase(prop_file_path):

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
                PropertyData["AWM"] = thermo.PhysicalProperty(unit=unit,coeffs=coeffs)

            elif line.startswith("chemical_formula"):
                PropertyData["chemical_formula"] = line.split()[1]

            elif line.startswith("melting_point"):

                coeffs = float(line.split()[1])
                PropertyData["melting_point"] = thermo.PhysicalProperty(unit=unit,coeffs=coeffs)

            elif line.startswith("boiling_point"):

                coeffs = float(line.split()[1])
                PropertyData["boiling_point"] = thermo.PhysicalProperty(unit=unit,coeffs=coeffs)

            # standard physical properties with Tmin and Tmax
            elif line.startswith("Pvap_liq"):

                eqn = int(line.split()[1])
                coeffs = np.array(line.split()[2:len(line.split())-3],dtype=float) 
                Tmin = float(line.split()[len(line.split())-3])
                Tmax = float(line.split()[len(line.split())-2])
                PropertyData["Pvap_liquid"] = thermo.Vapour_pressure_liq(eqn=eqn,coeffs=coeffs,
                                                                Tmin=Tmin,Tmax=Tmax,
                                                                unit=unit)

            elif line.startswith("Cp_liquid"): 

                eqn = int(line.split()[1])
                coeffs = np.array(line.split()[2:len(line.split())-3],dtype=float) 
                Tmin = float(line.split()[len(line.split())-3])
                Tmax = float(line.split()[len(line.split())-2])
                PropertyData["Cp_liquid"] = thermo.Cp_liq(eqn=eqn,coeffs=coeffs,
                                                                Tmin=Tmin,Tmax=Tmax,
                                                                unit=unit)

            else: 
                print "Component.getFromDatabase Error: Unexpected physical property"
                print "with name", line.split()[0], " in database file "
                print prop_file_path
                sys.exit()

    data_file.close()
    return PropertyData
