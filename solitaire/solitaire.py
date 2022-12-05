import pygame
pygame.init()

doDebug = True
is_running = True

WIDTH = 1024
HEIGHT = 768
BLACK=(0,0,0)
WHITE=(255,255,255)
GRAY=(127,127,127)
RED=(255,0,0)
DARKGREEN=(20,120,74)

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
SCREEN.fill(DARKGREEN)
pygame.display.set_caption('Solitaire 0P')
pygame.display.flip()
gamefont = pygame.font.SysFont('Corbel',25)

def debug(msg):
    if doDebug: print(msg)

def shuffle():
	debug("shfuffufuufle")

def newgame():
	debug("newgame")

def endgame():
	debug("endgame")

def buildButton(lx,ly,sx,sy,txt):
	'''
	TL	px,		py
	TR	px+sx	py+sy
	BL	px,		py+sy
	BR	px+sx	py+sy
	LBL	px+TLx,	py+TLy
	'''
	location = (lx,ly)
	padding = (10,10)
	size = (sx,sy)
	labeloffset = (10,10)
	coords = {
		"TL": (location[0]+padding[0]         , location[1]+padding[1]),
		"TR": (location[0]+padding[0]+size[0] , location[1]+padding[1]+size[1]),
		"BL": (location[0]+padding[0]         , location[1]+padding[1]+size[1]),
		"BR": (location[0]+padding[0]+size[0] , location[1]+padding[1]+size[1]),
	}
	lbl = (
		location[0]+padding[0]+labeloffset[0],
		location[1]+padding[1]+labeloffset[1]
	)

	text = gamefont.render(txt,True,WHITE)
	out = {
		"location": location,
		"size": size,
		"padding": padding,
		"text": text,
		"coords": coords,
		"label": lbl
	}
	return out

while is_running:
	mouse = pygame.mouse.get_pos()
	btnQuit = buildButton(0,0,90,40,"Quit") # Each button's TL is next to the previous TR
	btnShuffle = buildButton(btnQuit["coords"]["TR"][0],0,90,40,"Shuffle")
	btnNewGame = buildButton(btnShuffle["coords"]["TR"][0],0,140,40,"New Game") # new game
	for button in (btnQuit, btnShuffle, btnNewGame):
		pygame.draw.rect(
			SCREEN,
			GRAY,
			(button["coords"]["TL"],button["size"])
		)
		SCREEN.blit(button["text"],button['label'])

	for event in pygame.event.get():
		debug(event)
		if event.type == pygame.QUIT:
			is_running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			debug("mouseclick"+ str(mouse))
			#TODO: compare mouse[0] and mouse[1] to each button's coords - return that button's name and fire the function
	pygame.display.flip()
pygame.quit()