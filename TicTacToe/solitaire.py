import pygame

pygame.font.init()
pygame.font.get_init()

doDrawBox = False
doDebug = True
screensize = 540,540
width, height = screensize

BLACK = (0, 0, 0)        # Background
WHITE = (255,255,255)    # Labels
GRAY = (127, 127, 127)   # Boxes
YELLOW = (255, 255, 0)   # Board
RED = (255, 0, 0)        # X
BLUE = (0, 0, 255)       # O
GREEN = (0, 255, 0)      # Win
ORANGE = (255, 127, 0)   # CAT

cardsize = 64, 89, 16    # width, height, vertical offset
cardvalues = {
	"A": 1,
	"2": 2,
	"3": 3,
	"4": 4,
	"5": 5,
	"6": 6,
	"7": 7,
	"8": 8,
	"9": 9,
	"10": 10,
	"J": 11,
	"Q": 12,
	"K": 13
}

def debug(msg):
    if doDebug: print(msg)

def main():
	pygame.init()             # Let's go
	screen = pygame.display.set_mode(screensize)
	running = True
	screen.fill(BLACK)
	debug("what now")
	while running:
		pygame.time.Clock().tick(15) # slow down
		for event in pygame.event.get():
			if event.type == pygame.quit:
				running = False

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