#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rowla
#
# Created:     05-02-2019
# Copyright:   (c) rowla 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------

import arcpy
import os
import sys

scriptFolder = os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptFolder)

fc = r"..\..\..\Data\Canada\Can_Mjr_Cities.shp"
fields = ['NAME', 'PROV']
count = 0
# Use ORDER BY sql clause to sort field values
for row in arcpy.da.SearchCursor(
    fc, fields):
    count += 1
    print(u'{0}, {1}'.format(row[0], row[1]))


print "There are {} cities in the above list".format(count)


del row
