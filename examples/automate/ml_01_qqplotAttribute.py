__author__='mike_bowles'

import urllib.request
import sys
import numpy as np
import scipy.stats as stats
import pylab

#read data from uci data repository
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urllib.request.urlopen(target_url)

#arrange data into list for labels and list of lists for attributes
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


#generate summary statistcs for column 3 (e.g.)
col = 3
colData = []
for row in xList:
        colData.append(float(row[col]))

stats.probplot(colData, dist="norm", plot=pylab)
pylab.show()

#sys.stdout.write("number of rows of data = " + str(len(xList)) + '\n')
#sys.stdout.write("number of colums of data = " + str(len(xList[1])))


