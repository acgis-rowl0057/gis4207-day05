#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rowla
#
# Created:     09-02-2019
# Copyright:   (c) rowla 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
import os
import sys
import os.path
import zipfile

#create ouput folder
output = r"D:\Semester2\gis4207_Customization_I\day05\Output"
if not os.path.exists(output):
    os.makedirs(output)


def main():
    fc = r"..\..\..\Data\Canada\Can_Mjr_Cities.shp"
    fields = ['NAME', 'PROV', 'SHAPE@X', 'SHAPE@Y','UTM_MAP']

    #create kml file, open and write header
    savePath = output
    fileName = "Cities"
    completName = os.path.join(savePath,fileName + ".kml")
    file1 = open(completName,"w")
    file1.write(getHeader())


    # iterate and write body
    for row in arcpy.da.SearchCursor(fc, fields):
        file1.write (getBody(row))

    # write body
    file1.write(getFooter())

    #close file
    file1.close()

def getHeader():
    header= """<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2">
    <Document>"""
    return header


def getBody(row):
    kml = """ <Placemark>
        <name>{0}, {1}</name>
         <description>http://www.canmaps.com/topo/nts50/map/{2}.htm</description>
       <Point>
            <coordinates>{3},{4}</coordinates>
         </Point>
     </Placemark>"""
    return kml.format(row[0].encode('utf-8'),row[1],row[4],row[2],row[3])

def getFooter():
    footer= """</Document> </kml>"""
    return footer


# zip Cities.kml to Cities.kmz
fileLocation = r"D:\Semester2\gis4207_Customization_I\day05\Output\Cities.kmz"
kmlZip = zipfile.ZipFile(fileLocation, 'w')
kmlZip.write('D:\Semester2\gis4207_Customization_I\day05\Output\Cities.kml')
kmlZip.close()

if __name__ == "__main__":
    main()
