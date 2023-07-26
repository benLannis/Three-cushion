import pygame, math
from cueball import Cueball

pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width, height))
applegreen = (0, 150, 255)
white = (0, 0, 0)
self.yvel -= self.yaccel

# global variables
cueball = Cueball(50, 50, 10, 0.7)

running = True
while running:
    screen.fill(applegreen)
    pygame.draw.circle(screen, white, (cueball.xpos, cueball.ypos), cueball.radius)
    cueball.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Events will include what button was pushed, which you can check in if statements
            if event.button == pygame.BUTTON_LEFT:
                print("pressed")
                x, y = pygame.mouse.get_pos()
                cueball.shoot(x, y)

    pygame.display.update()

pygame.quit()
