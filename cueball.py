import pygame, math

class Cueball:
    def __init__(self, xpos, ypos, radius, friction, width, height, surface, color):
        self.xpos = xpos
        self.ypos = ypos
        self.radius = radius
        self.friction = friction
        self.xvel = 0
        self.yvel = 0
        self.xaccel = 0
        self.yaccel = 0

        # width and height of the pool table
        self.width = width
        self.height = height

        # stuff needed to blit
        self.surface = surface
        self.color = color
        
    def is_moving(self):
        return self.xvel != 0 or self.yvel != 0
    
    def shoot(self, targetx, targety):
        self.xvel = 2 * (self.xpos - targetx)
        self.yvel = 2 * (self.ypos - targety)
        
    def update(self):
        pygame.draw.circle(self.surface, self.color, (self.xpos, self.ypos), self.radius)
        # ball is stationary
        if abs(self.xvel) < 1 and abs(self.yvel) < 1:
            self.xvel = 0
            self.yvel = 0
            return
        
        # ball is translating, slow it down via acceleration
        self.xpos += 0.01 * self.xvel
        self.ypos += 0.01 * self.yvel
        norm = math.hypot(self.xvel, self.yvel)
        self.xaccel = self.friction * self.xvel / norm
        self.yaccel = self.friction * self.yvel / norm
        self.xvel -= self.xaccel
        self.yvel -= self.yaccel

        # ball espies rail
        if self.ypos <= self.height/2 - 215 + self.radius or self.ypos >= self.height/2 + 217 - self.radius:
            # hits top or bottom rail
            self.yvel *= -1
        if self.xpos <= self.width/2 - 470 + self.radius or self.xpos >= self.width/2 + 470 - self.radius:
            # hits left or right rail
            self.xvel *= -1
