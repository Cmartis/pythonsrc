__author__='mike_bowles'

import urllib.request
import sys

#read data from uci data repository
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urllib.request.urlopen(target_url)

#arranged data into list for labels and list of lists for attributes
xList = []
labels = []

for line in data:
    #split on comma
    row = str(line).strip().split(",")
    xList.append(row)
nrow = len(xList)
ncol = len(xList[1])

type = [0]*3
colCounts = []


for col in range(ncol):
    for row in xList:
        try:
            a = float(row[col])
            if isinstance(a, float):
                type[0] += 1
        except ValueError:
            if len(row[col]) > 0 :
                type[1] += 1
            else:
                type[2] += 1
    colCounts.append(type)
    type = [0]*3
sys.stdout.write("Col#" + '\t' + "Number" + '\t' +
                     "Strings" + '\t ' + "Others\n")
iCol = 0
for types in colCounts:
    sys.stdout.write(str(iCol)+ '\t\t' + str(types[0]) + '\t\t' +
                            str(types[1]) + '\t\t' + str(types[2]) + "\n")
    iCol += 1            
    
#sys.stdout.write("number of rows of data = " + str(len(xList)) + '\n')
#sys.stdout.write("number of colums of data = " + str(len(xList[1])))


