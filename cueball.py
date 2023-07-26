import pygame, math

class Cueball:
    def __init__(self, xpos, ypos, radius, friction, width, height):
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
        
    def ismoving(self):
        return self.xvel != 0 or self.yvel != 0
    
    def shoot(self, targetx, targety):
        if self.ismoving():
            # we don't want to allow shooting the cue ball while it's still in motion
            print(self.xvel, self.yvel)
            print("ok")
            return
        self.xvel = targetx - self.xpos
        self.yvel = targety - self.ypos
        print(self.xvel, self.yvel)
        
    def update(self):
        if abs(self.xvel) < 0.5 and abs(self.yvel) < 0.5:
            self.xvel = 0
            self.yvel = 0
            return
        
        # slow down the ball via acceleration
        self.xpos += 0.01 * self.xvel
        self.ypos += 0.01 * self.yvel
        norm = math.sqrt(self.xvel * self.xvel + self.yvel * self.yvel)
        self.xaccel = self.friction * self.xvel / norm
        self.yaccel = self.friction * self.yvel / norm
        self.xvel -= self.xaccel
        self.yvel -= self.yaccel

        # what to do when ball espies rail
        if self.ypos <= self.radius or self.ypos >= self.height - self.radius:
            # hits top or bottom rail
            self.yvel *= -1
        if self.xpos <= self.radius or self.xpos >= self.width - self.radius:
            # hits left or right rail
            self.xvel *= -1