from matrix import Matrix
import os
import csv
import pathlib
import time

scene = Matrix(71,71,values=' ')

positions = []
balls = []

with open(str(pathlib.Path(__file__).parent.resolve()) + '/output.csv', 'r') as data :

    reader = list(csv.reader(data))
    Tto = float(reader[0][0])
    dt = float(reader[0][1])
    box_width = float(reader[0][2])
    box_height = float(reader[0][3])                             

    for index in range(1,len(reader)-1) :

        reader[index].pop(0)

        for i in range(len(reader[index])) : 
            reader[index][i] = reader[index][i].split()
            for coord_index in range(2) : reader[index][i][coord_index] = float(reader[index][i][coord_index])


        positions.append(reader[index])

while True :

    FRAME_RATE = 30
    DT = 1/FRAME_RATE

    coeff = DT/dt
    coeff_ = scene.width/box_width
    ln = len(positions)
    inst_index = 0
    s = time.time()
    begin = s
    frame = 0

    while frame < ln - 1:

        if time.time() >= s + DT :

            s = time.time()

            frame = int(inst_index*coeff)

            scene.clear(value=' ')
            scene.encadre(0,0,'#','#')
            scene.print(5,64,str(round(100*frame/ln,1))+' % | time : '+str(round(s-begin,1))+'/'+str(Tto),color='green')

            if frame >= len(positions) : frame = len(positions)-1

            particles_coordinates = positions[frame]

            for coords_index in range(len(positions[0])) :

                coordx = int(particles_coordinates[coords_index][0]*coeff_)
                coordy = int(particles_coordinates[coords_index][1]*coeff_)+1
                scene.setCase(coordx,coordy,'●')

            os.system('clear')
            scene.display()

            inst_index += 1