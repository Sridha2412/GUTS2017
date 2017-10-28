import noise, math, random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy
import csv


height = 8
width = 8




from opensimplex import OpenSimplex
gen = OpenSimplex()




final = []

def noise(nx, ny):
    # Rescale from -1.0:+1.0 to 0.0:1.0
    return gen.noise2d(nx, ny) / 2.0 + 0.5

for y in range(0,height-1):
    print y
    for x in range(0,width):
        nx = float(x)/float(width) - 0.5
        ny = float(y)/float(height) - 0.5
        z = 0
#        for step in range(1, 5):
#            z += (1/step)*noise((2**step)*nx, (2**step)*ny)
        z = noise(nx, ny)
#        z = math.exp(z)
        final.append([x, y, z])

print(len(final))

for y in range(width**2):
    if y%width==0:
        print
    try:
        print (final[y][0], final[y][1]),round(final[y][2]*10, 3),
    except:
        pass


with open("test.dat", 'wb') as myfile:
    for x in final:
        myfile.write("%f %f %f\n" %(x[0], x[1], x[2]))
