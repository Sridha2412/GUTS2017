import pygame, os, random
from opensimplex import OpenSimplex

class Map(object):

    def __init__(self, screen, hardness, type, speed, mapping, gen):

        pygame.sprite.Sprite.__init__(self)

        self.hardness = 0
        self.type = {"GRASS":1, "GRAVEL":2, "CONCRETE":3}
        self.speed = 0
        self.mapping = []
        self.gen = OpenSimplex()

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
