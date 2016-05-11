#!/usr/bin/python

'''This cross-platform script will create/update all the png files in
the bitmap dircetory by converting all the svg files in 'vector'.

Requires ImageMagick to be installed and the installation folder to be
in your path.  '''

import subprocess
import os

# create the bitmap folder if there's not one there already
if not os.path.exists('bitmap'):
    os.makedirs('bitmap')

# convert to svg, trim any whitespace and output to bitmap dir
subprocess.call(["mogrify", "-format", "png", 
                 "-trim", "-path", "./bitmap", "./vector/*.svg"])






