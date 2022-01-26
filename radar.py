import math

class Radar :

    def __init__(self,particles_array,box_width,box_height) -> None:
        self.particles_array = particles_array
        self.box_width = box_width
        self.box_height = box_height

    def check4collision(self,pos,radius,_particle) :

        if pos[0] + radius >= self.box_width or pos[0] - radius <= 0 : return 'w'
        if pos[1] + radius >= self.box_height or pos[1] - radius <= 0: return 'f'

        for particle in self.particles_array :
            if (particle != _particle) and  (math.sqrt((pos[0]-particle.position[0])**2 + (pos[1]-particle.position[1])**2) <= particle.radius + radius) : return particle

        return None