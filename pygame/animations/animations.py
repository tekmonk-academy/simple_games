import pygame

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
FPS = 60

rect = pygame.Rect(0, 0, 32, 32)
block = pygame.Surface((32, 32))
block.fill('orange')

dx = 5
while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    rect.centerx += dx

    if rect.topright[0] >= SCREEN_WIDTH or rect.topleft[0] <= 0:
        dx *= -1

    screen.blit(block, rect)
    screen.fill('white')

    pygame.display.update()
