#!/usr/bin/python

'''Preliminary test of the flash class methods'''
from unitop import FlashTank
import numpy as np
from component import Component

#binary system
Methanol = Component("methanol")
Water = Component("water")
mole_fracs = np.array([0.6,0.4])
bin_test = FlashTank(temperature=363.0,pressure=1.0e04,components=[Methanol,Water],mole_fracs=mole_fracs)
bin_test.getVLEConst()
bin_test.binary_flash()

#tertiary system
#based on: www.nt.ntnu.no/users/skoge/bok/mer/flash_english_edition_2009 p6
#solution: x = [0.3394087   0.36505606  0.29553524]
#          y = [0.57190365  0.2708716   0.15722475]
#          beta = 0.6915
tert_test = FlashTank(temperature=390.0,pressure=5.0e05,components=["dummy_comp1","dummy_comp2","dummy_comp3"],mole_fracs=np.array([0.5,0.3,0.2]))
tert_test.vle = np.array([1.685, 0.742, 0.532])
tert_test.rach_rice()
