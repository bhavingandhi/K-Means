import pandas as pd
import numpy as np
import numpy.linalg as linalg
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D

mypath = os.getcwd()
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) and f.endswith(".csv") and f.startswith("num") ]

for idx,fname in enumerate(onlyfiles):
	idx = idx +1 
# read file

	df = pd.read_csv(fname)
	df = df.drop(['Cluster Identifier', 'totaltime'], axis=1)	

#covariance matrix
	a =df.corr() 
	a= a.as_matrix(columns = None)

# get eigenVectors
	eigenValues, eigenVectors = linalg.eig(a)

# sort eigenvectors and eigenvalues 

	idx = eigenValues.argsort()   
	eigenvalues = eigenValues[idx]
	eigenvectors = eigenVectors[:,idx]

# Use leading eigenvectors to lower dimensionality of the system

	c= c.as_matrix(columns=None)

	x = c[:,9]
	y = c[:,10]
	z = c[:,11]

	data= np.vstack((x,y,z))

	# File for analysis with R scripts
	np.savetxt("foo.csv", data.transpose(),delimiter=",")
	#Kmeans calculations

	k_means = KMeans(init='k-means++' , n_clusters=2 , n_init=10)

	k_means.fit(data.transpose())
	colors = ['r', 'b', 'g']
	#fig = plt.figure(2)
	#ax = fig.add_subplot(111, projection='3d')
	#ax.scatter(data.transpose()[:, 0], data.transpose()[:, 1], data.transpose()[:, 2],  c = cnot)
	
	new = pd.read_csv('new-' + str(idx)  '.csv')
	new['cl_id'] =  k_means_labels
	new.to_csv('cl-num-' + str(idx) '.csv',index=False)



