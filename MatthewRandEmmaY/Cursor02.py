#-------------------------------------------------------------------------------
# Name:        Cursor02.py
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

if len(sys.argv) != 4:
    print "Usage: Cursor02.py <FeatureClass>"
    sys.exit()

fc = sys.argv[1]

import arcpy
if not arcpy.Exists(fc):
    sys.exit()

scriptFolder = os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptFolder)

start=timeit.default_timer()
##fc = r"..\..\..\Data\Canada\Can_Mjr_Cities.shp"

def getDaCityProv():
    print "City, Prov"
    fields = ['NAME', 'PROV']
    count = 0
    # Use ORDER BY sql clause to sort field values
    for row in arcpy.da.SearchCursor(
        fc, fields):
        count += 1
        print(u'{0}, {1}'.format(row[0], row[1]))
    print "There are {} cities in the above list".format(count)
    del row

getDaCityProv()

stop=timeit.default_timer()
seconds=stop-start
print "Seconds to execute:",seconds

