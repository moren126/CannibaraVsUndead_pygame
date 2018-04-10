import pygame as pg
from os import path

from colors import*
from steering import*


class Player(pg.sprite.Sprite):
    def __init__(self, gameParams):
        pg.sprite.Sprite.__init__(self)
     
        self.WIDTH = gameParams.WIDTH
        self.HEIGHT = gameParams.HEIGHT
        self.screen = gameParams.displaySurface
        self.moverate = gameParams.MOVERATE
     
        self.l_image_orig = pg.image.load(path.join('Data', 'capybara.png'))
        self.r_image_orig = pg.transform.flip(self.l_image_orig, True, False)   
        self.l_image = self.l_image_orig.copy()
        self.r_image = self.r_image_orig.copy()
        self.start_size = gameParams.STARTSIZE
        self.size = self.start_size
       
        self.image = pg.transform.scale(self.l_image, (self.size, self.size))
        self.facing = 'left'
        
        self.rect = self.image.get_rect()
        self.radius = 25 #int(self.size / 2)   

        self.rect.center = (gameParams.HALFWIDTH, gameParams.HALFHEIGHT)
        self.pos = VEC(self.rect.centerx, self.rect.centery)
        self.vel = VEC(0, 0)
        
        self.health = 100
        
    def face_left(self):
        self.image = pg.transform.scale(self.l_image, (self.size, self.size))
        self.facing = 'left'
        
    def face_right(self):    
        self.image = pg.transform.scale(self.r_image, (self.size, self.size))
        self.facing = 'right'
                        
    def update(self):          
        keystate = pg.key.get_pressed()

        if keystate[pg.K_UP] or keystate[pg.K_w]:
            self.vel.y -= self.moverate
        if keystate[pg.K_DOWN] or keystate[pg.K_s]:
            self.vel.y += self.moverate
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.vel.x -= self.moverate
            if self.facing != 'left':
                self.face_left()
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.vel.x += self.moverate
            if self.facing != 'right':
                self.face_right()    

                
        out(self, OBSTACLES)


        if self.vel.length() > MAX_SPEED:
            self.vel.scale_to_length(MAX_SPEED)
        self.pos += self.vel

        self.rect.center = self.pos               
                
        # niewychodzenie za ekran          
        if self.rect.left < 0:
            self.rect.left = 0
            self.pos = VEC(self.rect.center)
        if self.rect.right > self.WIDTH:            
            self.rect.right = self.WIDTH 
            self.pos = VEC(self.rect.center)            
        if self.rect.top < 0:
            self.rect.top = 0
            self.pos = VEC(self.rect.center)
        if self.rect.bottom > self.HEIGHT:            
            self.rect.bottom = self.HEIGHT  
            self.pos = VEC(self.rect.center)    