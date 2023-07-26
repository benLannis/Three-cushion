import pygame, math

pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width, height))
applegreen = (141, 182, 0)
white = (0, 0, 0)

class Cueball:
    def __init__(self, xpos, ypos, radius, friction):
        self.xpos = xpos
        self.ypos = ypos
        self.radius = radius
        self.friction = friction
        self.xvel = 0
        self.yvel = 0
        self.xaccel = 0
        self.yaccel = 0
    def ismoving(self):
        return self.xvel != 0 and self.yvel != 0
    def shoot(self, targetx, targety):
        if self.ismoving:
            # we don't want to allow shooting the cue ball while it's still in motion
            return
        self.xvel = targetx - self.xpos
        self.yvel = targety - self.ypos
    def update(self):
        pygame.draw.circle(screen, white, (self.xpos, self.ypos), self.radius)
        if abs(self.xvel) < 0.2 and abs(self.yvel) < 0.2:
            self.xvel = 0
            self.yvel = 0
            return
        self.xpos += self.xvel
        self.ypos += self.yvel
        norm = math.sqrt(self.xvel * self.xvel + self.yvel * self.yvel)
        self.xaccel = self.friction * self.xvel / norm
        self.yaccel = self.friction * self.yvel / norm
        self.xvel -= self.xaccel
        self.yvel -= self.yaccel

# global variables
cueball = Cueball(50, 50, 10, 0.2)

running = True
while running:
    screen.fill(applegreen)
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
