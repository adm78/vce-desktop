#!/usr/bin/python
'''This is just a test script to test the existing classes. More
rigorus numerical testing will be implemented in the future.'''

from species import Species
from mixture import Mixture

#create some test species
water = Species("water","H2O",1000.0, 0.58, 
                4182.0, 4182.0, 1.002e-03, 
                18.0, 273.0, 373.0)
ethanol = Species("ethanol","C2H5OH",789.0, 0.171, 
                  2439.9, 2439.9, 1.095e-03, 
                  46.068, 159, 351.37)

#create an empty mixture object and add species one at a time
my_mixture = Mixture()
my_mixture.addSpecies(water, 1.0)
my_mixture.addSpecies(ethanol, 0.05)

my_mixture.dispProperties()

