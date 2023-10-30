#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:24:08 2020
@author: arventh
"""
import matplotlib.pyplot as plt
import os
print('Program plots no. of Hydrogen bonds as the string force increses over time')
folder = raw_input("Enter directory:")
txt = raw_input("Enter filename:")
F0 = input("Force_initial :") #units in  pN
F_rate = input("Force_rate :") # rate of increase force (simulation units) per simulation step 
dt = 0.005 # simulation time units
#MD units = steps * dt

os.chdir(folder)
data = open(txt, 'r')
x, y, z = [],[],[]
i = 0
F_units = 48.63 #units in pN 

fig = plt.figure()       # size in inches
ax = fig.add_subplot(1,1,1)
for line in data:
    z = line.split()
    force = (F0 + ((float(z[0])/dt) * F_rate))*F_units
    x.append(force)
    y.append(float(z[2]))
    if float(z[2]) == 0 and i < 10:
        print force
        i=i+1
        
plt.plot(x,y)
plt.show()
data.close()