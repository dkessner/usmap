#!/usr/bin/env python
#
# extract_coordinates.py
#


from pykml import parser
import pandas as pd


filename = "cb_2023_us_state_20m.kml"

with open(filename) as f:
    doc = parser.parse(f)

root = doc.getroot()

#print("root.Document.name:", root.Document.name)
#print("root.Document.Folder.name:", root.Document.Folder.name)

#for place in root.Document.Folder.Placemark:
#    print(place.name)

states = []

for placemark in root.Document.Folder.Placemark:
    #print(place.name)
    data_raw = {item.get("name"):item.text for item in
                placemark.ExtendedData.SchemaData.SimpleData}

    #print(data_raw["NAME"])

    if "MultiGeometry" in dir(placemark):
        coords_list = [polygon.outerBoundaryIs.LinearRing.coordinates.text.strip() \
                       for polygon in placemark.MultiGeometry.Polygon]
    else:
        coords_list = [placemark.Polygon.outerBoundaryIs.LinearRing.coordinates.text.strip()]

    state = { 
        "name" : data_raw["NAME"], 
        "coordinates" : coords_list
    }

    states.append(state)



def vector_str_to_list(s):
    tokens = s.split(',')
    result = [float(token) for token in tokens]
    return result


# write Javascript object
#    state_name -> list of polygons
#    polygon = list of points [x,y,z]
#    point = list of 3 numbers
#
# {
# ...
# 'California' : [ [[1,2,0], [3,4,0]], [ ... ] ]
# ...
# }


print("let state_data = {")

for state in states:
    print("     \'" + state['name'] + "\' : ", end='')
    points_list_text = [s.split() for s in state['coordinates']]
    #print(points_list_text)
    points_floats_list = [[vector_str_to_list(s) for s in point_text] for point_text in points_list_text]
    print(points_floats_list, ',')

print("};")


