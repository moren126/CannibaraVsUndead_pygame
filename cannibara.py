import pygame, time, random
import tkinter
import os

from parameters import Parameters
from colors import* 
from states import GameStates
from button import button, drawselectedButton, caption
from game import*

class WelcomeScreen(Parameters):

    def __init__(self):
        super(WelcomeScreen, self).__init__()               
        self.WELCOMEMENU = True
        self.DIFFMENU = False
        self.SCOREMENU = False        
        
    def main(self):
        pygame.init()   
        pygame.display.set_icon(pygame.image.load(path.join('Data', 'capybaraUltra.png')))
        pygame.display.set_caption('CannibaraVsUNDEAD')  
        
        objState = GameStates() 

        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            # tlo gry (zielone)    
            self.displaySurface.fill(GROUNDCOLOR)
            
            # tytul gry
            caption(self, 'Cannibara', self.FONTSIZEMAIN, 0, 0, 0, 0, self.HALFWIDTH, self.HALFHEIGHT - int( (400 * self.HEIGHT)/1000 ), False)
            caption(self, 'Vs', self.FONTSIZEMAIN - 20, 0, 0, 0, 0, self.HALFWIDTH, self.HALFHEIGHT - int( (290 * self.HEIGHT)/1000 ), False)
            caption(self, 'UNDEAD', self.FONTSIZEMAIN, 0, 0, 0, 0, self.HALFWIDTH, self.HALFHEIGHT - int( (180 * self.HEIGHT)/1000 ), False, PURPLE)  

            # logo - zywa kapibara
            aliveSurface = pygame.image.load(path.join('Data', 'capybaraUltra.png'))
            aliveSurfaceScaled = pygame.transform.scale( aliveSurface, (int( (355 * self.WIDTH)/1900 ), int( (250 * self.HEIGHT)/1000 )) )
            self.displaySurface.blit(aliveSurfaceScaled, (self.HALFWIDTH - int( (180 * self.WIDTH)/1900 ), self.HALFHEIGHT - int( (100 * self.HEIGHT)/1000 )))
            
            # logo cd. - martwe kapibary, prawa strona
            deadSurface = pygame.image.load(path.join('Data', 'capybaraDead.png'))
            deadSurfaceScaled = pygame.transform.scale( deadSurface, (int( (355 * self.WIDTH)/1900 ), int( (250 * self.HEIGHT)/1000 )) )
            self.displaySurface.blit(deadSurfaceScaled, (self.HALFWIDTH + int( (200 * self.WIDTH)/1900 ), self.HALFHEIGHT - int( (100 * self.HEIGHT)/1000 )))
            self.displaySurface.blit(deadSurfaceScaled, (self.HALFWIDTH + int( (380 * self.WIDTH)/1900 ), self.HALFHEIGHT ))
            
            # logo cd. - martwe kapibary, lewa strona
            mirrorDeadSurface = pygame.transform.flip(deadSurface, True, False)   
            mirrorDeadSurfaceScaled = pygame.transform.scale( mirrorDeadSurface, (int( (355 * self.WIDTH)/1900 ), int( (250 * self.HEIGHT)/1000 )) )            
            self.displaySurface.blit(mirrorDeadSurfaceScaled, (self.HALFWIDTH - int( (560 * self.WIDTH)/1900 ), self.HALFHEIGHT - int( (100 * self.HEIGHT)/1000 )))
            self.displaySurface.blit(mirrorDeadSurfaceScaled, (self.HALFWIDTH - int( (740 * self.WIDTH)/1900 ), self.HALFHEIGHT ))

            # przyciski        
            if objState.STATE == 'WelcomeMenu' and self.WELCOMEMENU: 
                if button(self, 'Play', self.FONTSIZE, self.BUTTONDISTANCE, self.HEIGHT - 125, self.BUTTONWIDTH, self.BUTTONHEIGHT):
                    WelcomeScreen.buttonAction(self, 'Start', objState)
                '''    
                if button(self, 'Difficulty', self.FONTSIZE, 2 * self.BUTTONDISTANCE + self.BUTTONWIDTH, self.HEIGHT - 125, self.BUTTONWIDTH, self.BUTTONHEIGHT):
                    WelcomeScreen.buttonAction(self, 'Difficulty', objState)
                if button(self, 'High Scores', self.FONTSIZE, 3 * self.BUTTONDISTANCE + 2 * self.BUTTONWIDTH, self.HEIGHT - 125, self.BUTTONWIDTH, self.BUTTONHEIGHT):
                    WelcomeScreen.buttonAction(self, 'HighScores', objState)
                '''    
                if button(self, 'Quit', self.FONTSIZE, 4 * self.BUTTONDISTANCE + 3 * self.BUTTONWIDTH, self.HEIGHT - 125, self.BUTTONWIDTH, self.BUTTONHEIGHT):
                    WelcomeScreen.buttonAction(self, 'Quit', objState)
            '''    
            elif objState.STATE == 'DiffMenu' and self.DIFFMENU:             
                if button(self, 'Easy',         self.FONTSIZE, (self.WIDTH - self.BUTTONWIDTH)/2, self.HALFHEIGHT + 160, self.BUTTONWIDTH, 40):
                    WelcomeScreen.buttonAction(self, 'Easy', objState)
                if button(self, 'Medium',       self.FONTSIZE, (self.WIDTH - self.BUTTONWIDTH)/2, (self.HALFHEIGHT + 160 + 35 + self.BUTTONDISTANCEH), self.BUTTONWIDTH, 40):                    
                    WelcomeScreen.buttonAction(self, 'Medium', objState)
                if button(self, 'Hard',         self.FONTSIZE, (self.WIDTH - self.BUTTONWIDTH)/2, (self.HALFHEIGHT + 160 + 70 + 2 * self.BUTTONDISTANCEH), self.BUTTONWIDTH, 40):                     
                    WelcomeScreen.buttonAction(self, 'Hard', objState)
                if button(self, 'Back to menu', self.FONTSIZE, 100, self.HEIGHT - self.BUTTONHEIGHT, self.BUTTONWIDTH + 30, 40):
                    WelcomeScreen.buttonAction(self, 'BackMenu', objState)
                    
                diff = objState.getDifficulty()    
                if diff == 'Easy':
                    drawselectedButton(self, 'Easy', self.FONTSIZE+2, (self.WIDTH - self.BUTTONWIDTH)/2, self.HALFHEIGHT + 160, self.BUTTONWIDTH, 40)
                elif diff == 'Medium':
                    drawselectedButton(self, 'Medium', self.FONTSIZE+2, (self.WIDTH - self.BUTTONWIDTH)/2, (self.HALFHEIGHT + 160 + 35 + self.BUTTONDISTANCEH), self.BUTTONWIDTH, 40)
                elif diff == 'Hard':
                    drawselectedButton(self, 'Hard', self.FONTSIZE+2, (self.WIDTH - self.BUTTONWIDTH)/2, (self.HALFHEIGHT + 160 + 70 + 2 * self.BUTTONDISTANCEH), self.BUTTONWIDTH, 40)  
                else:
                    print('Wrong DIFFICULTY name')
            '''
            '''    
            ###TODO kiedys, nie pali sie
            elif objState.STATE == 'ScoreMenu' and self.SCOREMENU:   
                # wyswietla osiagniete wyniki 
                showHighScore(self)

                if button(self, 'Back to menu', self.FONTSIZE, self.BUTTONDISTANCEX, self.BUTTONDOWNY, self.BUTTONWIDTH + 30, self.BUTTONHEIGHT):
                    WelcomeScreen.buttonAction(self, 'BackMenu', objState)    
            '''
            pygame.display.update()         
       
    # obsluga przyciskow z glownego menu        
    def buttonAction(self, msg, objState):

        if msg == 'Start': 
            time.sleep(0.2)

            objState.setState('Game')

            # obiekt odpowiedzialny za rozgrywke
            objGame = Game()
            objGame.runGame(objState)
            
        elif msg == 'Quit':
            pygame.quit()
            quit() 
 
        '''
        elif msg == 'Difficulty':
            time.sleep(0.2)
            self.WELCOMEMENU = False
            self.DIFFMENU = True
            objState.setState('DiffMenu')
                        
        elif msg == 'HighScores':
            time.sleep(0.2)
            self.WELCOMEMENU = False
            self.SCOREMENU = True
            objState.setState('ScoreMenu')
        '''                 

        '''
        elif msg == 'BackMenu':
            time.sleep(0.2)
            self.WELCOMEMENU = True
            self.DIFFMENU = False
            self.SCOREMENU = False
            objState.setState('WelcomeMenu')
            
        elif msg == 'Easy':
            time.sleep(0.2)
            objState.setDifficulty('Easy')
                        
        elif msg == 'Medium':
            time.sleep(0.2)
            objState.setDifficulty('Medium')
                        
        elif msg == 'Hard':
            time.sleep(0.2)
            objState.setDifficulty('Hard')            

        elif msg == 'Classic':
            time.sleep(0.2)
            objState.setMode('Classic')

        elif msg == 'Continuous':
            time.sleep(0.2)
            objState.setMode('Continuous')
        '''
            
if __name__ == '__main__':
    objWelcomeScreen = WelcomeScreen()
    objWelcomeScreen.main() 