#!/usr/bin/python

'''This script can bed used to update GUI .py and .pyr files after
editing the .ui files and .qrc files (resource files) on Qt
Designer. Any new ui widgets require a line to be added in this file''' 

import subprocess 
import os
from utils import which, isWindows
import sys

#update the main window .py

#checking for the correct executables 
pyuic_exec = "pyuic"
pyuic4_exec = "pyuic4"
if isWindows():
    pyuic_exec += ".exe"
    pyuic4_exec += ".exe"

if which(pyuic_exec) != None:
    pyuic_cmd = "pyuic vceMainWindowGUI.ui > vceMainWindowGUI.py"
    
elif which(pyuic4_exec) != None:
    pyuic_cmd = "pyuic4 vceMainWindowGUI.ui > vceMainWindowGUI.py"
else:
    print "update.py Error: neither pyuic or pyuic4 could not be found."
    print "Try installing pyqt4-dev-tools or adding pyuic to your"
    print "path and re-running."
    sys.exit()

pyuic_process = subprocess.Popen(pyuic_cmd,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 shell=True)

out, err = pyuic_process.communicate()
errorcode = pyuic_process.returncode
if errorcode != 0:
    print "stdout:", out
    print "stderr:", err
    print "exit code:", errorcode
    
#updating the GUI resource file
if which("pyrcc4") != None:
    pyrcc_cmd = "pyrcc4 " + os.path.join("GUIresources","GUIresources.qrc") + " > GUIresources_rc.py"
    pyrcc4_process = subprocess.Popen(pyrcc_cmd,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     shell=True)
else:
    print "update.py Error: pyrcc4 could not be found."
    print "Try installing pyqt4-dev-tools or adding pyrcc4 to your"
    print "path and re-running."   
    sys.exit()

out, err = pyrcc4_process.communicate()
errorcode = pyrcc4_process.returncode
if errorcode != 0:
    print "stdout:", out
    print "stderr:", err
    print "exit code:", errorcode
