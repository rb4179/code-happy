#!/usr/bin/python
#********* WRITTEN BY RB4179 ***
import sys
#********* VARIABLES ***********
oldKey = None
find_big = []
#********* MAIN LOOP ***********
#for line in open("mappertest1", "r"):
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # BAD DATA! Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    find_big.append(float(thisSale))
    if oldKey and oldKey != thisKey:
        find_big.pop()
        print oldKey, "\t", max(map(float,find_big))
        oldKey = thisKey;
        find_big = []

    oldKey = thisKey

if oldKey != None:
    print oldKey, "\t", max(find_big)
