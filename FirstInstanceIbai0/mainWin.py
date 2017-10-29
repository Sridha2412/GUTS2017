#Main method goes here
# I - Import and Initialize
import pygame,pygame.locals,worldObjects,random,os
pygame.init()
pygame.mixer.init()

SCREEN_SIZE = (1080, 620)
#screen = pygame.display.set_mode(SCREEN_SIZE)
screen = pygame.display.set_mode((1080, 620))


def main():
    #This function takes care of logic behind game

    #display
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

    #Creating sprites (players, zombies)
    #Creating a player
    player = worldObjects.Player(screen)

    # Create zombies
    #defining number of zombies that come up
    wave = [10,1,1,1,1,1,0] #default [10,10,10,5,5,5,0]

    #loads zombie images
    z_img = []
    for file in os.listdir("zombies/"):
        print(file)
        z_img.append(pygame.image.load("./zombies/"+file))
        z_img.append(pygame.image.load("./zombies/"+file))


    #zombie types
    #[speed, damage, hp, attack_speed, score value]
    z_info = [[3,5,10,100,2],[3,5,20,100,4],[3,5,20,100,6],[3,5,20,100,8]\
                  ,[3,5,20,100,10],[3,5,20,100,12],[15,20,100,100,40]]

    zombies = []

    #generate 5 random type zombies
    for i in range(5):
        while True:
            a = random.randint(0,5)
            if wave[a]:
                zombies.append(worldObjects.Creepers\
                               (screen, z_info[a][0], z_info[a][1],\
                                z_info[a][2], z_info[a][3], z_info[a][4], z_img[a], a, player.rect.center))
                wave[a]=wave[a]-1
                break

    #Ammo and gun stuff goes here

    #Player status [[current HP, max HP], [current armour, max armour], default speed]
    player_status=[[350,350],[200,200],3]

    #create HP stuff here

    #

    #Add sprite groups to be updated in this order
    zombieGroup = pygame.sprite.Group(zombies)
    allSprites = pygame.sprite.OrderedUpdates(player, zombieGroup)

    # ACTION HAPPENING

    # Assign
    clock = pygame.time.Clock()
    keepGoing = True

    # Wave number
    wave_num = 1

    #Wave values (how much should be spawn each wave)
    wave_value = [10,1,1,1,1,1,0]

    #number of zombies on screen
    active_zombies = 10

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

        #Collisions

        # Collision between player and zombies here
        x = pygame.sprite.spritecollide(player, zombieGroup, False)

        invincible_status = False #for now
        if x:
            for zombie in x:
                zombie.move(False)

                #if player is not invincible
                if not(invincible_status):
                    None    #TODO reduce armor by x

                else:
                    None    #TODO subtract hp by y
                    #if playerHP is under 0 - keepGoing = False

        else:
            for zombie in zombieGroup:
                zombie.move(True)
                zombie.reset_attack()


        #zombies
        #Adjust zombies
        for zombie in zombieGroup:
            zombie.rotate(player.rect.center)
            zombie.set_step_amount(player.rect.center)

        #check if wave has been cleared
        if sum(wave) == 0:
            active_zombies += 1
            wave_num += 1
            wave_increase += 1 #default is 7
            for index in range(len(wave_value) - 1):
                wave_value[index] = wave_value[index] + wave_incerase
                wave[index] = wave_value[index]
                if index/3:
                    wave_incerase -= 2

        #generate new zombies if there is less zombies than there should be
        while len(zombieGroup) != active_zombies:
            a = random.randint(0,5)
            if wave[a]:
                wave[a] = wave[a]-1
                zombie = (worldObjects.Creepers\
                               (screen,z_info[a][0],z_info[a][1],\
                                z_info[a][2],z_info[a][3],z_info[a][4],z_img[a],a,player.rect.center))
                zombieGroup.add(zombie)
                allSprites = pygame.sprite.OrderedUpdates\
                           (player,zombieGroup)



        #rotate character to face mouse
        #player.rotate(pygame.mouse.get_pos())

        # Refresh screen
        screen.blit(background,(0,0))
        allSprites.update()
        allSprites.draw(screen)




        pygame.display.flip()

    #close game window
    pygame.quit()


# Call the main function to initiate game
main()
