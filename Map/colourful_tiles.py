import pygame, sys, map_gen, time

pygame.init()
reso_x = 2000
reso_y = 1300
divs = 4

screen = pygame.display.set_mode((reso_x, reso_y))

dirt = (101, 71, 31)
concrete = (37, 37, 37)
grass = (34, 126, 15)
sand = (176, 166, 76)

type_ = {1:(101, 71, 31), 2:(37, 37, 37), 3:(34, 126, 15), 4:(176, 166, 76), None:(0,0,0)}

screen.fill((0,0,0))

map_ = map_gen.wanking_cunt(reso_x/divs, reso_y/divs, 10, 0, 2, 4)

print len(map_),
#while(True):
while True:

    for i in range(len(map_)-1):
        x = map_[i][0][0]*divs
        y = map_[i][0][1]*divs
        z = map_[i][1]
        pygame.draw.rect(screen, type_[z], (x,y,divs,divs))
    pygame.display.update()
