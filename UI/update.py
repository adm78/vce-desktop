#!/usr/bin/python

'''This script can bed used to update GUI .py and .pyr files after
editing the .ui files and .qrc files (resource files) on Qt
Designer. Any new ui widgets require a line to be added in this file''' 

import subprocess
import os

#update the main window .py
subprocess.call(["pyuic", "vceMainWindowGUI.ui", ">", "vceMainWindowGUI.py"], shell=True)

#updating the GUI resource file
subprocess.call(["pyrcc4", "./GUIresources/GUIresources.qrc", ">", "GUIresources_rc.py"], shell=True)
