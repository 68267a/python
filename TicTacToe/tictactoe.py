import pygame

pygame.font.init()
pygame.font.get_init()
pygame.time.Clock().tick(30)

screensize = 320,320
width, height = screensize

BLACK = (0, 0, 0)       # Background
WHITE = (255,255,255)
GRAY = (127, 127, 127)	# Boxes
YELLOW = (255, 255, 0)  # Board
RED = (255, 0, 0)       # X
BLUE = (0, 0, 255)      # O
GREEN = (0, 255, 0)     # Win

boxsize = 100,100
boxes = [[0,0],#dummy box
	[5,5],[110,5],[215,5],
	[5,110],[110,110],[215,110],
	[5,215],[110,215],[215,215]
]
boardlines = [
	[[106,0],[106,320]],
	[[211,0],[211,320]],
	[[0,107],[320,107]],
	[[0,212],[320,212]]
]
solutions = [
	[1,2,3],[4,5,6],[7,8,9], #horizontals
	[1,4,7],[2,5,8],[3,6,9], #verticals
	[1,5,9],[7,5,3]          #diagonals
]

p1 = ["p1","X",RED]
p2 = ["p2","O",BLUE]
turn = False
player = p1
moves = {"p1":[],"p2":[]}

def draw(p,m,b):
	#player, move, box
	print("drawing "+str(m)+
	" in box "+str(b)+
	" "+str(boxes[int(b)])+
	" for "+str(p))
	font = pygame.font.Font(None, 125)
	text = font.render(player[1], True, player[2])
	textRect = text.get_rect()
	# textRect.center = boxes[int(b)]
	textRect.center = (
		int(boxes[int(b)][0] + boxsize[0]/2),
		int(boxes[int(b)][1] + boxsize[1]/2)
	)
	screen.blit(text,textRect)
	pygame.display.flip()
	
def winner():
	for p in moves:
		for solution in solutions:
			if (str(solution[0]) in moves[p] and str(solution[1]) in moves[p] and str(solution[2]) in moves[p]):
				print("match")
				print(solution)
				print(moves[p])
				print("WIN!")
				endgame()

def endgame():
	gameover = True
	print("Game over. Press 0 to exit.")
	if pygame.event.wait().unicode == '0':
		running = False
	print("die")

pygame.init()
screen = pygame.display.set_mode(screensize)
running = True

screen.fill(BLACK)
for box in boxes:
	if box != [0,0]: pygame.draw.rect(screen, GRAY, (box, boxsize), 5)
for line in boardlines:
	# boardline1 = [106,0],[106,320]
	pygame.draw.line(screen, YELLOW, line[0], line[1], width=5)

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if len(moves) < 9 and event.type == pygame.KEYDOWN:
			print(str(player[0]) + " has pressed key " + str(event.unicode) + ". ", end='')
			if int(event.unicode) in range(1,10) and event.unicode not in moves["p1"]+moves["p2"]:
				print("valid selection.")
				moves[player[0]].append(event.unicode)
				# player.append(event.unicode)
				draw(player[0],player[1],event.unicode)
				turn = True
				# print("End of turn.")
			else:
				print("invalid selection.")
			print("moves: "+str(moves))
			print("p1: "+str(p1))
			print("p2: "+str(p2))
			if turn:
				if player == p1: player = p2
				else: player = p1
				turn = False
			print(str(9 - len(moves)) + " moves left")
			winner()
		if len(moves["p1"])+len(moves["p2"]) == 9: 
			endgame()

	pygame.display.set_caption(player[0] + "'s turn")
	pygame.display.flip()
pygame.quit()

