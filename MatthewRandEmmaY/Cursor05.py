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
import os.path


output = r"D:\Semester2\gis4207_Customization_I\day05\Output"
if not os.path.exists(output):
    os.makedirs(output)


def main():
    fc = r"..\..\..\Data\Canada\Can_Mjr_Cities.shp"
    fields = ['NAME', 'PROV', 'SHAPE@X', 'SHAPE@Y','UTM_MAP']
    getHeader()
    for row in arcpy.da.SearchCursor(fc, fields):
        print getBody(row)
    print "<Document>"
    print "<KML>"


def getHeader():
    print """<?xml version="1.0" encoding="UTF-8"?>"""
    print """<kml xmlns="http://www.opengis.net/kml/2.2">"""
    print "<Document>"


def getBody(row):
    kml = " <Placemark>"
    kml += u"     <name>{}, {}</name>".format(row[0], row[1])
    kml += u"     <description>http://www.canmaps.com/topo/nts50/map/{}.htm</description>".format(row[4])
    kml += "     <Point>"
    kml += u"         <coordinates>{},{}</coordinates>".format(row[2],row[3])
    kml += "     </Point>"
    kml += " </Placemark>"
##    kml +="</kml>"
    return kml


#write to kml file
##savePath = output
##fileName = "Cities"
##completName = os.path.join(savePath,fileName+".kml")
##file1 = open(completName,"w")
##file1.write(kml)
##file1.close()

if __name__ == "__main__":
    main()
