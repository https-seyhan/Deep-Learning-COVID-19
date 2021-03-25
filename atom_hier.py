import pandas as pd
import numpy as np
import seaborn as sb
from matplotlib import  pyplot as plt
from sklearn.cluster import KMeans
import os
import sys

print(sys.version)

os.chdir('/home/saul/protein')


heatdata = pd.read_csv('alldata_freq.csv', sep = ',')


def shapeData():
	print("Shapes ")

	#atoms
	atomsAve = pd.pivot_table(heatdata, values='freq', index= ['Atom'], aggfunc = np.average )
	#print("Atom Shape ", atomsAve.head())
	atomsMedian = pd.pivot_table(heatdata, values='freq', index= ['Atom'], aggfunc = np.median)
	#print("Atom Shape ", atomsMedian.head())
	atoms = pd.merge(atomsAve, atomsMedian, how = "inner", on = ['Atom'])
	#atoms = pd.DataFrame(atoms, columns=['Average', 'Median'])
	atoms = atoms.rename(columns={'freq_x':'Average', 'freq_y':'Median'})

	#print(atoms.head())
	#print(atoms.columns)
	#print(atoms['Average'])

	kmeanClusters(atoms)

def kmeanClusters(atoms):
	print("Clusters called ")

	averageVals = atoms.iloc[:, 0:1]
	print("Avera Variable ",averageVals.head())

	#cluster
	kmeans = KMeans(7)
	print(kmeans)
	kmeans.fit(averageVals)

	identified_clusters = kmeans.fit_predict(averageVals)
	print(identified_clusters)

	#add clusters to the dataset
	atomClusters = atoms.copy()
	atomClusters['Clusters'] = identified_clusters

	atomClusters.reset_index(level=0, inplace=True) #reset index

	print(atomClusters.head())
	print(atomClusters.columns)

	#plot data points
	#plt.hist(atomClusters['Average'], color= atomClusters['Clusters'] )
	sb.catplot(x="Atom", y="Average", hue="Clusters", kind="swarm", data=atomClusters);
	
	plt.show()


if __name__ == '__main__':
	shapeData()
