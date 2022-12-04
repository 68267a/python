import pygame

pygame.font.init()
pygame.font.get_init()

doDrawBox = False
doDebug = True
screensize = 540,540
width, height = screensize

BLACK = (0, 0, 0)        # 
WHITE = (255,255,255)    # 
GRAY = (127, 127, 127)   # 
YELLOW = (255, 255, 0)   # 
RED = (255, 0, 0)        # 
BLUE = (0, 0, 255)       # 
GREEN = (0, 255, 0)      # 
ORANGE = (255, 127, 0)   # 
DARKGREEN = (24, 120, 74)#
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

def main():
	pygame.init()             # Let's go
	screen = pygame.display.set_mode(screensize)
	running = True
	screen.fill(background)
	debug("what now")
	while running:
		pygame.time.Clock().tick(15) # slow down
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			debug(event)
		pygame.display.flip()
	pygame.quit()



def endGame():            # end of game
    debug("Game over. Press 0 to exit.")
    # pygame.event.clear() # I think there's a way to buffer overflow event and crash
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.unicode == '0':
                global running
                running = False
                return


if __name__ == "__main__":
	main()