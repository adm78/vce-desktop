#!/usr/bin/python

'''This module contains all the wrapper code to simulate a flash tank
using the cantera sublayer'''

import cantera as ct
from __future__ import print_function


class FlashTank(object):

    def __init__(self,name):

        '''set up an instancde of the flash tank object'''

        self.name = name




def run_flash_test():

    ''' this acts as a callable test for a complete flash system '''

    print("Initiating test flash tank...")

    test_FT = FlashTank("test_FT")
    



    
