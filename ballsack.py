import math

class Ballsack:
    def __init__(self, balls):
        # balls : Cueball list
        self.balls = balls
        # assume self.balls[0] is the cueball
    def all_balls_stationary(self):
        for ball in self.balls:
            if ball.is_moving():
                return False
        return True
    def shoot_cue(self, targetx, targety):
        if not self.all_balls_stationary():
            # don't allow shooting until all balls are done moving
            return
        self.balls[0].shoot(targetx, targety)
    def collision_helper(self, vx, vy, px, py):
        v0 = math.hypot(vx, vy)
        vb_len = math.hypot(px, py)
        dot = vx * px + vy * py
        cos =  dot/(v0 * vb_len)
        sin = math.sqrt(1 - cos * cos)
        vbx_hat = px/vb_len
        vby_hat = py/vb_len
        proj_x = dot/vb_len * vbx_hat
        proj_y = dot/vb_len * vby_hat
        vax = vx - proj_x
        vay = vy - proj_y
        s = math.hypot(vax, vay)
        vax_hat = vax/s
        vay_hat = vay/s
        #return v0 * sin * vax_hat, v0 * sin * vay_hat, v0 * cos * vbx_hat, v0 * cos * vby_hat
        # phenomenological follow
        followx = 100 * px / vb_len
        followy = 100 * py / vb_len
        
        #'''
        return (v0 * sin * vax_hat + followx,
                v0 * sin * vay_hat + followy,
                v0 * cos * vbx_hat + followx,
                v0 * cos * vby_hat + followy)
        #'''
        
    def resolve_collision(self, A, B):
        # assert math.hypot(A.xpos - B.xpos, A.ypos - B.ypos) <= A.radius + B.radius
        vap_x, vap_y, vbp_x, vbp_y = self.collision_helper(A.xvel-B.xvel, A.yvel-B.yvel, B.xpos-A.xpos, B.ypos-A.ypos)
        return vap_x + B.xvel, vap_y + B.yvel, vbp_x + B.xvel, vbp_y + B.yvel
        
    def update(self):
        # check for collisions between all possible pairs of balls and resolve them
        for i in range(len(self.balls)):
            for j in range(i+1, len(self.balls)):
                if math.hypot(self.balls[i].xpos - self.balls[j].xpos,
                              self.balls[i].ypos - self.balls[j].ypos) <= self.balls[i].radius + self.balls[j].radius:
                    self.balls[i].xvel, self.balls[i].yvel, self.balls[j].xvel, self.balls[j].yvel = self.resolve_collision(self.balls[i], self.balls[j])
        for ball in self.balls:
            ball.update()
