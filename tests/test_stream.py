#!/usr/bin/python

'''This script is used to test the stream class'''

from component import Component
from stream import Stream
import numpy as np


#Make some components to add to the stream
test_components = [Component("water"), Component("methanol")]
test_mole_fracs = np.array([0.4,0.6])
test_state = "liquid"

#Make a stream object
TestStream = Stream(test_components,
                    mole_fracs=test_mole_fracs,
                    state=test_state)

#Get the heat capacity of the stream
print "TestStream.Cp = ", TestStream.Cp(), TestStream.CpUnit()
print "TestStream.Pvap = ", TestStream.Pvap(), TestStream.PvapUnit()
print "TestStream.rho = ", TestStream.rho(), TestStream.rhoUnit()
