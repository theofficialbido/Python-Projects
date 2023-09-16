import pygame
import os

WIDTH, HEIGHT = 900, 550
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('First Game!')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
FPS = 60
YELLOW_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
def draw():

	WIN.fill((BLACK))
	WIN.blit(YELLOW_SPACESHIP_IMG, (300, 100))
	pygame.display.update()



def main():
	run = True
	clock = pygame.time.Clock()
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				run = False
			draw()


if __name__ == '__main__':
	main()
