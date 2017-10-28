#Main method goes here
# I - Import and Initialize
import pygame,pygame.locals,random,os
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1000, 620))

SCREEN_SIZE = (1000, 800)

def main():
    #This function takes care of logic behind game

    #display
    pygame.display.set_caption("Moving up down left right")

    #Entities
    #Creating background
    background_colour = (92, 34, 34)
    screen.fill(background_colour)

    #Creating a player
    player = worldObjects.Player(screen)

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
            player(screen)

        if keystate[pygame.locals.K_a]:
            player.go_left(screen)

        if keystate[pygame.locals.K_s]:
            player.go_down(screen)

        if keystate[pygame.locals.K_d]:
            player.go_right(screen)

        #Events happen here
        for event in pygame.event.get():

            #on user close window, keepGoing sets to false and program quits
            if event.type == pygame.QUIT:
                keepGoing = False

        #rotate character to face mouse
        player.rotate(pygame.mouse.get_pos())

        # Refresh screen
        screen.blit(background,(0,0))
        allSprites.update()

        pygame.display.flip()

    #close game window
    pygame.quit()


# Call the main function to initiate game
main()
