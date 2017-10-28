import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import csv

# Load data from CSV
temp = []
with open('test.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        temp = row
X_dat = []
Y_dat = []
Z_dat = []
for x in temp:
	x = x[1:-1]
	x = x.split(', ')
	print(x)
	print(x[0], x[1], x[2])
	X_dat.append(float(x[0]))
	Y_dat.append(float(x[1]))
	Z_dat.append(float(x[2]))

# Convert from pandas dataframes to numpy arrays
X, Y, Z, = np.array([]), np.array([]), np.array([])
print len(X_dat), len(Y_dat), len(Z_dat)
for i in range(0,len(X_dat)):
	X = np.append(X,X_dat[i])
	Y = np.append(Y,Y_dat[i])
	Z = np.append(Z,Z_dat[i])
print "Done"


print X[0], Y[0]
print len(X), len(Y)
# Create the contour plot
CS = plt.plot(X, Y, Z, 15)
plt.colorbar()
plt.show()
