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


if len(sys.argv) != 2:
    print "Usage: Cursor03.py <FeatureClass>"
    sys.exit()

fc = sys.argv[1]

if not os.path.exists(fc):
            print fc, "does not exist."
            sys.exit()

scriptFolder = os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptFolder)



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

