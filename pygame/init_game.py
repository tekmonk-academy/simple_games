import pygame

pygame.init()

screen = pygame.display.set_mode((720, 480))

icon = pygame.image.load("arrow_icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Move Around game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill("black")

    pygame.display.update()
