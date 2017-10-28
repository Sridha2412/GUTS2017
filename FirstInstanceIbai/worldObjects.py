#Class file with player ability to move only
import pygame,math,os,random

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        #This retrieves all the possible looks of the character from system different
        self.__list = []
        for file in os.listdir("playerImage/"):
            self.__list.append(pygame.image.load('./playerImage/' + file))

        #Set initial look to first element in _list
        """TODO: ask for gun input next"""
        self.image = self.__list[0]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        #set saved image
        self.__saved_image = self.image

        #resize image
        w,h = self.__saved_image.get_size()
        self.image = pygame.transform.scale(self.__saved_image, (int(w*0.3), int(h*0.3)))


        #Set the rect properties for our player
        #Don't ask me why I chose these numbers because I don't have an answer
        #They just work **magic**
        self.rect.left = 0
        self.rect.top = 200
        self.rect.right = 700
        self.rect.bottom = 500
        self.__speed = 4

        #Sets angle value aka: where the player is facing
        self.__angle = 0


    #methods to make player move
    def go_right(self, screen):
        #go right if rect.right < screen width
        allowLimit = int(screen.get_width()+150)
        if self.rect.right > allowLimit:
            None
        else:
            self.rect.right += self.__speed

    def go_left(self, screen):
        if self.rect.left < 0:
            None
        else:
            self.rect.left -= self.__speed

    def go_up(self,screen):
        if self.rect.top < 100:
            None
        else:
            self.rect.top-=self.__speed

    def go_down(self,screen):

        allowLimit = screen.get_height()+150
        if self.rect.bottom > allowLimit:
            None
        else:
            self.rect.bottom+=self.__speed


    #Methods for HP and player status1
    def change_image(self,weapon):
        '''accepts an index(weapon).Changes the player image based on index'''
        #Set original image
        self.image = self.__list[weapon]
        self.image = self.image.convert_alpha()

    #This stays disabled for player who cannot see
    """TODO: add toggle so that this functions runs for player who can aim """
    def rotate(self,mouse_pos):
        self.__angle = math.degrees(math.atan2\
              (self.rect.centerx-mouse_pos[0], self.rect.centery-mouse_pos[1]))

        #(self.__saved_image, self.__angle)
        self.image=pygame.transform.rotate\
            (self.actualSize, self.__angle)

        self.rect = self.image.get_rect(center=self.rect.center)

    def get_angle(self):
        '''returns current angle'''
        return self.__angle

class Creepers(pygame.sprite.Sprite):

    def __init__(self, screen, speed, damage, hp, attack_speed, value, image, zombie_type, player_pos):
        pygame.sprite.Sprite.__init__(self)

        #Assign screen to a variable
        self.__screen = screen

        #Assign speed to a variable
        self.__speed = speed
        self.__default_speed = speed

        #Assign the bullet damage to a variable
        self.__damage = damage

        #Assign attack speed to a variable
        self.__attack_speed = attack_speed

        #Assign value to a variable
        self.__value = value

        #Assign wave type to a variable
        self.__zombie_type = zombie_type

        #set variable for move
        self.__move = True

        #set counter for zombie attack speed
        self.__count = (attack_speed-1)

        #set variables for slow
        self.__slow = False
        self.__slow_counter = 0

        self.image = image
        self.image.convert_alpha()
        self.__saved_image = self.image
        self.rect = self.image.get_rect()

        #Assigning initial zombie spawn point
        self.spawn()

        #Rotate the zombie towards player
        self.rotate(player_pos)

        #calculate distance and step amount
        self.set_step_amount(player_pos)

    def reset_attack(self):
        #Resets acount counter
        self.__count = self.__attack_speed-1

    def get_attack(self):
        self.__count += 1
        if self.__count == self.__attack.speed:
            self.__count = 0
            return True
        else:
            return False

    def get_zombie_type(self):
        #Gets zombie type
        return self__zombie_type

    def get_damage(self):
        #Get damage value of zombie
        return self.__damage

    def get_value(self):
        #Get value
        return self.__value

    #This may not work because player doesn't have attribue HP yet.
    # TODO add HP attribute to Player class
    """def damage_hp(self, damage):
        #Subtract damage from hpand returns the state of the hp
        self.__hp -= damage
        if self.__hp > 0:
            return True
        else:
            return False
    """

    def slow(self):
        #halves speed of zombie and sets slow to True so it stays that way till False
        self.__speed = self.__speed / 2
        self.__slow = True

    def set_step_amount(self, player_pos):
        #calculate steps needed to get to player
        try:
            self.__distance=math.sqrt\
                (pow(player_pos[0]-self.rect.centerx,2)+pow(player_pos[1]-self.rect.centery,2))
            self.__animation_steps=self.__distance/self.__speed
            self.__dx=(player_pos[0]-self.rect.centerx)/self.__animation_steps
            self.__dy=(player_pos[1]-self.rect.centery)/self.__animation_steps
        except:
            self.__dx=0
            self.__dy=0

    def move(self, bool):
        #sets move variable to passed parameter bool
        self.__move = bool

    def spawn(self):
        #randomly spawns zombie from left, rigt or bottom
        self.__spawn = random.randint(1,3)

        #Spawning on Left
        if self.__spawn == 1:
            self.__x = random.randrange(0, -300, -30)
            self.__y = random.randint(0, self.__screen.get_height()-100)

        #Spawning on right
        elif self.__spawn == 2:
            self.__x = random.randint(self.__screen.get_width(), self.__screen.get_width()+300)
            self.__y=random.randint(0,self.__screen.get_height()-100)

        #Spawning on bottom
        elif self.__spawn == 3:
            self.__x = random.randint(0, self.__screen.get_width())
            self.__y = random.randint(self.__screen.get_height(), self.__screen.get_height()+300)

        self.rect.center = (self.__x, self.__y)

    def rotate(self, player_pos):
        #Takes player position and rotates zombies towards it
        self.__angle = math.degrees(math.atan2\
        (self.rect.centerx - player_pos[0], self.rect.centery - player_pos[1]))

        self.image = pygame.transform.rotate\
        (self.__saved_image, self.__angle)

        self.rect = self.image.get_rect(center = self.rect.center)

    def update(self):
        """if move is true, the zombie will move. if slow is true, slow counter
        be increased and when the counter reaches 400 or greater, the counter resets
        and slow is no longer true
        *** ESSENTIALLY the main method for the zombies"""

        if self.__move:
            self.rect.centerx += self.__dx
            self.rect.centery += self.__dy

        if self.__slow:
            self.__slow_counter += 1
            if self.__slow_counter >= 400:
                self.__speed = self.__default_speed
                self.__slow_counter = 0
                self.__slow = False
