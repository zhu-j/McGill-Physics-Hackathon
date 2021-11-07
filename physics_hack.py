#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 20:27:27 2021

"""

import numpy as np
import matplotlib.pyplot as plt

# set up blank 3D graph to plot points in
ax = plt.subplot(projection='3d')
ax.set_xlabel('Distance')
ax.set_ylabel('Width')
ax.set_zlabel('Height')

# set parameters
time_steps = 7200 # 2 hour air suspension
num_simulation = 1000 #number of aribone virus
distance = 100 # distance separating transmittor and bystander
height = 150 # height of average person's head

person_contact = 0 #variable for number of times virus reaches person


# loop through 1000 molecules
for i in range (0, num_simulation+1):
		# set initial x,y,z coordinates to be the origin
    x = 0
    y = 0
    z = 0
    
    # create array of zeros to plot movement of particle later
    x_plot = np.zeros(time_steps)
    y_plot = np.zeros(time_steps)
    z_plot = np.zeros(time_steps)
    
    index = 0
    
    #steps taken by one airborne virus
    #random walk model of brownian motion
    while index < time_steps:
          if abs(x) < distance and abs(y) < distance and abs(z) < height:
              # choose a random x-direction for the molecule to move in
              x_direction = np.random.randint(-1,2)
              if x_direction == -1:
                  x += -1
                  x_plot[index] = x
              elif x_direction == 0: 
                  x += 0
                  x_plot[index] = x
              else:
                  x += 1
                  x_plot[index] = x
        
        			# choose a random y-direction for the molecule to move in
              y_direction = np.random.randint(-1,2)
              if y_direction == -1:
                  y += -1
                  y_plot[index] = y
              elif y_direction == 0:
                  y += 0
                  y_plot[index] = y
              else:
                  y += 1
                  y_plot[index] = y
        
        			# choose a random z-direction for the molecule to move in
              z_direction = np.random.randint(-1,2)
              if z_direction == -1:
                  z += -1
                  z_plot[index] = z
              elif z_direction== 0:
                  z += 0
                  z_plot[index] = z
              else:
                  z += 1
                  z_plot[index] = z
          # if the airborne virus reaches the person, will
          else:  
              person_contact += 1
              break
          index += 1

    
    # plot the path of a single molecule
    # will overlay when iterating the loop
    ax.plot(x_plot,y_plot,z_plot)
    

    
    i+=1

plt.show()
        
print("Number of particles in contact with person: " , person_contact)
print("Probability of an airborne virus reaching a person: ", (person_contact/
num_simulation)*100)

