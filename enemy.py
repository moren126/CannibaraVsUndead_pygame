import pygame as pg
from os import path
from random import randint, uniform

from colors import*
from steering import*

class Enemy(pg.sprite.Sprite):
    def __init__(self, gameParams, x, y, player):
        pg.sprite.Sprite.__init__(self) 
        self.WIDTH = gameParams.WIDTH
        self.HEIGHT = gameParams.HEIGHT

        self.l_image_orig = pg.image.load(path.join('Data', 'capybaraDead.png'))
        self.r_image_orig = pg.transform.flip(self.l_image_orig, True, False)   
        self.l_image = self.l_image_orig.copy()
        self.r_image = self.r_image_orig.copy()
        
        self.size = gameParams.STARTSIZE
        self.radius = int(1.3 * (self.size / 2) ) 
        self.image = pg.transform.scale(self.l_image, (self.size, self.size))
        self.facing = 'left'
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.pos = VEC(self.rect.center) 
        self.vel = VEC(MAX_SPEED, 0).rotate(uniform(0, 360))
        self.acc = VEC(0, 0)

        self.last_update = 0
        self.target = VEC(randint(0, gameParams.WIDTH), randint(0, gameParams.HEIGHT))
        
        self.player = player
        self.state = 'separate'

    def face_left(self):
        self.image = pg.transform.scale(self.l_image, (self.size, self.size))
        self.facing = 'left'
        
    def face_right(self):    
        self.image = pg.transform.scale(self.r_image, (self.size, self.size))
        self.facing = 'right'

    def change_image(self):
        if self.state == 'separate':
            self.l_image_orig = pg.image.load(path.join('Data', 'capybaraDead.png'))
            self.r_image_orig = pg.transform.flip(self.l_image_orig, True, False)   
            self.l_image = self.l_image_orig.copy()
            self.r_image = self.r_image_orig.copy()
            
            if self.facing == 'left':
                self.image = pg.transform.scale(self.l_image, (self.size, self.size))
            elif self.facing == 'right':
                self.image = pg.transform.scale(self.r_image, (self.size, self.size))  
                
        if self.state == 'stray':
            self.l_image_orig = pg.image.load(path.join('Data', 'capybaraDeadRed.png'))
            self.r_image_orig = pg.transform.flip(self.l_image_orig, True, False)   
            self.l_image = self.l_image_orig.copy()
            self.r_image = self.r_image_orig.copy()
            
            if self.facing == 'left':
                self.image = pg.transform.scale(self.l_image, (self.size, self.size))
            elif self.facing == 'right':
                self.image = pg.transform.scale(self.r_image, (self.size, self.size))                    
        
    def check_for_player(self, obs):
        player_center = self.player.pos
        d = player_center.distance_to(self.pos)
        timez = int(d/200)
        ahead_jump = int(0.75 * 200)
        
        obs_center = VEC(obs.rect.center)
        
        for i in range(1, timez+1):
            ahead_length = i * ahead_jump * self.vel.length() / MAX_SPEED
            ahead = self.pos + self.vel.normalize() * ahead_length
            d1 = obs_center.distance_to(ahead)
            if d1 <= obs.radius:
                return True
                break
        return False
         
    def avoid_walls(self):
        steer = VEC(0, 0)
        self.desired = VEC(0, 0)
        near_wall = False
        if self.pos.x < WALL_LIMIT:
            self.desired = VEC(MAX_SPEED, self.vel.y)
            near_wall = True
        if self.pos.x > self.WIDTH - WALL_LIMIT:
            self.desired = VEC(-MAX_SPEED, self.vel.y)
            near_wall = True
        if self.pos.y < WALL_LIMIT:
            self.desired = VEC(self.vel.x, MAX_SPEED)
            near_wall = True
        if self.pos.y > self.HEIGHT - WALL_LIMIT:
            self.desired = VEC(self.vel.x, -MAX_SPEED)
            near_wall = True
        if near_wall:
            steer = (self.desired )#- self.vel)
            if steer.length() > MAX_FORCE:
                steer.scale_to_length(MAX_FORCE)
        return steer             
    
    def flee(self):
        dist = self.pos - self.player.pos
        if dist.length() < FLEE_DISTANCE:
            return evade(self, self.player)  
        else:
            return VEC(0,0)            
    '''    
    def seek(self):
        self.desired = (self.target2 - self.pos).normalize() * MAX_SPEED
        steer = (self.desired - self.vel)
        
        if self.pos.x > 10:#or self.pos.y < 380:
            self.faze = 'second'
        
        if steer.length() > MAX_FORCE:
            steer.scale_to_length(MAX_FORCE)
        return steer        
    '''    
    def check_neighbours(self, neighbors):
        flockDist = self.size * 2
        flockNbr = 0
        temp_list = []

        for a in neighbors:
            dist = a.pos.distance_to(self.pos)
           
            if dist <= flockDist:
                flockNbr += 1
                temp_list.append(a)
        
        if flockNbr >= NEEDTOFLOCK:    
            for i in temp_list:
                i.state = 'flock'

    def update(self):   
        
        # wl/wyl trybu zblakanej owcy
        if self.player.vel == VEC(0, 0):
            change = random.random()
    
            if self.state == 'separate':
                if change < 0.01:
                    self.state = 'stray'
                    self.change_image()
            elif self.state == 'stray':
                if change < 0.03:
                    self.state = 'separate'
                    self.change_image()
        else:
            if self.state == 'stray':
                self.state = 'separate'
                self.change_image() 
        
        #    
        self.check_neighbours(ENEMIES)
    
        if self.state == 'flock':
            self.acc = arrive(self, self.player.pos, 'slow')         
            
        elif self.state == 'separate':    
            a = 0.99 * wander(self)
            b = 0.01 * hide(self, self.player, OBSTACLES) 
            self.acc = a + b
            self.acc += self.flee()  

        elif self.state == 'stray':
            self.acc = wander(self)
            self.acc += self.flee()  

        self.acc += self.avoid_walls()
        self.acc += separate(self, ENEMIES, self.player.pos)
        out(self, OBSTACLES)
        

        self.vel += self.acc
        
        if self.vel.length() > MAX_SPEED:
            self.vel.scale_to_length(MAX_SPEED)
        self.pos += self.vel
        
        if self.vel.x < 0:
            self.face_left()
        if self.vel.x > 0:
            self.face_right()            

        self.rect.center = self.pos 