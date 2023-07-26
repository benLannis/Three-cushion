import pygame, math
from cueball import Cueball
from target import Target

pygame.init()

width = 1200
height = 700

screen = pygame.display.set_mode((width, height))
felt_blue = (0, 150, 255)
black = (0, 0, 0) 
white = (255, 255, 255)
red = (255, 0, 0)

# global variables
cueball = Cueball(width/2, height/2, 10, 1.3, width, height)
target = Target(width/2, height/2, 10, 3)

running = True
while running:
    screen.fill(white)
    pygame.draw.rect(screen, felt_blue, pygame.Rect(width/2 - 500, height/2 - 250, 1000, 500))
    pygame.draw.circle(screen, white, (cueball.xpos, cueball.ypos), cueball.radius)
    pygame.draw.rect(screen, black, pygame.Rect(width/2 - 500, height/2 - 250, 1000, 500),  10)
    cueball.update()
    x, y = pygame.mouse.get_pos()
    target.xpos = x
    target.ypos = y
    #draw target
    pygame.draw.circle(screen, red, (target.xpos, target.ypos), target.outradius)
    pygame.draw.circle(screen, felt_blue, (target.xpos, target.ypos), target.outradius - 2)
    pygame.draw.circle(screen, red, (target.xpos, target.ypos), target.inradius)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Events will include what button was pushed, which you can check in if statements
            if event.button == pygame.BUTTON_LEFT:
                x, y = pygame.mouse.get_pos()
                cueball.shoot(x, y)
    pygame.display.update()

pygame.quit()
