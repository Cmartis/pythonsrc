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
    print(xList[i])
    
sys.stdout.write("number of rows of data = " + str(len(xList)) + '\n')
sys.stdout.write("number of colums of data = " + str(len(xList[1])))


