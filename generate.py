#!/bin/python

import csv
import json

csvfile = open('2018_Gaz_zcta_national.txt', 'r')
jsonfile = open('zipcodes.json', 'w')

fieldnames = ("GEOID", "ALAND", "AWATER", "ALAND_SQMI", "AWATER_SQMI", "INTPTLAT", "INTPTLONG")
reader = csv.DictReader( csvfile, fieldnames, dialect='excel-tab' )

output = {}

for each in reader:
    row = {}
    row['lat'] = each['INTPTLAT'].strip()
    row['lon'] = each['INTPTLONG'].strip()
    if (each['GEOID'].strip().isdigit()):
        output[each['GEOID'].strip()] = row

json.dump(output, jsonfile, indent=2)
