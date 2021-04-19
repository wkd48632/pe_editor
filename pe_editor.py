import pygame

pygame.init()
screen = pygame.display.set_mode([1920,1080])
pygame.display.set_caption('PE editor')

FRAME_PER_SECOND = 120
BACKGROUND_COLOR = (204,204,204)

def render_screen():
	screen.fill(BACKGROUND_COLOR);
	

done = False
clock = pygame.time.Clock()
while not done:
	clock.tick( FRAME_PER_SECOND )
	for event in pygame.event.get():
		need_render = True
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			pass
		elif event.type == pygame.KEYUP:
			pass
	render_screen()
	pygame.display.flip()

pygame.quit();