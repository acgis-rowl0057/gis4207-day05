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

if len(sys.argv) != 2:
    print "Usage: Cursor03.py <FeatureClass>"
    sys.exit()

fc = sys.argv[1]

import arcpy

if not os.path.exists(fc):
    print fc, "does not exist."
    sys.exit()

scriptFolder = os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptFolder)

start=timeit.default_timer()

## where clause   """"PROV"='QC'"""

fields = ['NAME', 'PROV', 'SHAPE@X', 'SHAPE@Y']
count = 0
dscCS = arcpy.Describe(fc).spatialReference
print("Coordinate System:      " + dscCS.Name)
print  "Name, Province, Longitude, Latitude"
for row in arcpy.da.SearchCursor(
    fc, fields):
    count += 1
    print(u'{0}, {1}, {2}, {3}'.format(row[0], row[1], row[2], row[3]))

stop=timeit.default_timer()
seconds=stop-start
print "There are {} cities in the above list".format(count)
print "Seconds to execute:",seconds

del row



