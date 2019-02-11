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

if len(sys.argv) != 4:
    print "Usage: Cursor03.py <FeatureClass>"
    sys.exit()
prov = sys.argv[3]
fc = sys.argv[1]
provList = ["NS","NF","PEI","ON","NB","QC","MB","SK","AB","BC","NT","YT","NU"]

if prov.upper() not in provList:
    sys.exit()
import arcpy
if not arcpy.Exists(fc):
    sys.exit()

scriptFolder = os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptFolder)

start=timeit.default_timer()
exp = """"PROV"LIKE '{}'""".format(prov.upper())

def getAlberta():
    fields = ["Name", "PROV"]
    rows = arcpy.da.SearchCursor(fc,fields, exp)
    count = 0
    print "Name, Prov"
    for row in rows:
        count += 1
        print u"{},{}".format(row[0], row[1])
    print "There are {} cities in the above list".format(count)
    del rows
    del row
getAlberta()


stop=timeit.default_timer()
seconds=stop-start
print "Seconds to execute:",seconds



