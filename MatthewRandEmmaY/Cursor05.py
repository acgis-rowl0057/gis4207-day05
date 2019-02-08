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

import arcpy
import os
import sys

def main():
    fc = r"..\..\..\Data\Canada\Can_Mjr_Cities.shp"

    fields = ['NAME', 'PROV', 'SHAPE@X', 'SHAPE@Y','UTM_MAP']
    count = 0
    dscCS = arcpy.Describe(fc).spatialReference
    print("Coordinate System:      " + dscCS.Name)
    print  "Name, Province, Longitude, Latitude, UTM"
    print getHeader()
    for row in arcpy.da.SearchCursor(fc, fields):
        count += 1
        print getBody(row)
        #print(u'{0}, {1}, {2}, {3}, {4}'.format(row[0], row[1], row[2], row[3], row[4]))
    print "There are {} cities in the above list".format(count)


def getHeader():
    print """<?xml version="1.0" encoding="UTF-8"?>"""
    print """<kml xmlns="http://www.opengis.net/kml/2.2">"""


def getBody(row):
    kml = " <Placemark>"
    kml += u"     <name>{}, {}</name>".format(row[0], row[1])
    kml += u"     <description>http://www.canmaps.com/topo/nts50/map/{}.htm</description>".format(row[4])
    kml += "     <Point>"
    kml += u"         <coordinates>{},{}</coordinates>".format(row[2],row[3])
    kml += "     </Point>"
    kml += " </Placemark>"
    kml +="</kml>"
    return kml

if __name__ == "__main__":
    main()
