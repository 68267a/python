import pygame

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
box1 = 5,5
box2 = 110,5
box3 = 215,5
box4 = 5,110
box5 = 110,110
box6 = 215,110
box7 = 5,215
box8 = 110,215
box9 = 215,215
boardline1 = [106,0],[106,320]
boardline2 = [211,0],[211,320]
boardline3 = [0,107],[320,107]
boardline4 = [0,212],[320,212]

sol1 = [1,2,3]
sol2 = [4,5,6]
sol3 = [7,8,9]
sol4 = [1,4,7]
sol5 = [2,5,8]
sol6 = [3,6,9]
sol7 = [1,5,9]
sol8 = [7,5,3]

p1 = ["p1"]
p2 = ["p2"]
player = p1
moves = []
turn = False

pygame.init()
screen = pygame.display.set_mode(screensize)
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				print(player[0] + " has pressed key 1")
				if 1 not in moves:
					moves.append(1)
					player.append(1)
					turn = True
			elif event.key == pygame.K_2:
				print(player[0] + " has pressed key 2")
				if 2 not in moves:
					moves.append(2)
					player.append(2)
					turn = True
			elif event.key == pygame.K_3:
				print(player[0] + " has pressed key 3")
				if 3 not in moves:
					moves.append(3)
					player.append(3)
					turn = True
			elif event.key == pygame.K_4:
				print(player[0] + " has pressed key 4")
				if 4 not in moves:
					moves.append(4)
					player.append(4)
					turn = True
			elif event.key == pygame.K_5:
				print(player[0] + " has pressed key 5")
				if 5 not in moves:
					moves.append(5)
					player.append(5)
					turn = True
			elif event.key == pygame.K_6:
				print(player[0] + " has pressed key 6")
				if 6 not in moves:
					moves.append(6)
					player.append(6)
					turn = True
			elif event.key == pygame.K_7:
				print(player[0] + " has pressed key 7")
				if 7 not in moves:
					moves.append(7)
					player.append(7)
					turn = True
			elif event.key == pygame.K_8:
				print(player[0] + " has pressed key 8")
				if 8 not in moves:
					moves.append(8)
					player.append(8)
					turn = True
			elif event.key == pygame.K_9:
				print(player[0] + " has pressed key 9")
				if 9 not in moves:
					moves.append(9)
					player.append(9)
					turn = True

			if turn:
				if player == p1: player = p2
				else: player = p1
				turn = False
			
			if len(moves) == 9: print("Game over")
			
		
	
	screen.fill(BLACK)
	pygame.draw.rect(screen, BLACK, (box1, boxsize), 5) 
	pygame.draw.rect(screen, BLACK, (box2, boxsize), 5) 
	pygame.draw.rect(screen, BLACK, (box3, boxsize), 5) 
	pygame.draw.rect(screen, BLACK, (box4, boxsize), 5) 
	pygame.draw.rect(screen, BLACK, (box5, boxsize), 5) 
	pygame.draw.rect(screen, BLACK, (box6, boxsize), 5) 
	pygame.draw.rect(screen, BLACK, (box7, boxsize), 5) 
	pygame.draw.rect(screen, BLACK, (box8, boxsize), 5) 
	pygame.draw.rect(screen, BLACK, (box9, boxsize), 5) 
	pygame.draw.line(screen, WHITE, boardline1[0], boardline1[1], width=5)
	pygame.draw.line(screen, WHITE, boardline2[0], boardline2[1], width=5)
	pygame.draw.line(screen, WHITE, boardline3[0], boardline3[1], width=5)
	pygame.draw.line(screen, WHITE, boardline4[0], boardline4[1], width=5)
	pygame.display.set_caption(player[0] + "'s turn")
	pygame.display.update()
pygame.quit()