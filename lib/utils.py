#!/usr/bin/python

'''The model serves as a storage are for general system utlities that
are useful across the code-base'''
import os
import glob

def getVCEPath():

    #returns the full path of the vce-desktop diectory.
    # Should work cross platform!

    cwd =  os.path.abspath(os.getcwd())
    
    #keep cutting the end of the path off until
    #we find the vce-desktop directory
    head, tail = os.path.split(cwd)
    while tail != "vce-desktop":
        head, tail = os.path.split(head)

    vce_path = os.path.join(head, tail)
     
    return vce_path


def getVCEPropertiesPath():

    #returns the path of the properties database
    return os.path.join(getVCEPath(),'properties')

def which(program):
    
    ''' Cross platform functional to check if an executable exists
    http://stackoverflow.com/questions/
    377017/test-if-executable-exists-in-python'''
    
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None
