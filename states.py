class GameStates(object):

    def __init__(self):

        self.STATE = 'WelcomeMenu'
   
        #parametry poziomu trudnosci (domyslnie easy)
        self.DIFFNAME = 'Easy'
        self.HEALTH = 100
        
        self.MOVERATE = 9
        self.BOUNCERATE = 6
        self.BOUNCEHEIGHT = 30
        self.STARTSIZE = 40
        ###
        self.WINSIZE = 400
        self.MAXHEALTH = 5
        ###
        self.CAPMINSPEED = 3
        self.CAPMAXSPEED = 7

    ### stan gry    
    def setState(self, state):
        if state == 'WelcomeMenu':
            self.STATE = 'WelcomeMenu'
        elif state == 'DiffMenu':
            self.STATE = 'DiffMenu'
        elif state == 'ScoreMenu':
            self.STATE = 'ScoreMenu'    
        elif state == 'Game':
            self.STATE = 'Game'    
        else:
            print('Wrong STATE name')        

    ### poziomy trudnosci 
    def setEasy(self):
        self.DIFFNAME = 'Easy'
        self.HEALTH = 100

        self.MOVERATE = 9
        self.BOUNCERATE = 6
        self.BOUNCEHEIGHT = 30
        self.STARTSIZE = 40
        ###
        self.WINSIZE = 400
        self.MAXHEALTH = 5
        ###
        self.CAPMINSPEED = 3
        self.CAPMAXSPEED = 7

    def setMedium(self):
        self.DIFFNAME = 'Medium'
        self.HEALTH = 80
        
        self.MOVERATE = 9
        self.BOUNCERATE = 5
        self.BOUNCEHEIGHT = 28
        self.STARTSIZE = 20
        ###
        self.WINSIZE = 400
        self.MAXHEALTH = 4
        ###
        self.CAPMINSPEED = 4
        self.CAPMAXSPEED = 8
        
    def setHard(self):
        self.DIFFNAME = 'Hard'
        self.HEALTH = 60  
        
        self.MOVERATE = 9
        self.BOUNCERATE = 4
        self.BOUNCEHEIGHT = 26
        self.STARTSIZE = 20
        ###
        self.WINSIZE = 400
        self.MAXHEALTH = 3
        ###
        self.CAPMINSPEED = 5
        self.CAPMAXSPEED = 9        
    
    def getDifficulty(self):
        return self.DIFFNAME
    
    def getParams(self):
        return (
        self.HEALTH,

        self.MOVERATE,
        self.BOUNCERATE,
        self.BOUNCEHEIGHT,
        self.STARTSIZE,
        ###
        self.WINSIZE,
        self.MAXHEALTH,
        ###
        self.CAPMINSPEED,
        self.CAPMAXSPEED)

            
    def setDifficulty(self, name):
        if name == 'Easy':
            GameStates.setEasy(self)
        elif name == 'Medium':
            GameStates.setMedium(self)     
        elif name == 'Hard':
            GameStates.setHard(self)
        else:
            print('Wronf DIFFICULTY name')
    
if __name__ == '__main__':
    objGameStates = GameStates()  