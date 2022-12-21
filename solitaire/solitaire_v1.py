import pygame
import random

pygame.init()

doDebug = True
is_running = True

WIDTH = 1024
HEIGHT = 768
MENU = (0, HEIGHT - 60)
CARDASPECT = 1.4
CARDX = 120
CARDY = CARDX * CARDASPECT
CARD = (CARDX,CARDY)
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (127,127,127)
GOLD = (212, 161, 69)
RED = (255,0,0)
DARKGREEN = (20,120,74)
DARKBLUE = (16, 27, 61)

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
SCREEN.fill(DARKGREEN)
pygame.display.set_caption('Solitaire 0P')
pygame.display.flip()
gamefont = pygame.font.SysFont('Corbel', 25)

shuffled = False
dealt = False



def debug(msg):
	if doDebug: print(msg)

def newgame():
	debug("newgame")

def endgame():
	debug("endgame")

def buildbutton(lx,ly,sx,sy,txt,fg,bg):
	'''
	location x/y, size x/y, button text, foreground, background
	TL	px,		py
	TR	px+sx	py+sy
	BL	px,		py+sy
	BR	px+sx	py+sy
	LBL	px+TLx,	py+TLy
	'''
	location = (lx, ly)
	padding = (10, 10)
	size = (sx, sy)
	labeloffset = (10, 10)
	coords = {
		"TL": (location[0]+padding[0],          location[1]+padding[1]),
		"TR": (location[0]+padding[0]+size[0],  location[1]+padding[1]+size[1]),
		"BL": (location[0]+padding[0],          location[1]+padding[1]+size[1]),
		"BR": (location[0]+padding[0]+size[0],  location[1]+padding[1]+size[1]),
	}
	lbl = (
		location[0]+padding[0]+labeloffset[0],
		location[1]+padding[1]+labeloffset[1]
	)

	text = gamefont.render(txt,True,fg)
	out = {
		"location": location,
		"size": size,
		"padding": padding,
		"text": text,
		"coords": coords,
		"label": lbl,
		"bg": bg
	}
	return out

def displaybutton(b):
	pygame.draw.rect(
		SCREEN,
		b['bg'],
		(b["coords"]["TL"], b["size"])
	)
	SCREEN.blit(b["text"], b['label'])

def builddeck():
	cards = {
		"values": range(1,13),
		"suits": (
			('H', 'RED'),  # hearts red
			('D', 'RED'),  # diamonds red
			('S', 'BLACK'),  # spades black
			('C', 'BLACK')   # clubs black
		)
	}
	deck = []
	for suit in cards['suits']:
		for value in cards['values']:
			deck.append((value,suit))
	return deck

def shuffledeck():
	deck = builddeck()
	debug(deck)
	random.shuffle(deck)
	debug(deck)
	global shuffled
	shuffled = True
	return deck

def buildcard(x, y, v,s,fg):  #value, suit, fg, bg
	face = str(v) + str(s)
	# debug(face)
	return buildbutton(x, y, CARD[0], CARD[1], face, fg, WHITE)

def buildgame():
	padding = 15
	cols = [ 0*CARDX+1*padding, 
		1*CARDX+2*padding, 2*CARDX+3*padding, 3*CARDX+4*padding, 
		4*CARDX+5*padding, 5*CARDX+6*padding, 6*CARDX+7*padding
	]
	col1 = cols.copy()
	del col1[2]
	rows = [ padding, CARDY+2*padding, CARDY+4*padding]
	for col in (col1, rows[0]), (cols, rows[1]), (cols, rows[2]):
		for x in range(len(col[0])):
			card = buildcard(
				col[0][x],
				col[1],
				x+1,
				# deck[x][0],     # value
				deck[x][1][0],  # suit
				deck[x][1][1],  # color
			)
			debug("col" + str(col[0]))
			displaybutton(card)


while is_running:
	mouse = pygame.mouse.get_pos()
	btnQuit = buildbutton(MENU[0], MENU[1], 90, 40, "Quit", WHITE, GRAY)  # Each button's TL is next to the previous TR
	btnShuffle = buildbutton(btnQuit["coords"]["TR"][0], MENU[1], 90, 40, "Shuffle", BLACK, RED)
	btnNewGame = buildbutton(btnShuffle["coords"]["TR"][0], MENU[1], 140, 40, "New Game", DARKBLUE, GOLD)  # new game
	for button in (btnQuit, btnShuffle, btnNewGame):
		displaybutton(button)

	for event in pygame.event.get():
		# debug(event)
		if event.type == pygame.QUIT:
			is_running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			debug("mouseclick" + str(mouse))
			# TODO: compare mouse[0] and mouse[1] to each button's coords - return that button's name and fire the function
			# if btnQuitCoords[0] <= mouse[0] <= btnQuitCoords[1] and btnQuitCoords[3] <= mouse[1] <= btnQuitCoords[4]:

			debug(str(btnQuit['coords']['TL'][0]) + " " + str(mouse[0]) + " " + str(btnQuit['coords']['TR'][0]))

			if btnQuit['coords']['TL'][0] <= mouse[0] <= btnQuit['coords']['TR'][0] and \
			btnQuit['coords']['TL'][1] <= mouse[1] <= btnQuit['coords']['BL'][1]:
				debug("Found quit button")
				is_running = False
			elif btnShuffle['coords']['TL'][0] <= mouse[0] <= btnShuffle['coords']['TR'][0] and \
			btnShuffle['coords']['TL'][1] <= mouse[1] <= btnShuffle['coords']['BL'][1]:
				debug("Found shuffle button")
				deck = shuffledeck()
			elif btnNewGame['coords']['TL'][0] <= mouse[0] <= btnNewGame['coords']['TR'][0] and \
			btnNewGame['coords']['TL'][1] <= mouse[1] <= btnNewGame['coords']['BL'][1]:
				debug("Found new game button")
			else:
				debug("nothing")
		if shuffled and not dealt:
		# 	debug("build AH")
			buildgame()
	pygame.display.flip()
pygame.quit()