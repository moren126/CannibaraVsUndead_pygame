import pygame
from os import path
from colors import* 

class Eaten:

    def drawEatenCounter(winParameters, eatenCounter):
    
        BASICFONT = pygame.font.Font( (path.join('Data', 'Kenzo.otf')), 20) 
        eatenSurf = BASICFONT.render('KILLED: ', True, WHITE)
        eatenRect = eatenSurf.get_rect()
        eatenRect.center = (winParameters.WIDTH - 50, 30)
        winParameters.displaySurface.blit(eatenSurf, eatenRect)
        
        eatenCounterSurf = BASICFONT.render(str(eatenCounter), True, WHITE)
        eatenCounterRect = eatenCounterSurf.get_rect()
        eatenCounterRect.center = (winParameters.WIDTH - 15, 30)
        winParameters.displaySurface.blit(eatenCounterSurf, eatenCounterRect)