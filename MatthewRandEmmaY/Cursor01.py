#-------------------------------------------------------------------------------
# Name:        Cursor01.py
# Purpose:
#
# Author:      Matthew Rowland
#
# Created:     05-02-2019
# Copyright:   (c) Rowland 2019
#-------------------------------------------------------------------------------

import arcpy
import os
import sys
import timeit

if len(sys.argv) != 3:
    print "Usage: Cursor01.py <FeatureClass>"
    sys.exit()

fc = sys.argv[1]

scriptFolder = os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptFolder)

start=timeit.default_timer()


def getCityProvince():
    rows = arcpy.SearchCursor(fc,"","", "NAME; PROV", "PROV D")
    count = 0
    currentState = ""
    print "Name, Prov"
    for row in rows:
        if currentState != row.PROV:
            currentState = row.PROV
        count += 1
        print u"{},{}".format(row.NAME, row.PROV)
    print "There are {} cities in the above list".format(count)
    del rows
    del row

getCityProvince()

stop=timeit.default_timer()
seconds=stop-start
print "Seconds to execute:",seconds


