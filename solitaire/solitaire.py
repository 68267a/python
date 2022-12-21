import pygame
import random

pygame.init()
doDebug = True
is_running = True

SCREENSIZE = 1024,768
MENUAREA = 0, SCREENSIZE[1] - 60
CARDSIZE = 120, 120*1.4
COLOR = {
    "black" :	(0,0,0),
    "white" :	(255,255,255),
    "gray" : 	(127,127,127),
    "gold" : 	(212,161,69),
    "red": 		(255,0,0),
    "darkgreen":(20,120,74),
    "darkblue":	(16,27,61)
}

deck = {
    "red": ("♥","♦"),
    "black": ("♣","♠")
    
}

SCREEN = pygame.display.set_mode(SCREENSIZE)
SCREEN.fill(COLOR["darkgreen"])
pygame.display.set_caption("Solitaire 0P")
pygame.display.flip()
gamefont = pygame.font.SysFont('Corbel',25)

shuffled = False
dealt = False

def debug(msg):
    if doDebug: print("Debug " + str(msg))

def newgame():
    debug("newgame")

def endgame():
    debug("endgame")
    
