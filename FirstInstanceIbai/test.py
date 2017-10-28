import os
import sys
import random
import time
import multiprocessing
import pygame, pygame.locals, worldObjects, random, os

pygame.init()
pygame.mixer.init()

SCREEN_SIZE = (1080, 620)

def doStuff(keystroke, quit, change, clock, screen, background, allSprites, player):

    while quit.value == 1:
        # time
        clock.tick(40)

        if change.value == 0:
            keystroke = pygame.key.get_pressed()
            change.value = 1

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

        # Refresh screen
        screen.blit(background,(0,0))
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()


def screen1(quit, change, keystroke, lock):
    #This function takes care of logic behind game

    #display
    screen = pygame.display.set_mode((1080, 620))

    pygame.display.set_caption("Moving - 1")

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

    clock = pygame.time.Clock()

    while quit.value != 2:
        # lock.acquire()
        # lock.release()

        quit.value = 1
        doStuff(keystroke, quit, change, clock, screen, background, allSprites, player)

        lock.acquire()
        lock.release()


        if quit.value == 2:
            pygame.quit()
        change.value = 0


    #close game window
    if quit.value == 2:
        pygame.quit()

def screen2(quit, change, keystroke, lock):
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
        # lock.acquire()
        # lock.release()

        # print(2, str(keystroke))
        quit.value = 1
        print(2, change.value)
        doStuff(keystroke, quit, change, clock, screen, background, allSprites, player)

        lock.acquire()
        lock.release()

        if quit.value == 2:
            pygame.quit()

        change.value = 0


    #close game window
    if quit.value == 2:
        pygame.quit()


if __name__ == "__main__":
    lock = multiprocessing.Lock()
    quit = multiprocessing.Value('i', 1)
    change = multiprocessing.Value('i', 0)
    keystroke = multiprocessing.Array('i', 323)

    p1 = multiprocessing.Process(target = screen1, args = (quit, change, keystroke, lock, ))
    p2 = multiprocessing.Process(target = screen2, args = (quit, change, keystroke, lock, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
