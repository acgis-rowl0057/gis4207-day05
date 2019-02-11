#-------------------------------------------------------------------------------
# Name:        Cursor03.py
# Purpose:
#
# Author:      Matthew Rowland
#
# Created:     05-02-2019
# Copyright:   (c) Rowland 2019
#-------------------------------------------------------------------------------


import os
import sys
import timeit
import arcpy


fc = r"..\..\..\Data\Canada\Can_Mjr_Cities.shp"




scriptFolder = os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptFolder)

start=timeit.default_timer()

def getAlberta():
    rows = arcpy.SearchCursor(fc,""""PROV"='AB'""","","NAME; PROV")
    count = 0
    currentState = ""
    print "Name, Prov"
    for row in rows:
        if currentState != row.PROV:
            currentState = row.PROV
            count += 1
        print u"{},{}".format(row.NAME, row.PROV.upper())
    print "There are {} cities in the above list".format(count)
    del rows
    del row
getAlberta()


stop=timeit.default_timer()
seconds=stop-start
print "Seconds to execute:",seconds



