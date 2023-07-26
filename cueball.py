import pygame, math

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
        return self.xvel != 0 or self.yvel != 0
    def shoot(self, targetx, targety):
        if self.ismoving():
            # we don't want to allow shooting the cue ball while it's still in motion
            return
        self.xvel = targetx - self.xpos
        self.yvel = targety - self.ypos
        print(self.xvel, self.yvel)
    def update(self):
        if abs(self.xvel) < 0.2 and abs(self.yvel) < 0.2:
            self.xvel = 0
            self.yvel = 0
            return
        self.xpos += 0.01 * self.xvel
        self.ypos += 0.01 * self.yvel
        norm = math.sqrt(self.xvel * self.xvel + self.yvel * self.yvel)
        self.xaccel = self.friction * self.xvel / norm
        self.yaccel = self.friction * self.yvel / norm
        self.xvel -= self.xaccel
        self.yvel -= self.yaccel
