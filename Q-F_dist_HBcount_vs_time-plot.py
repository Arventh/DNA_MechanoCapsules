#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 02:35:49 2020

@author: arventh
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os
import numpy
folder = '/home/arventh/Data/oxDNAdata/TO-TD1/6-5_TD_force'#raw_input("Enter directory:")
txt = '6-5-0_out_Observables_4_distances_list.dat'#raw_input("Enter Observables output file:")
dt = 0.005 # simulation time units 
L_units = 0.8518 #units in nm 
t_units = 3.03e-12 #picoseconds

os.chdir(folder)
data = open(txt, 'r')
time, z = [],[]
t = 0

for line in data: # print every 1e4 steps
    x = [float(dist) for dist in line.split()]
    z.append(x)
    t = t + (dt*1e4*t_units)*1e9 # add time elapsed in nanoseconds every 1e4 steps
    time.append(t)
z = numpy.transpose(z)

fig = plt.figure(5)       # size in inches
ax1 = fig.add_subplot(111)
ax1.set(title='Distances vs Time',ylabel='BHQ2-Cy3B distance (nm)',xlabel='Time (ns)')
ax1.set(xlim=[0,1100],ylim=[-1,30])
patch = mpatches.Patch()
lw = 0.4
plt.plot(time, z[9,:].tolist(), linewidth=lw, alpha = 0.8, color='#FF6347', label='Cy3B-BHQ2 distance')
ax1.tick_params(axis='y', labelcolor='#FF6347')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.set_ylabel('Hydrogen bonds', color='#2F4F4F')  
ax2.set(ylim=[40,120])
ax2.plot(time, z[7,:].tolist(), linewidth=lw, alpha = 0.3, color='#2F4F4F', label='cRGD edge 3')
ax2.tick_params(axis='y', labelcolor='#2F4F4F')
      
plt.savefig('Q-F distances with hbcount for' + txt + '.svg', transparent=True)
plt.show()
data.close()