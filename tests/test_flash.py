#!/usr/bin/python

'''Preliminary test of the flash class methods'''
from unitop import FlashTank
import numpy as np
from component import Component



#binary system
print "--------------------------------------------------"
print "starting methanol-water binary flash test..."
Methanol = Component("methanol")
Water = Component("water")
mole_fracs = np.array([0.6,0.4])
bin_test = FlashTank(temperature=333.0,pressure=5e04,components=[Methanol,Water],
                     mole_fracs=mole_fracs, debug=True)
bin_test.getVLEConst()
bin_test.rach_rice()
print "methanol-water binary flash test complete!"


#tertiary system
#based on: www.nt.ntnu.no/users/skoge/bok/mer/flash_english_edition_2009 p6
#solution: x = [0.3394087   0.36505606  0.29553524]
#          y = [0.57190365  0.2708716   0.15722475]
#          beta = 0.6915
print "--------------------------------------------------"
print "starting hydrocarbon multi-component flash test..."
tert_test = FlashTank(temperature=390.0,pressure=5.0e05,components=["dummy_comp1","dummy_comp2","dummy_comp3"],
                      mole_fracs=np.array([0.5,0.3,0.2]), debug=True)
tert_test.vle = np.array([1.685, 0.742, 0.532])
tert_test.rach_rice()
print "hydrocarbon multi-component flash test complete!"
