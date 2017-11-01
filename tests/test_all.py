#!/usr/bin/python

'''This script runs the all the regression tests in sequence to ensure
that recent changes have not broken any part of the code-base. By
default all test_* scripts are run. Tests are run in order from base
classes all the way to the top of the class hierarchy. The results of the test are output to the regression_log.txt.

THIS SCRIPT SHOULD BE RUN AND PASS BEFORE ANY PUSH IS MADE TO THE
MASTER OR DEVELOP BRANCH!

'''
import subprocess 
import os
from utils import which, isWindows
import sys

#list of test scripts to be run
test_scripts = ['test_thermo.py',
                'test_component.py',
                'test_stream.py',
                'test_flash.py']
                


#start running the scripts in order
print "starting full regression test..."

for script in test_scripts:
    print "------------------------------------"
    print "running", script
    vce_process = subprocess.Popen(("python " + script),
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 shell=True)

    out, err = vce_process.communicate()
    errorcode =  vce_process.returncode
    if errorcode != 0:
        print "********************************"
        print "error: regression test failure!!"
        print "********************************"
        print "script:", script
        print "stdout:", out
        print "stderr:", err
        print "exit code:", errorcode
        sys.exit()
    else:
        print script, "exited without errors."
        print "stdout:", out
        print "stderr:", err
        print "exit code:", errorcode

print "=================================="
print "regression test successful!"
print "all scripts executed without error."
print "=================================="
