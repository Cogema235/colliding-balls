import csv
import time
import vpython as v
import pathlib

positions = []
balls = []

with open(str(pathlib.Path(__file__).parent.resolve()) + '/output.csv', 'r') as data :

    reader = list(csv.reader(data))

    ###################### EXTRACT ANIMATION INFORAMATIONS ######################

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

    ###################### CREATES THE REPRESENTATIONS OF THE PARTICLES ######################

    for index in range(4,len(reader[0])) : 

        balls.append(v.sphere(pos=v.vector(float(positions[0][index-4][0]),float(positions[0][index-4][1]),0), radius=float(reader[0][index])))  

    ##########################################################################################
    ################################################################################


###################### ANIMATION LOOP ######################

FRAME_RATE = 60
DT = 1/FRAME_RATE

coeff = DT/dt

while True : 

    for inst_index in range(len(positions)) : 
        frame = int(inst_index*coeff)
        if frame >= len(positions) : frame = len(positions)-1

        particles_coordinates = positions[frame]

        for coords_index in range(len(balls)) :

            coordx = particles_coordinates[coords_index][0]
            coordy = particles_coordinates[coords_index][1]
            balls[coords_index].pos=v.vector(coordx,coordy,0)

        time.sleep(DT/5)