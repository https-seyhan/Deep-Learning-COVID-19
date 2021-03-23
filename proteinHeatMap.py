import pandas as pd
import numpy as np
import seaborn as sb
import os
import sys
from matplotlib import  pyplot as plt

print(sys.version)
os.chdir('/home/saul/protein')

heatdata = pd.read_csv('alldata_freq.csv', sep = ',')
#heatdata = heatdata.pivot("Atom", "freq", "protein_name")
pivotdata = pd.pivot_table(heatdata, values='freq', index = ['Atom'], columns=['protein_name'], aggfunc=np.sum)

#print(heatdata.describe())
#print(heatdata.head())

def plotHeadMap():
	print("Head Map")
	fig, ax = plt.subplots(figsize=(20,7)) 
	#print(heatdata.describe())
	#print(heatdata.head())
	print(type(heatdata['freq']))
	heatdata['freq'] = pd.to_numeric(heatdata['freq'],  downcast='signed')
	sb.heatmap(pivotdata, annot=True, linewidths=.7, fmt='g', cmap='tab10', ax=ax)
	plt.show()

def plotBoxPlot():
	heatdata.describe()
	ax = sb.boxplot(x= heatdata['freq'])
	plt.show()

def testWork():
	flights = sb.load_dataset("flights")
	print(flights)
	flights = flights.pivot("month", "year", "passengers")
	print(flights)
	#ax = sb.heatmap(flights, annot=True, fmt="d")
	#plt.show()

if __name__ == '__main__':

	plotHeadMap()
	#plotBoxPlot()
	#testWork()
