import math

class Particle :

    def __init__(self,x0,y0,Vx0,Vy0,mass,radius) -> None:

        self.position = [x0,y0]
        self.velocity = [Vx0,Vy0]
        self.mass = mass
        self.radius = radius

    def updateVelocity(self,dt,acceleration,collision) :

        self.acceleration = acceleration

        
        self.velocity[0] += self.acceleration[0]*dt
        self.velocity[1] += self.acceleration[1]*dt

        if collision == 'w' : self.velocity[0] *= -1

        if collision == 'f' : self.velocity[1] *= -1

        if type(collision) == Particle :

            AB = (collision.position[0]-self.position[0],collision.position[1]-self.position[1])

            VA = tuple(self.velocity)
            VB = tuple(collision.velocity)

            NAB = math.sqrt(AB[0]**2+AB[1]**2)

            normale = (AB[0]/NAB, AB[1]/NAB) 
            tangente = (-normale[1],normale[0])

            dpt_self = tangente[0]*VA[0] + tangente[1]*VA[1]
            dpt_touched = tangente[0]*VB[0] + tangente[1]*VB[1]

            dpn_self = normale[0]*VA[0] + normale[1]*VA[1]
            dpn_touched = normale[0]*VB[0] + normale[1]*VB[1]

            mA = (dpn_self * (self.mass - collision.mass) + 2*collision.mass*dpn_touched) / (self.mass + collision.mass)
            mB = (dpn_touched * (collision.mass - self.mass) + 2*self.mass*dpn_self) / (self.mass + collision.mass)

            self.velocity[0] = tangente[0] * dpt_self + normale[0] * mA
            self.velocity[1] = tangente[1] * dpt_self + normale[1] * mA
            collision.velocity[0] = tangente[0] * dpt_touched + normale[0] * mB
            collision.velocity[1] = tangente[1] * dpt_touched + normale[1] * mB
    
    def updatePosition(self,dt) :

        self.position[0] += self.velocity[0]*dt
        self.position[1] += self.velocity[1]*dt