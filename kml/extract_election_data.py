#!/usr/bin/env python
#
# extract_election_data.py
#


filename = "election_data_2016.txt"


print("let election_data_2016 = {")

with open(filename) as f:
    f.readline()
    for line in f:
       state, clinton, trump = line.strip().split(',')
       print("    \'" + state + "\' : [" + clinton + "," + trump + "],")

print("};")

