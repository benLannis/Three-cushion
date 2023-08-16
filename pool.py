import pygame, math
from cueball import Cueball
from cue import Cue
from ballsack import Ballsack

pygame.init()

FPS = 60
clock = pygame.time.Clock()

width = 1200
height = 700

screen = pygame.display.set_mode((width, height))
felt_blue = (0, 150, 255)
black = (0, 0, 0) 
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 215, 0)

# global variables
whiteball = Cueball(width/2 + 230, height/2 - 51, 10, 2, width, height, screen, white)
redball = Cueball(width/2 - 230, height/2, 10, 2, width, height, screen, red)
yellowball = Cueball(width/2 + 230, height/2, 10, 2, width, height, screen, yellow)
bs = Ballsack([whiteball, redball, yellowball])
cue = Cue(whiteball.xpos, whiteball.ypos, 0)

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
    if bs.all_balls_stationary():
        #compute cue attributes
        x, y = pygame.mouse.get_pos()
        vector1 = [x - whiteball.xpos, y - whiteball.ypos]
        vector2 = [1, 0]
        dot = vector1[0] * vector2[0] + vector1[1] * vector2[1]
        magnitude = (math.sqrt(vector1[0] * vector1[0] + vector1[1] * vector1[1])) * (math.sqrt(vector2[0] * vector2[0] + vector2[1] * vector2[1]))
        if y >= whiteball.ypos:
            cue.angle = math.acos(dot/magnitude)
        else:
            cue.angle = -math.acos(dot/magnitude)
        points = [(whiteball.xpos + 20, whiteball.ypos - 4), (whiteball.xpos + 20, whiteball.ypos + 4), (whiteball.xpos + 450, whiteball.ypos + 4), (whiteball.xpos + 450, whiteball.ypos - 4)]
        #draw the cue
        #translate vectors back to the origin
        for i in range(len(points)):
            points[i] = ((points[i][0] - whiteball.xpos), (points[i][1] - whiteball.ypos))
        #apply rotation matrix
        for i in range(len(points)):
            points[i] = ((points[i][0] * math.cos(cue.angle) - points[i][1] * math.sin(cue.angle)), (points[i][0] * math.sin(cue.angle) + points[i][1] * math.cos(cue.angle)))
        #translate vectors back to original position
        for i in range(len(points)):
            points[i] = ((points[i][0] + whiteball.xpos), (points[i][1] + whiteball.ypos))
        pygame.draw.polygon(screen, black, points)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Events will include what button was pushed, which you can check in if statements
            if event.button == pygame.BUTTON_LEFT:
                x, y = pygame.mouse.get_pos()
                bs.shoot_cue(x, y)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
