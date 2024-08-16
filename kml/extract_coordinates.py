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

places = []

for placemark in root.Document.Folder.Placemark:
    #print(place.name)
    data_raw = {item.get("name"):item.text for item in
                placemark.ExtendedData.SchemaData.SimpleData}


    # hack: Alaska has Placemark/MultiGeometry/Polygon
    if "MultiGeometry" in dir(placemark):
        coords = placemark.MultiGeometry.Polygon.outerBoundaryIs[-1].LinearRing.coordinates.text.strip()
    else:
        coords = placemark.Polygon.outerBoundaryIs[-1].LinearRing.coordinates.text.strip()


    data = { 
        "name" : data_raw["NAME"], 
        "coordinates" : coords
    }
    #print(data)

    places.append(data)



def vector_str_to_list(s):
    tokens = s.split(',')
    result = [float(token) for token in tokens]
    return result



print("let state_data = {")


for place in places:
    print("     \'" + place['name'] + "\' : ", end='')
    points_text = place['coordinates'].split()
    points_ints = [vector_str_to_list(s) for s in points_text]
    print(points_ints, ',')


print("};")


