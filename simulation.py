from box import Box
from particle import Particle
import os
import pathlib
import csv
import random

box = Box(70,70,gravity=(0,-20))

radius = 0.5

for x in range(30,box.width-30,1) :
    for y in range(0,box.heigth-30,1) :

        box.addParticle(Particle(x,y+0.5,random.randint(-1,1),random.randint(-1,1),1,radius))

Tt = 10

dt = 0.01

output_path = str(pathlib.Path(__file__).parent.resolve()) + '/output.csv'

with open(output_path, 'w', newline='') as out :

    writer = csv.writer(out)

    tmp = [Tt,dt,box.width,box.heigth]
    for particule in box.particles : tmp.append(particule.radius)
    writer.writerow(tmp)

    t = 0
    while t < Tt :

        tmp =  [t]

        box.update(dt)

        for particle in box.particles : 
            tmp.append(str(particle.position[0]) + ' ' + str(particle.position[1]))

        writer.writerow(tmp)

        os.system('clear')
        print(round((t/Tt)*100,0),'%')

        t += dt

    print('simulation completed')

import consoleRender #en depit de ent