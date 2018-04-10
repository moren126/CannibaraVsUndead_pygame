import pygame as pg
from os import path
from random import randint, uniform

from colors import*
from steering import*

class Obstacle(pg.sprite.Sprite):
    def __init__(self, gameParams, x, y, size):
        pg.sprite.Sprite.__init__(self)
       
        self.size = size    
        self.image_orig = pg.image.load(path.join('Data', 'cucumberSlice.png'))  
        self.image_orig2 = self.image_orig.copy()
        self.image = pg.transform.scale(self.image_orig2, (self.size, self.size))        
        self.rect = self.image.get_rect()        

        self.radius = int(1.0 * (self.size / 2))
     
        self.rect.centerx = x
        self.rect.centery = y
        self.pos = VEC(self.rect.center)
    
    def draw_params(gameParams, sizeMin, sizeMax):
        randp = randint(sizeMin, sizeMax)
        size = int( (randp * gameParams.WIDTH)/1900 )   
        posX = randint(size, gameParams.WIDTH - size)
        posY = randint(size, gameParams.HEIGHT - size)

        return(posX, posY, size)
    
    def find_position(gameParams, list):
        HALFWIDTH = gameParams.WIDTH // 2
        HALFHEIGHT = gameParams.HEIGHT // 2
    
        if list:            
            params = Obstacle.draw_params(gameParams, 80, 200)
            pos = VEC(params[0], params[1])
            
            cond = True
            while cond:    
                notCollision = True
                for obstacle in list:
                    if obstacle.pos.distance_to(pos) <= obstacle.radius + params[2] // 2 + 100 or (pos.x >= HALFWIDTH - 60 and pos.x <= HALFWIDTH + 60) or (pos.y >= HALFHEIGHT - 60 and pos.y <= HALFHEIGHT + 60):
                        notCollision = False      
                if notCollision:
                    cond = False
                    return params
                else:
                    params = Obstacle.draw_params(gameParams, 80, 200)
                    pos = VEC(params[0], params[1])
        else:
            params = Obstacle.draw_params(gameParams, 80, 200)
            
        return params