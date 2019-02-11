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

scriptFolder = os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptFolder)

fc = r"..\..\..\Data\Canada\Can_Mjr_Cities.shp"
start=timeit.default_timer()

def cityProvince():
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

cityProvince()

stop=timeit.default_timer()
seconds=stop-start
print "Seconds to execute:",seconds


