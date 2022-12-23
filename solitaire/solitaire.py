import pygame
import random
pygame.init()

doDebug = True
# doDebug = False
def debug(msg):
    if doDebug: print("Debug " + str(msg))

SCREENSIZE = 1024,768
clock = pygame.time.Clock()

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
PADDING = 35,10
MENUAREA = 0, SCREENSIZE[1] - 60
SCREEN = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Solitaire 0P")
SCREEN.fill(COLOR["darkgreen"])

def buildset():
	debug("buildset")

	row = [i for i in (PADDING[0],) + tuple([i for i in range(225,1000,PADDING[0])])]
	col = [i for i in (tuple([i for i in range(PADDING[1],800,130)]))]
	# 28 slots, 1+2+3+4+5+6+7 rows
	# slot = (row, col, value, state)

	DECK = [
		"A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥",
		"A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠",
		"A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦",
		"A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣"
	]
	random.shuffle(DECK)
	slots = { # horizontal, vertical
		0 : (row[1], col[0], DECK[ 0], "u"),
		1 : (row[1], col[1], DECK[ 1], "d"),
		2 : (row[1], col[2], DECK[ 2], "d"),
		3 : (row[1], col[3], DECK[ 3], "d"),
		4 : (row[1], col[4], DECK[ 4], "d"),
		5 : (row[1], col[5], DECK[ 5], "d"),
		6 : (row[1], col[6], DECK[ 6], "d"),
		# 
		7 : (row[2], col[1], DECK[ 7], "u"),
		8 : (row[2], col[2], DECK[ 8], "d"),
		9 : (row[2], col[3], DECK[ 9], "d"),
		10: (row[2], col[4], DECK[10], "d"),
		11: (row[2], col[5], DECK[11], "d"),
		12: (row[2], col[6], DECK[12], "d"),
		#
		13: (row[3], col[2], DECK[13], "u"),
		14: (row[3], col[3], DECK[14], "d"),
		15: (row[3], col[4], DECK[15], "d"),
		16: (row[3], col[5], DECK[16], "d"),
		17: (row[3], col[6], DECK[17], "d"),
		#
		18: (row[4], col[3], DECK[18], "u"),
		19: (row[4], col[4], DECK[19], "d"),
		20: (row[4], col[5], DECK[20], "d"),
		21: (row[4], col[6], DECK[21], "d"),
		#
		22: (row[5], col[4], DECK[22], "u"),
		23: (row[5], col[5], DECK[23], "d"),
		24: (row[5], col[6], DECK[24], "d"),
		#
		25: (row[6], col[5], DECK[25], "u"),
		26: (row[6], col[6], DECK[26], "d"),
		#
		27: (row[7], col[6], DECK[27], "u"),
		#
		28: (row[0], col[0], DECK[28:-1], "d"),
		29: (row[0], col[1], "EMPTY", "e"),
		30: (row[0], col[3], "EMPTY", "e"),
		31: (row[0], col[4], "EMPTY", "e"),
		32: (row[0], col[5], "EMPTY", "e"),
		33: (row[0], col[6], "EMPTY", "e"),
	}
	return slots

	'''
	drawpile = 10,10,None
	playpile = 140,10,None
	blank = 270,10,None
	ace1 = 400,10,None
	ace2 = 530,10,None
	ace3 = 660,10,None
	ace4 = 790,10,None
	'''
	return slots

def drawset(set):
	debug("drawset")
	# set = dict(row, col, value, state)
	# debug(set)
	for card in set:
		debug(set[card])
		state = set[card][3]
		if state == 'u':
			text = str(set[card][2])
			pygame.draw.rect(SCREEN,COLOR["white"],(
				set[card][1],set[card][0],CARDSIZE[0],CARDSIZE[1]),0,15
			)
		elif state == 'd':
			text = str(set[card][2]) if doDebug == True else 'reverse'
			pygame.draw.rect(SCREEN,COLOR["gray"],(
				set[card][1],set[card][0],CARDSIZE[0],CARDSIZE[1]),0,15
			)
		elif state == 'e':
			text = 'empty'
			pygame.draw.rect(SCREEN,COLOR["gray"],(
				set[card][1],set[card][0],CARDSIZE[0],CARDSIZE[1]),2,15
			)
		
		pygame.draw.rect(SCREEN,COLOR["gold"],(
			set[card][1],set[card][0],CARDSIZE[0],CARDSIZE[1]),2,15
		)
		# print('♥♦♣♠')
		color = COLOR["black"]
		if '♥' in text or '♦' in text:
			color = COLOR["red"]
		
		text_display(text, color, (set[card][1]+5,set[card][0]+5))
		pygame.display.update()

def text_objects(text, font, color):
	debug("text_objects")
	textSurface = font.render("".join(text), True, color)
	return textSurface, textSurface.get_rect()

def text_display(text,color,coords):
	gamefont = pygame.font.SysFont('Impact',25)
	TextSurf, TextRect = text_objects(text, gamefont, color)
	TextRect.topleft = (coords)
	SCREEN.blit(TextSurf, TextRect)
	pygame.display.update()

def selectcard(mouse):
	debug("selectcard "+str(mouse))

def newgame():
    debug("newgame")

def endgame():
    debug("endgame")

def gameloop():
	is_running = True
	game = buildset()
	drawset(game)

	while is_running:
		mouse = pygame.mouse.get_pos()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				is_running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				debug("mouseclick " + str(mouse))
				selectcard(mouse)
		pygame.display.update()
		clock.tick(25)

gameloop()
pygame.quit()
quit()
