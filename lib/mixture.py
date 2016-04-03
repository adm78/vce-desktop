#!/usr/bin/python
''' a base class used to hold combinations of species.'''
import numpy as np

class Mixture:

    def __init__(self):
        
        '''Mixture properties'''
        self.Species = [] # list of species objects in the mix.
        self.x = np.array([]) # list of mass fractions of species (in order)

        '''Average properties of the mix'''
        self.props_list = ["rho", "k", "cp", "amw"]

        '''Units'''
        self.rho_unit = "kg.m$^{-3}$"
        self.k_unit = "W.m$^{-1}$.K$^{-1}$"
        self.cp_unit = "J.kg$^{-1}$.K$^{-1}$"
        self.mu_unit = "Pa.s"
        self.amw_unit = "g.mol$^{-1}$"
        self.x_unit = "-"
       
    def getMassMeanValue(self,prop):
        '''Estimates average of single phys. prop. by mass'''

        #locals
        p_avg = 0.0 

        # loop through the species
        for i,species in enumerate(self.Species):
            x_i = self.x[i]
            
            #find the correct species property
            if prop == "rho":
                p_i = species.rho
            elif prop == "k":
                p_i = species.k
            elif prop == "cp":
                p_i = species.cp
            elif prop == "amw":
                p_i = species.amw

            p_avg += p_i*x_i

        return p_avg

    def updateMassMeanValues(self):
        '''a function to update all mix 
        mean phys. properties'''

        for prop in self.props_list:
            if prop == "rho":
                self.rho = self.getMassMeanValue("rho")
            elif prop == "k":
                self.k = self.getMassMeanValue("k")
            elif prop == "cp":
                self.cp = self.getMassMeanValue("cp")
            elif prop == "amw":
                self.amw = self.getMassMeanValue("amw")

    def addSpecies(self,new_species,x_new):
        ''' add a new species and update mix properties'''

        self.Species.append(new_species)
        self.updateMassFractions(x_new)
        self.updateMassMeanValues()


    def updateMassFractions(self,x_new):
        '''add new mass fraction and renormalise the mass fraction array'''
        
        self.x = self.x*(1.0 - x_new)
        self.x = np.append(self.x, np.array([x_new]))

        
    def dispProperties(self):
        
        for item in vars(self):
            spec_names = []
            if item == "Species":
                for spec in vars(self)[item]:
                    spec_names.append(spec.name)
                print "Species(names) = ", spec_names
                    
            print item, " = ", vars(self)[item]
    
                
                
