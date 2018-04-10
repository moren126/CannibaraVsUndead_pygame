import pygame as pg
import time, sys, math
from pygame.locals import*
import random
from os import path

from player import Player
from enemy import Enemy
from obstacle import Obstacle
from laser import Laser, LaserBeam
from parameters import Parameters
from states import GameStates
from button import caption
from colors import* 
from healthMeter import*
from eaten import*

#
PAUSE = False
#
     
class Game(Parameters):

    def __init__(self):
        super(Game, self).__init__()
        self.HEALTH = 0

        self.MOVERATE = 0
        self.BOUNCERATE = 0
        self.BOUNCEHEIGHT = 0
        self.STARTSIZE = 0

        self.CAPMINSPEED = 0
        self.CAPMAXSPEED = 0
        
        #self.CUCUMBERSIZE = int( (200 * self.WIDTH)/1900 ) 

        CUCUMBERX300 = int( (300 * self.WIDTH)/1900 )
        CUCUMBERX475 = int( (475 * self.WIDTH)/1900 ) 
        CUCUMBERX775 = int( (775 * self.WIDTH)/1900 ) 
        CUCUMBERX950 = int( (950 * self.WIDTH)/1900 )
        CUCUMBERX1300 = int( (1300 * self.WIDTH)/1900 )
        CUCUMBERX1600 = int( (1600 * self.WIDTH)/1900 )     
        CUCUMBERY250 = int( (250 * self.HEIGHT)/1000 ) 
        CUCUMBERY400 = int( (250 * self.HEIGHT)/1000 ) 
        CUCUMBERY650 = int( (650 * self.HEIGHT)/1000 ) 
        CUCUMBERY750 = int( (750 * self.HEIGHT)/1000 ) 
   
        self.CUCUMBERSX1 = [random.randint(CUCUMBERX300, CUCUMBERX475), random.randint(CUCUMBERX775, CUCUMBERX950), random.randint(CUCUMBERX1300, CUCUMBERX1600)]
        self.CUCUMBERSX2 = [random.randint(CUCUMBERX300, CUCUMBERX475), random.randint(CUCUMBERX775, CUCUMBERX950), random.randint(CUCUMBERX1300, CUCUMBERX1600)]
        self.CUCUMBERSY300 = [random.randint(CUCUMBERY250, CUCUMBERY400), random.randint(CUCUMBERY250, CUCUMBERY400), random.randint(CUCUMBERY250, CUCUMBERY400)]
        self.CUCUMBERSY700 = [random.randint(CUCUMBERY650, CUCUMBERY750), random.randint(CUCUMBERY650, CUCUMBERY750), random.randint(CUCUMBERY650, CUCUMBERY750)]
        
        self.MARGIN = int( (10 * self.WIDTH)/1900 )
        
    def runGame(self, objState):
    
        params = objState.getParams()
        self.HEALTH = params[0]

        self.MOVERATE = params[1]
        self.BOUNCERATE = params[2]
        self.BOUNCEHEIGHT = params[3]
        self.STARTSIZE = params[4]
        ###
        self.WINSIZE = params[5]
        self.MAXHEALTH = params[6]
        ###
        self.CAPMINSPEED = params[7]
        self.CAPMAXSPEED = params[8]
        
        first_shoot = 0
        cooldown = 0.2
        shoot_possible = True
        cooldown_time = time.time() 
        laserBeamObj = None
        self.RESPAWN = False
        self.DOITONCE = True
    
        FPSCLOCK = pg.time.Clock() 
        
        L_CAP_IMGEN = pg.image.load(path.join('Data', 'capybaraDead.png'))
        R_CAP_IMGEN = pg.transform.flip(L_CAP_IMGEN, True, False)   

        # audio 
        pg.mixer.music.load(path.join('Data', 'capybara_sound_mono.wav'))
        pg.mixer.music.play(-1)
        
        gameOverMode = False
        gameOverStartTime = 0
        winMode = False

        # licznik zabitych kapibar
        kills = 0
        
        playerObj = Player(self)
        ALL_SPRITES.add(playerObj)
        laserObj = Laser(self, playerObj)
        ALL_SPRITES.add(laserObj)  

        obstacles_list = []

        for i in range(20):  
            cucumber_params = Obstacle.find_position(self, obstacles_list)
            cucumber = Obstacle(self, cucumber_params[0], cucumber_params[1], cucumber_params[2])
            obstacles_list.append(cucumber)
            ALL_SPRITES.add(cucumber)
            OBSTACLES.add(cucumber)

        for i in range(20): 
            enemy = Enemy(self, random.randrange(- self.MARGIN, self.WIDTH + self.MARGIN), random.randrange(- self.MARGIN, self.HEIGHT + self.MARGIN), playerObj)
            ALL_SPRITES.add(enemy)
            ENEMIES.add(enemy)

        
        # główna pętla gry    
        while True:   
            self.displaySurface.fill(GROUNDCOLOR) 

            # rysowanie wskaźnika poziomu zdrowia
            HealthMeter.drawHealthBar(self, playerObj.health)

            # rysowanie licznika zjedzonych kapibar
            Eaten.drawEatenCounter(self, kills)

            hits = pg.sprite.spritecollide(playerObj, ENEMIES, True, pygame.sprite.collide_circle)
            for hit in hits:                   
                injured = pygame.mixer.Sound(path.join('Data', 'capybara_barks_mono.wav'))
                injured.play()
                playerObj.health -= 10
                if playerObj.health <= 0:
                    gameOverMode = True
                    gameOverStartTime = time.time()
            
            ALL_SPRITES.update()     
 
            # obsługa zdarzeń
            for event in pg.event.get():
                if event.type == QUIT:
                    Game.terminate()

                elif event.type == KEYDOWN:
                    if event.key == K_p:
                        PAUSE = True
                        Game.paused(self)
                    elif winMode and event.key == K_m:
                        return

                elif event.type == KEYUP:
                    if event.key == K_UP or event.key == K_w:                
                        playerObj.stop = False
                        playerObj.vel.y = 0
                    if event.key == K_DOWN or event.key == K_s:                
                        playerObj.stop = False  
                        playerObj.vel.y = 0
                    if event.key == K_LEFT or event.key == K_a:                
                        playerObj.stop = False  
                        playerObj.vel.x = 0
                    if event.key == K_RIGHT or event.key == K_d:                
                        playerObj.stop = False   
                        playerObj.vel.x = 0                       
                    if event.key == K_ESCAPE:
                        Game.terminate()
       
                elif event.type == pg.MOUSEBUTTONDOWN: 
                    first_shoot += 1              
                    shoot_time = time.time() 

                    if shoot_time - cooldown_time >= cooldown:
                        cooldown_time = shoot_time
                        shoot_possible = True
                    else:
                        shoot_possible = False

                elif event.type == pg.MOUSEBUTTONUP  and ( not gameOverMode):
                    if first_shoot != 0 and shoot_possible:
                        laserBeamObj = LaserBeam(self, playerObj.rect.center, laserObj.angle, playerObj)
                        ALL_SPRITES.add(laserBeamObj)   
           
            if laserBeamObj is not None:
                hitsWithEnemies = pg.sprite.spritecollide(laserBeamObj, ENEMIES, True, pg.sprite.collide_circle)
                for hit in hitsWithEnemies:
                    kills += 1    

                hitsWithObstacles = pg.sprite.spritecollide(laserBeamObj, OBSTACLES, False, pg.sprite.collide_circle)
                if hitsWithObstacles:
                    laserBeamObj.kill()
                    
            if kills % NEEDTOFLOCK == 0 and kills != 0:
                self.RESPAWN = True
            if kills % NEEDTOFLOCK != 0:
                self.DOITONCE = True
            
            if self.RESPAWN and self.DOITONCE:
                Game.newEnemies(self, playerObj, NEEDTOFLOCK - 1)
                self.RESPAWN = False
                self.DOITONCE = False
            
            #for cucumber in OBSTACLES:    
            #    pg.draw.circle(self.displaySurface, DARKGREEN, cucumber.rect.center, cucumber.radius)    

            ALL_SPRITES.draw(self.displaySurface)                  
               

            if not gameOverMode:
                pass
            else:
                # koniec gry
                ### napis Game Over
                caption(self, 'Game Over', self.FONTSIZE70, self.HALFWIDTH - int((150 * self.WIDTH) / 1900), self.HALFHEIGHT - int((65 * self.HEIGHT) / 1000), int((300 * self.WIDTH) / 1900), int((130 * self.HEIGHT) / 1000), self.HALFWIDTH, self.HALFHEIGHT, False)
                
                gameOverMode = True
                
                pg.mixer.music.fadeout(1000)
                playerObj.kill()
                laserObj.kill()
                if time.time() - gameOverStartTime > GAMEOVERTIME:
                    Game.terminate()              
                
                             
            pg.display.flip()     
            #pg.display.update()
            FPSCLOCK.tick(FPS)
            

    def newEnemies(self, playerObj, howMany):

        for i in range(int(howMany/2)): 
            enemy = Enemy(self, random.randrange(-self.MARGIN * 5, - self.MARGIN * 2), random.randrange(-self.MARGIN * 2, self.HEIGHT + self.MARGIN * 2), playerObj)
            ALL_SPRITES.add(enemy)
            ENEMIES.add(enemy)

        for i in range(int(howMany/2)):     
            enemy = Enemy(self, random.randrange(self.WIDTH + self.MARGIN * 2, self.WIDTH + self.MARGIN * 5), random.randrange(-self.MARGIN * 2, self.HEIGHT + self.MARGIN * 2), playerObj)      
            ALL_SPRITES.add(enemy)
            ENEMIES.add(enemy)
            
    def unpause():
        global PAUSE
        pg.mixer.music.unpause()
        PAUSE = False
    
    def paused(self):
        pg.mixer.music.pause()

        while PAUSE:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    Game.terminate()
                elif event.type == KEYDOWN:
                    if event.key == K_p:
                        Game.unpause()   
                        
            #kliknij p by kontynuowac
            caption(self, 'Click \'p\' to continue', self.FONTSIZE30, self.HALFWIDTH - int((150 * self.WIDTH) / 1900), self.HALFHEIGHT - int((50 * self.HEIGHT) / 1000), int((300 * self.WIDTH) / 1900), int((50 * self.HEIGHT) / 1000), self.HALFWIDTH, self.HALFHEIGHT - int((25 * self.HEIGHT) / 1000), True)

            pg.display.update()
            
    def terminate():
        pg.quit()
        sys.exit()