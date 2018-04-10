import pygame, tkinter, os
from os import path

class Parameters(object):

    def __init__(self):
    
        #parametry okna
        #os.environ['SDL_VIDEO_CENTERED'] = '1'
        os.environ['SDL_VIDEO_WINDOW_POS'] = '10, 30'
        root = tkinter.Tk()
        self.WIDTH = root.winfo_screenwidth() - 20
        self.HEIGHT = root.winfo_screenheight() - 80
        self.HALFWIDTH = int(self.WIDTH / 2)
        self.HALFHEIGHT = int(self.HEIGHT / 2) 
        self.notFullscreen = True      
        self.displaySurface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        #self.displaySurface = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        
        self.FONTNAME = path.join('Data', 'Kenzo.otf')
        self.FONTNAMEITALIC = path.join('Data', 'KenzoRegularItalic.otf')
        self.FONTSIZE = int((30 * self.HEIGHT) / 1000)
        self.FONTSIZE30 = int((30 * self.HEIGHT) / 1000)
        self.FONTSIZE48 = int((48 * self.HEIGHT) / 1000)
        self.FONTSIZE70 = int((70 * self.HEIGHT) / 1000)
        self.FONTSIZEMAIN = int((120 * self.HEIGHT) / 1000)        
                
        #odleglosc miedzy przyciskami
        self.BUTTONWIDTH = int((150 * self.WIDTH) / 1900)   
        self.BUTTONHEIGHT = int((50 * self.HEIGHT) / 1000)   
        self.BUTTONDISTANCE = int((self.WIDTH - 4 * self.BUTTONWIDTH)/5)
        self.BUTTONDISTANCEH = int((self.HALFHEIGHT - 125 - 4 * 40)/2)
       
if __name__ == '__main__':
    objParameters = Parameters()      