import random, math, pygame

class Camera:

    def getRandomOffCameraPos(windowParameters, camerax, cameray, objWidth, objHeight):
    
        cameraRect = pygame.Rect(camerax, cameray, windowParameters.WIDTH, windowParameters.HEIGHT)
        while True:
            x = random.randint(camerax - windowParameters.WIDTH, camerax + (2 * windowParameters.WIDTH))
            y = random.randint(cameray - windowParameters.HEIGHT, cameray + (2 * windowParameters.HEIGHT))

            objRect = pygame.Rect(x, y, objWidth, objHeight)
            if not objRect.colliderect(cameraRect):
                return x, y
                
    def isOutsideActiveArea(windowParameters, camerax, cameray, obj):

        boundsLeftEdge = camerax - windowParameters.WIDTH
        boundsTopEdge = cameray - windowParameters.HEIGHT
        boundsRect = pygame.Rect(boundsLeftEdge, boundsTopEdge, windowParameters.WIDTH * 3, windowParameters.HEIGHT * 3)
        objRect = pygame.Rect(obj['x'], obj['y'], obj['width'], obj['height'])
        return not boundsRect.colliderect(objRect)