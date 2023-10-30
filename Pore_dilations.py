#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 02:39:13 2022

@author: arventh
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os
import math
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Segoe UI']

folder = '/home/arventh/Documents/oxDNAdata/AV/TO-TD7/3-6_TD_force_design03' #raw_input directory
txt = '3-6_out_trajectory.dat'
os.chdir(folder)
data = open(txt, 'r')

dt = 0.005 #simulation time units (Output has time in MD units where MD units = steps * dt)
F_units = 48.63 #units in pN 
l_units = 0.8518 #units in nm 
t_units = 3.03e-12 #seconds
set1 = np.array([241, 220, 71])
set2 = np.array([71, 113, 92])
set3 = np.array([28, 7, 49])
set4 = np.array([199, 178, 157])
tri1, tri2, tri3, tri4 = [],[],[],[]
x, y1, y2, y3, y4 = [],[],[],[],[]


#functions
def length(i,j):
    dist = math.sqrt((i[0]-j[0])**2 + (i[1]-j[1])**2 + (i[2]-j[2])**2)
    return dist

def incircle(pts):
    a = length(pts[0:3],pts[3:6])
    b = length(pts[6:9],pts[3:6])
    c = length(pts[6:9],pts[0:3])
    Perimeter = a+b+c
    p = Perimeter/2
    Area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    r = l_units*(2*Area)/Perimeter #https://brilliant.org/wiki/inscribed-triangles/
    return(r)

n = -3
for line in data:
    if n == -3:
        t = line.strip('t= \n')
        time = float(t)*dt*t_units*1e6 #time elapsed in microseconds
        x.append(time)
    n += 1
    if n in set1:
        Tri = np.array(line.split(), dtype=float)
        tri1.extend(Tri[0:3])
    if n in set2:
        Tri = np.array(line.split(), dtype=float)
        tri2.extend(Tri[0:3])
    if n in set3:
        Tri = np.array(line.split(), dtype=float)
        tri3.extend(Tri[0:3])
    if n in set4:
        Tri = np.array(line.split(), dtype=float)
        tri4.extend(Tri[0:3])
    if n == 252:
        y1.append(incircle(tri1))
        y2.append(incircle(tri2))
        y3.append(incircle(tri3))
        y4.append(incircle(tri4))
        #print (x, y1, y2, y3, y4)
        tri1, tri2, tri3, tri4 = [],[],[],[]
        n = -3

fig = plt.figure(5)       # size in inches
ax1 = fig.add_subplot(111)
ax1.set(title='Distances vs Time',ylabel='Distance (nm)',xlabel='Time (us)')
ax1.set(xlim=[0,12],ylim=[1,4])
plt.axhline(y=2.6, color="#aaaaaa", linestyle="--")

lw = 0.4
plt.plot(x, y1, linewidth=lw, alpha = 0.4, color='#00BFFF', label='Pore 1')
plt.plot(x, y2, linewidth=lw, alpha = 0.4, color='#00BFFF', label='Pore 2')
plt.plot(x, y3, linewidth=lw, alpha = 0.4, color='#00BFFF', label='Pore 3')
plt.plot(x, y4, linewidth=lw, alpha = 0.4, color='#00BFFF', label='Pore 4')

plt.savefig('Pore sizes vs Time for' + txt + '.svg', transparent=True)
plt.show()

for oolala in range(len(x)):
    csv = open("Pore_dilations_graph_plot.csv", "a")
    csv.write(str(x[oolala]) + ',' + str(y1[oolala]) + ',' + str(y2[oolala]) + ',' + str(y3[oolala]) + ',' + str(y4[oolala]) + '\n')

csv.close()
data.close()





