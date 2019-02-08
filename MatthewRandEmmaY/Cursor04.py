#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rowla
#
# Created:     07-02-2019
# Copyright:   (c) rowla 2019
# Licence:     <your licence>
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

fc = r"..\..\..\Data\Canada\Can_Mjr_Cities.shp"
fields = ['NAME', 'PROV', 'SHAPE@X', 'SHAPE@Y']
count = 0
print "Name, Province, Longitude, Latitude"
# Use ORDER BY sql clause to sort field values
for row in arcpy.da.SearchCursor(
    fc, fields):
    count += 1
    print(u'{0}, {1}, {2}, {3}'.format(row[0], row[1], row[2], row[3]))


print "There are {} cities in the above list".format(count)
stop=timeit.default_timer()
seconds=stop-start
print "Seconds to execute:",seconds

del row

