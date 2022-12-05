import pygame

pygame.font.init()
pygame.font.get_init()

doDrawBox = False
doDebug = True
screensize = 1024,768

BLACK = (0, 0, 0)        # 
WHITE = (255,255,255)    # 
GRAY = (127, 127, 127)   # 
YELLOW = (255, 255, 0)   # 
RED = (255, 0, 0)        # 
BLUE = (0, 0, 255)       # 
GREEN = (0, 255, 0)      # 
ORANGE = (255, 127, 0)   # 
DARKGREEN = (20, 120, 74)#
background = DARKGREEN

cardsize = {"h":64, "w":89, "v":16} # width, height, vertical offset
cardfont = (None, 12)
cardvalues = {
	"A": 1,	"2": 2,	"3": 3,	"4": 4,	"5": 5,
	"6": 6,	"7": 7,	"8": 8,	"9": 9,	"10": 10,
	"J": 11,"Q": 12, "K": 13
}
cardsuits = {
	"red": ("hearts","diamonds"),
	"black": ("clubs","spades")
}

def debug(msg):
    if doDebug: print(msg)

# Let's go
def main():
	pygame.init()
	screen = pygame.display.set_mode(screensize)
	screen.fill(background)

	running = True
	# debug("what now")
	while running:
		pygame.time.Clock().tick(15) # slow down
		mouse = pygame.mouse.get_pos()
		smallfont = pygame.font.SysFont('Corbel',25)

		px = 10
		py = 10
		bx = 90
		by = 40

		btnQuit= {
			"text": smallfont.render("Quit",True,WHITE),
			"location": (px,py),
			"area": (bx,by)
		}
		btnQuitCoords = (
			btnQuit["location"][0],
			btnQuit["location"][0] + btnQuit["area"][0],
			btnQuit["location"][1],
			btnQuit["location"][1] + btnQuit["area"][1]
		)
		pygame.draw.rect(screen,GRAY,[btnQuit["location"]])
		screen.blit(btnQuit["text"],btnQuit["area"])

#####################
		btnShuffle = (smallfont.render("Shuffle", True, WHITE),
			[(2*px+bx,py),(bx,by)],
			[(3*px+bx,2*py),(bx,by)]
		)
		pygame.draw.rect(screen,GRAY,btnShuffle[1])
		screen.blit(btnShuffle[0],btnShuffle[2])
#####################

		btnDeal = (smallfont.render("Deal", True, WHITE),
			[(3*px+2*bx,py),(bx,by)],
			[(4*px+2*bx,2*py),(bx,by)]
		)
		pygame.draw.rect(screen,GRAY,btnDeal[1])
		screen.blit(btnDeal[0],btnDeal[2])

		pygame.display.flip()
		for event in pygame.event.get():
			debug(event)
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				debug("mouseclick"+ str(mouse))
				if btnQuitCoords[0] <= mouse[0] <= btnQuitCoords[1] and btnQuitCoords[3] <= mouse[1] <= btnQuitCoords[4]:
					debug("FOUND QUIT BUTTON")
	pygame.quit()

def shuffle():
	debug("shfuffufuufle")

def deal():
	debug("deal")

def endgame():
	debug("endgame")

if __name__ == "__main__":
	main()