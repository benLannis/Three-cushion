import pygame, math
from cueball import Cueball

pygame.init()

width = 1200
height = 700

screen = pygame.display.set_mode((width, height))
applegreen = (0, 150, 255)
black = (0, 0, 0) 
white = (255, 255, 255)

# global variables
cueball = Cueball(width/2, height/2, 10, 1.3, width, height)

running = True
while running:
    screen.fill(applegreen)
    pygame.draw.circle(screen, white, (cueball.xpos, cueball.ypos), cueball.radius)
    #pygame.draw.rect(screen, black, pygame.Rect(30, 30, 60, 60),  2)
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
