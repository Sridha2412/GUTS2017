import os
import sys
import random
import time
import multiprocessing
import pygame, pygame.locals, worldObjects, random, os

pygame.init()
pygame.mixer.init()

SCREEN_SIZE = (1080, 620)

def doStuff(keystroke, mousepos, quit, change, clock, screen, background, allSprites, player):

    # print(keystroke[:])

    while quit.value == 1:
        # time
        clock.tick(40)

        keystate = pygame.key.get_pressed()
        if change == 0:
            for idx, i in enumerate(keystate):
                keystroke[idx] = keystate[idx]
        # else:
        #     print(keystroke[:])


        if keystroke[pygame.locals.K_w]:
            player.go_up(screen)

        if keystroke[pygame.locals.K_a]:
            player.go_left(screen)

        if keystroke[pygame.locals.K_s]:
            player.go_down(screen)

        if keystroke[pygame.locals.K_d]:
            player.go_right(screen)

        quit.value = 0

        #Events happen here
        for event in pygame.event.get():

            #on user close window, keepGoing sets to false and program quits
            if event.type == pygame.QUIT or keystroke[pygame.locals.K_ESCAPE]:
                quit.value = 2

        mouse = pygame.mouse.get_pos()
        if change == 1:
            for idx, i in enumerate(mouse):
                mousepos[idx] = mouse[idx]

        player.rotate(mousepos)


    # print(keystroke[119], keystroke[97], keystroke[115], keystroke[100])

def screen1(quit, keystroke, mousepos, lock):
    #This function takes care of logic behind game

    #display
    screen = pygame.display.set_mode((1080, 620))

    pygame.display.set_caption("Moving - 1")

    #Entities
    #Creating background
    """background_colour = (92, 34, 34)
    screen.fill(background_colour)"""

    background = pygame.image.load('black.png')
    background = pygame.transform.scale(background, (1080, 620))

    rect = background.get_rect()
    rect = rect.move((1080, 620))
    screen.blit(background, rect)

    """background = pygame.image.load('bg.jpg')
    background=background.convert()
    screen.blit(background, (0, 0))"""

    #Creating a player
    player = worldObjects.Player(screen)

    allSprites = pygame.sprite.OrderedUpdates(player)

    clock = pygame.time.Clock()

    while quit.value != 2:
        lock.acquire()
        lock.release()

        quit.value = 1
        doStuff(keystroke, mousepos, quit, 0, clock, screen, background, allSprites, player)

        # print(keystroke[119], keystroke[97], keystroke[115], keystroke[100])

        # print(2, keystroke[:])
        lock.acquire()
        lock.release()

        screen.blit(background,(0,0))
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()

        if quit.value == 2:
            pygame.quit()

    #close game window
    if quit.value == 2:
        pygame.quit()

def screen2(quit, keystroke, mousepos, lock):
    #This function takes care of logic behind game

    #display
    screen = pygame.display.set_mode((1080, 620))

    pygame.display.set_caption("Shooting - 2")

    #Entities
    #Creating background
    """background_colour = (92, 34, 34)
    screen.fill(background_colour)"""

    background = pygame.image.load('bg.jpg')
    background = pygame.transform.scale(background, (1080, 620))

    rect = background.get_rect()
    rect = rect.move((1080, 620))
    screen.blit(background, rect)

    """background = pygame.image.load('bg.jpg')
    background=background.convert()
    screen.blit(background, (0, 0))"""

    #Creating a player
    player = worldObjects.Player(screen)

    allSprites = pygame.sprite.OrderedUpdates(player)

    # ACTION HAPPENING
    # Assign
    clock = pygame.time.Clock()

    while quit.value != 2:
        lock.acquire()
        lock.release()

        quit.value = 1
        # print(2, keystroke[:])
        doStuff(keystroke, mousepos, quit, 1, clock, screen, background, allSprites, player)

        lock.acquire()
        lock.release()

        screen.blit(background,(0,0))
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()

        if quit.value == 2:
            pygame.quit()

    #close game window
    if quit.value == 2:
        pygame.quit()


if __name__ == "__main__":
    lock = multiprocessing.Lock()
    quit = multiprocessing.Value('i', 1)
    keystroke = multiprocessing.Array('i', 323)
    mousepos = multiprocessing.Array('i', 2)

    p1 = multiprocessing.Process(target = screen1, args = (quit, keystroke, mousepos, lock, ))
    p2 = multiprocessing.Process(target = screen2, args = (quit, keystroke, mousepos, lock, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
