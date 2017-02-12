__author__='mike_bowles'

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

#read data from uci data repository
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#data = urllib.request.urlopen(target_url)

#arrange data into list for labels and list of lists for attributes
#xList = []
#labels = []

#read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

#print head and tail of data frame
print(rocksVMines.head())
print(rocksVMines.tail())

#print summary of data frame
summary = rocksVMines.describe()
print(summary)

