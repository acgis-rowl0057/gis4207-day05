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

import arcpy
import os
import sys

scriptFolder = os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptFolder)

fc = r"..\..\..\Data\Canada\Can_Mjr_Cities.shp"

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

