#Class file with player ability to move only
import pygame,math,os,random

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.mainWin.mainWin.__init__(self)

        #This retrieves all the possible looks of the character from system different
        self._looksList = []
        for file in os.listdir("playerImage/"):
            self._looksList.append(pygae.image.load("./playerImage/" + file))

        #Set initial look to first element in _list
        """TODO: ask for gun input next"""
        self.image = _looksList[0]
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        #set saved image
        self.__saved_image = self.image

        #Set the rect properties for our player
        self.rect.left = 0
        self.rect.top = 200
        self.__speed = 4

        #Sets angle value aka: where the player is facing
        self.__angle = 0


    #methods to make player move
    def go_right(self, screen):
        #go right if rect.right < screen width
        if self.rect.right > screen.get_width():
            None
        else:
            self.rect.right += self.__speed

    def go_left(self, screen):
        if self.rect.left < 0:
            None
        else:
            self.rect.left += self.__speed

    def go_up(self,screen):
        if self.rect.top < 100:
            None
        else:
            self.rect.top-=self.__speed

    def go_down(self,screen):
        if self.rect.bottom > screen.get_height():
            None
        else:
            self.rect.bottom+=self.__speed

    def rotate(self,mouse_pos):
        self.__angle = math.degrees(math.atan2\
              (self.rect.centerx-mouse_pos[0], self.rect.centery-mouse_pos[1]))

        self.image=pygame.transform.rotate\
            (self.__saved_image, self.__angle)

        self.rect = self.image.get_rect(center=self.rect.center)

    def get_angle(self):
        '''returns current angle'''
        return self.__angle
