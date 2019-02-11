#-------------------------------------------------------------------------------
# Name:        Cursor06.py
# Purpose:
#
# Author:      Matthew Rowland
#
# Created:     05-02-2019
# Copyright:   (c) Rowland 2019
#-------------------------------------------------------------------------------


import os
import sys
import os.path
import zipfile

if len(sys.argv) != 4:
    print "Usage: Cursor03.py <FeatureClass>"
    sys.exit()

fc = sys.argv[1]
fz = sys.argv[2]

import arcpy
if not arcpy.Exists(fc):
    sys.exit()

scriptFolder = os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptFolder)

#create ouput folder
output = r"D:\Semester2\gis4207_Customization_I\day05\Output"
if not os.path.exists(output):
    os.makedirs(output)


def main():
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
    header = """<?xml version="1.0" encoding="UTF-8"?>
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
    footer = """</Document> </kml>"""
    return footer


# compression Cities.kml to Cities.kmz using the Zipfile module
def zipIt():
    kmlZip = zipfile.ZipFile(fz, 'w', zipfile.ZIP_DEFLATED)
    kmlZip.write('D:\Semester2\gis4207_Customization_I\day05\Output\Cities.kml')
    kmlZip.close()
zipIt()

if __name__ == "__main__":
    main()
