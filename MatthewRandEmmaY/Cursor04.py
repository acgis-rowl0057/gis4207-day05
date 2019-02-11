#-------------------------------------------------------------------------------
# Name:        Cursor04.py
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

## where clause   """"PROV"='QC'"""
def getLatLong():
    fields = ['NAME', 'PROV', 'SHAPE@X', 'SHAPE@Y']
    count = 0
    dscCS = arcpy.Describe(fc).spatialReference
    print("Coordinate System:      " + dscCS.Name)
    print  "Name, Province, Longitude, Latitude"
    for row in arcpy.da.SearchCursor(
        fc, fields):
        count += 1
        print(u'{0}, {1}, {2}, {3}'.format(row[0], row[1], row[2], row[3]))
    print "There are {} cities in the above list".format(count)
    del row

getLatLong()

stop=timeit.default_timer()
seconds=stop-start

print "Seconds to execute:",seconds





