#!/usr/bin/python

'''This script is used to test the methods within the thermo modules
that are called directly from the unit operations level'''

from thermo import *

print "IdealGasPressure(n=20,T=298.15,V=1) = ",IdealGasPressure(n=20,T=298.15,V=1)
print  "IdealGasPressure(n=20,T=298.15,V=1, unit=True) = ",IdealGasPressure(n=20,T=298.15,V=1,unit=True)
print "IdealGasPressure(molar_conc=100,T=332.0) = ",IdealGasPressure(molar_conc=100,T=332.0)
print "IdealGasPressure(molar_mass=100,amw=32.0) = ",IdealGasPressure(molar_conc=100,amw=32.0)

print "IdealGasVolume(n=40.8969,T=298.15) = ",IdealGasVolume(n=40.8969,T=298.15)

print "IdealGasTemperature(n=40.8969,V=1,P=2e5,unit=True) = ",IdealGasTemperature(n=40.8969,V=1,P=2e5,unit=True)

print "IdealGasConc(P=101325.0,T=298.15,unit=True) = ",IdealGasConc(P=101325.0,T=298.15,unit=True)
