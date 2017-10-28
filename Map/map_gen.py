import math
from opensimplex import OpenSimplex

gen = OpenSimplex()

def noise(nx, ny, freq, octave, power):
    sum_ = 0
    if octave == 0:
        octave = 1
    #for x in range(1, octave):
    #    sum_ += (1/x)*gen.noise2d(freq*nx*(x**2), freq*ny*(x**2)) / 2.0 + 0.5
    for x in range(1, octave):
        sum_ += (1/float(x))*(gen.noise2d(freq*nx*(2**x), freq*ny*(2**x)) /2.0 +0.5)
    #sum_ = gen.noise2d(freq*nx, freq*ny) + 0.5*gen.noise2d(2*freq*nx, 2*freq*ny) + 0.25*gen.noise2d(4*freq*nx, 4*freq*nx)#/ 2.0 + 0.5
    return (sum_)**power

def convert_to_terrain(num, blocks):
    for n in range(1, blocks+1):
        if num < (float(n)/blocks):
            return n
        elif num > 1:
            return 1


def wanking_cunt(x_width, y_height, freq, octaves, power, features):
    total = []
    for y in range(0,y_height):
        for x in range(0,x_width):
            nx = float(x)/float(x_width) - 0.5
            ny = float(y)/float(y_height) - 0.5
            z = 0
            z = noise(nx, ny, freq, octaves, power)
            terrain =  convert_to_terrain(z, features)
            total.append([(x, y), terrain])

    return total
