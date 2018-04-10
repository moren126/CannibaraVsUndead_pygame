import pygame as pg
from os import path

GROUNDCOLOR     = (34, 177, 76)
DARKGREEN       = (0, 51, 0)
WHITE           = (255, 255, 255)
RED             = (230, 0, 0)
RED2            = (158, 0, 0)
BRIGHTRED   = (255, 0, 0)
PURPLE      = (153, 0, 204)
BUTTONCOLOR = (230, 0, 0)
BUTTONBRIGHT= (255, 102, 0)


RAND_TARGET_TIME = 1000#500

MOB_SIZE = 16
MAX_SPEED = 4
MAX_FORCE = 0.15
WALL_LIMIT = 75#100
MAX_DIST = 3000

FLEE_DISTANCE = 220

ALL_SPRITES = pg.sprite.OrderedUpdates()
OBSTACLES = pg.sprite.Group()  
ENEMIES = pg.sprite.Group() 
WALLS = pg.sprite.Group() 

VEC = pg.math.Vector2

#DIR = path.join(path.dirname(__file__), 'Data')

FPS = 40

GAMEOVERTIME = 4


NEEDTOFLOCK = 5
