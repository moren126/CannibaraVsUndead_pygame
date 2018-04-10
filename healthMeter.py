import pygame as pg

from colors import* 

class HealthMeter:

    def drawHealthMeter(winParameters, currentHealth, MAXHEALTH):
      
        for i in range(currentHealth): 
        
            heartVertices = [ 
            (20 + ( MAXHEALTH - i - 1 ) * 30 , winParameters.HEIGHT - 15), 
            (10 + ( MAXHEALTH - i - 1 ) * 30 , winParameters.HEIGHT - 30), 
            (15 + ( MAXHEALTH - i - 1 ) * 30 , winParameters.HEIGHT - 35), 
            (20 + ( MAXHEALTH - i - 1 ) * 30 , winParameters.HEIGHT - 30), 
            (25 + ( MAXHEALTH - i - 1 ) * 30 , winParameters.HEIGHT - 35), 
            (30 + ( MAXHEALTH - i - 1 ) * 30 , winParameters.HEIGHT - 30)]
        
            pg.draw.polygon(winParameters.displaySurface, RED, heartVertices)
            

            
    def drawHealthBar(winParameters, health):
        if health < 0:
            health = 0
        BAR_LENGTH = 100
        BAR_HEIGHT = 20
        fill = (health / 100) * BAR_LENGTH
        outline_rect = pg.Rect(20, winParameters.HEIGHT - 40, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pg.Rect(20, winParameters.HEIGHT - 40, fill, BAR_HEIGHT)
        pg.draw.rect(winParameters.displaySurface, RED, fill_rect)
        pg.draw.rect(winParameters.displaySurface, WHITE, outline_rect, 2)

