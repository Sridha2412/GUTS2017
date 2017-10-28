import os
import sys
import random
import time
import multiprocessing
import pygame, pygame.locals, worldObjects, random, os

pygame.init()
pygame.mixer.init()

SCREEN_SIZE = (1080, 620)


def screen1():
    #This function takes care of logic behind game

    #display
    screen = pygame.display.set_mode((1080, 620))
    screen2 = pygame.display.set_mode((1080, 620))


    pygame.display.set_caption("Moving up down left right")

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
    keepGoing = True

    # main loop starts
    while keepGoing:
        # time
        clock.tick(40)

        #when key Pressed
        keystate = pygame.key.get_pressed()
        if keystate[pygame.locals.K_w]:
            player.go_up(screen)

        if keystate[pygame.locals.K_a]:
            player.go_left(screen)

        if keystate[pygame.locals.K_s]:
            player.go_down(screen)

        if keystate[pygame.locals.K_d]:
            player.go_right(screen)

        #Events happen here
        for event in pygame.event.get():

            #on user close window, keepGoing sets to false and program quits
            if event.type == pygame.QUIT or keystate[pygame.locals.K_ESCAPE]:
                keepGoing = False

        #rotate character to face mouse
        #player.rotate(pygame.mouse.get_pos())

        # Refresh screen
        screen.blit(background,(0,0))
        allSprites.update()
        allSprites.draw(screen)




        pygame.display.flip()

    #close game window
    pygame.quit()

def screen2():
    #This function takes care of logic behind game

    #display
    screen = pygame.display.set_mode((1080, 620))

    pygame.display.set_caption("Shooting")

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
    keepGoing = True

    # main loop starts
    while keepGoing:
        # time
        clock.tick(40)

        #when key Pressed
        keystate = pygame.key.get_pressed()
        if keystate[pygame.locals.K_w]:
            player.go_up(screen)

        if keystate[pygame.locals.K_a]:
            player.go_left(screen)

        if keystate[pygame.locals.K_s]:
            player.go_down(screen)

        if keystate[pygame.locals.K_d]:
            player.go_right(screen)

        #Events happen here
        for event in pygame.event.get():

            #on user close window, keepGoing sets to false and program quits
            if event.type == pygame.QUIT or keystate[pygame.locals.K_ESCAPE]:
                keepGoing = False

        #rotate character to face mouse
        # player.rotate(pygame.mouse.get_pos())

        # Refresh screen
        screen.blit(background,(0,0))
        allSprites.update()
        allSprites.draw(screen)


        pygame.display.flip()

    #close game window
    pygame.quit()

if __name__ == "__main__":
