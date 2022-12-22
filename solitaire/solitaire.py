import pygame
import random

pygame.init()
doDebug = True
is_running = True

COLOR = {
    "black" :	(0,0,0),
    "white" :	(255,255,255),
    "gray" : 	(127,127,127),
    "gold" : 	(212,161,69),
    "red": 		(255,0,0),
    "darkgreen":(20,120,74),
    "darkblue":	(16,27,61)
}

CARDSIZE = 120, 120*1.4
DECK = [
    "A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥",
    "A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦",
    "A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣",
    "A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠"
]

PADDING = 10,10
SCREENSIZE = 1024,768
MENUAREA = 0, SCREENSIZE[1] - 60

def shuffledeck():
    # take the ordered deck and shuffle them.
    debug(DECK)
    random.shuffle(DECK)
    global shuffled
    shuffled = True
    return DECK

def buildset():
    # take the shuffled deck and place cards in position
	debug("buildcards")
	# row1
	drawpile = 10,10
	playpile = 140,10
	blank = 270,10
	ace1 = 400,10
	ace2 = 530,10
	ace3 = 660,10
	ace4 = 790,10

	# row2		
	c1 = 10,188
	c2 = 140,188
	c3 = 270,188
	c4 = 400,188
	c5 = 530,188
	c6 = 660,188
	c7 = 790,188
    
	for card in DECK:
		debug(card)
        # wait what


def drawset(c):
	debug("displaycard")

SCREEN = pygame.display.set_mode(SCREENSIZE)
SCREEN.fill(COLOR["darkgreen"])
pygame.display.set_caption("Solitaire 0P")
pygame.display.flip()
gamefont = pygame.font.SysFont('Corbel',25)

shuffled = False
dealt = False
faceup = False
def debug(msg):
    if doDebug: print("Debug " + str(msg))

def newgame():
    debug("newgame")

def endgame():
    debug("endgame")

while is_running:
	mouse = pygame.mouse.get_pos()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			debug("mouseclick " + str(mouse))
	pygame.display.flip()
pygame.quit()