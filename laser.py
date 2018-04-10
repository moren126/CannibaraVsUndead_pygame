import pygame as pg
import math
from os import path

from colors import*
from steering import*


class Laser(pg.sprite.Sprite):
    def __init__(self, gameParams, player):
        pg.sprite.Sprite.__init__(self)
        
        self.player = player
        
        self.WIDTH = gameParams.WIDTH
        self.HEIGHT = gameParams.HEIGHT
        self.screen = gameParams.displaySurface
        
        self.size = 20
        self.image_orig = pg.image.load(path.join('Data', 'cannon.png'))
        self.image_scaled = pg.transform.scale(self.image_orig, (self.size, self.size))
        self.image = self.image_scaled.copy()

        self.rect = self.image.get_rect()
        self.rect.center = self.player.rect.center

        self.angle = self.get_angle(pg.mouse.get_pos())

    def get_angle(self, mouse): 
        offset = (mouse[1] - self.rect.centery, mouse[0] - self.rect.centerx)
        self.angle = 180 - math.degrees(math.atan2(*offset))
        self.image = pg.transform.rotate(self.image_scaled, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)    
    
    def update(self):
        self.rect.center = self.player.rect.center
        mouse = pg.mouse.get_pos()
        offset = (mouse[1] - self.rect.centery, mouse[0] - self.rect.centerx)
        self.angle = 180 - math.degrees(math.atan2(*offset))
        self.image = pg.transform.rotate(self.image_scaled, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)    

class LaserBeam(pg.sprite.Sprite):
    def __init__(self, gameParams, player_rect_center, laser_angle, player):
        pg.sprite.Sprite.__init__(self)
        
        self.player_rect_center = player_rect_center
        self.laser_angle = laser_angle
        
        self.WIDTH = gameParams.WIDTH
        self.HEIGHT = gameParams.HEIGHT
        self.screen = gameParams.displaySurface

        self.image_orig = pg.image.load(path.join('Data', 'ball.png'))
        self.image_scaled = pg.transform.scale(self.image_orig, (8, 8))
        #self.image = self.image_orig.copy()
        self.image = self.image_scaled.copy()

        self.rect = self.image.get_rect()
        self.rect.center = self.player_rect_center 

        self.angle = -math.radians(self.laser_angle - 180)
        
        self.move = [self.rect.x, self.rect.y]
        self.speed_magnitude = 40
        self.speed = (self.speed_magnitude * math.cos(self.angle), self.speed_magnitude * math.sin(self.angle))      

        self.player = player        

    def update(self):
        self.move[0] += self.speed[0]
        self.move[1] += self.speed[1]
        self.rect.topleft = self.move
        
        #pg.draw.line(self.screen, RED2, self.player.pos, self.rect.center, 5)
        
        if self.rect.centerx < 0 - 50 or self.rect.centerx > self.WIDTH + 50 or self.rect.centery < 0 - 50 or self.rect.centery > self.HEIGHT + 50:    
            self.kill()         