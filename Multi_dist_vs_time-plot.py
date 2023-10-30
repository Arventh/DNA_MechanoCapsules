#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:32:26 2020

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
ax = fig.add_subplot(111)
ax.set(title='Distances vs Time',ylabel='Distance (nm)',xlabel='Time (ns)')
ax.set(xlim=[0,1100],ylim=[-1,60])
patch = mpatches.Patch()
lw = 0.4
plt.plot(time, z[0,:].tolist(), linewidth=lw, alpha = 0.4, color='b', label='Tz edge 1')
plt.plot(time, z[1,:].tolist(), linewidth=lw, alpha = 0.4, color='#00BFFF', label='Tz edge 2')
plt.plot(time, z[2,:].tolist(), linewidth=lw, alpha = 0.4, color='#00FFFF', label='Tz edge 3')
plt.plot(time, z[3,:].tolist(), linewidth=lw, alpha = 0.4, color='#40E0D0', label='Tz edge 4')
plt.plot(time, z[4,:].tolist(), linewidth=lw, alpha = 0.4, color='r', label='cRGD edge 1')
plt.plot(time, z[5,:].tolist(), linewidth=lw, alpha = 0.4, color='#FF4500', label='cRGD edge 2')
plt.plot(time, z[6,:].tolist(), linewidth=lw, alpha = 0.4, color='#FF1493', label='cRGD edge 3')

ax.legend(loc=2, prop={'size': 8})
plt.savefig('Distance vs Time for ' + txt + '.svg', transparent=True)
plt.show()
data.close()
