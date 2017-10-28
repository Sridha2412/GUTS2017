import math
from opensimplex import OpenSimplex

gen = OpenSimplex()

def noise(nx, ny, freq, octave, power):
    return (gen.noise2d(freq*nx, freq*ny) / 2.0 + 0.5)**power

def convert_to_terrain(num, blocks):
    for n in range(1, blocks):
        if num < (float(n)/blocks):
            return n

def wanking_cunt(x_width, y_height, freq, octaves, power, features):
    total = []
    for y in range(0,y_height):
        for x in range(0,x_width):
            nx = float(x)/float(x_width) - 0.5
            ny = float(y)/float(y_height) - 0.5
            z = 0
            z = noise(nx, ny, freq, octaves, power)
            total.append([(x, y), convert_to_terrain(z, features)])

    return total
