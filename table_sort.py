outputDict = {}
sortedList = []
inputFile = open("./input.txt", "r")
# read lines in input and add entries to a dictionary with integers as keys and chars as values
for line in inputFile:
    line = line.split()
    outputDict[int(line[1])] = line[0]
# get dictionary keys (integers in input file)     
for key in outputDict.keys():
    sortedList.append(key)
# sort keys in ascending order
sortedList.sort()
# generate output 
outputFile = open("./output.txt", "w")
for entry in sortedList:
    outputFile.write(outputDict[entry] + " " + str(entry) + "\n")

