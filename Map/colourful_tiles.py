import pygame, sys, map_gen, time

pygame.init()
reso_x = 64*16
reso_y = 64*16
divs = reso_x/32

screen = pygame.display.set_mode((reso_x, reso_y))


dirt = (101, 71, 31)
concrete = (37, 37, 37)
grass = (34, 126, 15)
sand = (176, 166, 76)

type_ = {1:(101, 71, 31), 2:(37, 37, 37), 3:(34, 126, 15), 4:(176, 166, 76), 5:((255, 0, 221)), None:(0,0,0), 0:(255, 255, 255)}

screen.fill((0,0,0))


frequency = 10
octaves = 2
power = 1.5
number_of_different_tiles = 3 # the dictionary at the top must correspond to this and the colours too. im too tired to care so fuck off

map_ = map_gen.wanking_cunt(reso_x/divs, reso_y/divs, frequency, octaves, power, number_of_different_tiles)

print len(map_)
#while(True):
while True:

    for x in range(0,len(map_)-1):
        for y in range(0,len(map_[0])-1):
            z = map_[x][y]
            z = int(float((z)))
            #print type_[z]


            pygame.draw.rect(screen, type_[z], ((x+1)*divs,(y+1)*divs,divs,divs))
    pygame.display.update()
