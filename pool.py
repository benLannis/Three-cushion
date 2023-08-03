import pygame, math
from cueball import Cueball
from target import Target
from ballsack import Ballsack

pygame.init()

width = 1200
height = 700

screen = pygame.display.set_mode((width, height))
felt_blue = (0, 150, 255)
black = (0, 0, 0) 
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 215, 0)

clock = pygame.time.Clock()
fps = 60

# global variables
whiteball = Cueball(width/2 + 230, height/2 - 51, 10, 2, width, height, screen, white)
redball = Cueball(width/2 - 230, height/2, 10, 2, width, height, screen, red)
yellowball = Cueball(width/2 + 230, height/2, 10, 2, width, height, screen, yellow)
bs = Ballsack([whiteball, redball, yellowball])
target = Target(width/2, height/2, 10, 3)

running = True
while running:
    screen.fill(white)
    # draw table
    pygame.draw.rect(screen, felt_blue, pygame.Rect(width/2 - 500, height/2 - 250, 1000, 500))
    pygame.draw.rect(screen, black, pygame.Rect(width/2 - 500, height/2 - 250, 1000, 500), 30)
    for i in range(-460, 461, 115):
        pygame.draw.circle(screen, white, (width/2 + i, height/2 - 235), 2)
        pygame.draw.circle(screen, white, (width/2 + i, height/2 + 235), 2)
    for i in range(-204, 205, 102):
        pygame.draw.circle(screen, white, (width/2 - 485, height/2 + i), 2)
        pygame.draw.circle(screen, white, (width/2 + 485, height/2 + i), 2)
    #cueball.update()
    bs.update()
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
                bs.shoot_cue(x, y)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
