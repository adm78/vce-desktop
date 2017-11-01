#!/usr/bin/python

from __future__ import print_function
import cantera as ct


'''This module contains all the wrapper code to simulate a test water flash tank
using the cantera sublayer'''


class FlashTank(object):

    def __init__(self,name):

        '''set up an instancde of the flash tank object'''

        self.name = name
        self.feed_water = ct.Water()
        self.feed_water.TX = 400.0, 0.0
        self.feed_resevoir = ct.Reservoir(contents=self.feed_water,name="flash_feed")
        self.liq_vapour_system = ct.Water()
        self.liq_vapour_system.TX = 350.0,0.5
        
        

def run_flash_test():

    ''' this acts as a callable test for a complete flash system '''

    print("Initiating test flash tank...")

    test_FT = FlashTank("test_FT")
    print(test_FT.feed_water.report())
    print(test_FT.liq_vapour_system.report())
    
    


if __name__ == "__main__":

    run_flash_test()
