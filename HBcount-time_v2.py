#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 21:04:25 2021

@author: arventh
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

folder = '/home/arventh/Documents/oxDNAdata/AV/TO-TD1/5-5_TD_force'#raw_input("Enter directory:")
txt = '5-5-0_out_Observables_1.dat'#raw_input("Enter Observables output file:")
dt = 0.005 # simulation time units 
L_units = 0.8518 #units in nm 
t_units = 3.03e-12 #picoseconds
#Output has time in MD units where MD units = steps * dt
freq = 1e5 #change to hb printed every x steps

x, y, z = [],[],[] 
os.chdir(folder)
data = open(txt, 'r')
time, z = [],[]
t = 0
i,avg = 0,0

for line in data: # print every 2e4 steps
    x = [float(dist) for dist in line.split()]
    t = t + (dt*freq*t_units)*1e9 #time elapsed in microseconds
    time.append(t)
    y.append(x[2])
    if t > 2000 and i < 100: #x[2] is HB count
        avg = avg + x[2]
        i = i + 1

avg = round(avg/i)      
print(avg)


fig = plt.figure(5)       # size in inches
ax1 = fig.add_subplot(111)
ax1.set(title='',ylabel='',xlabel='time (ns)')  #'+ '$\mu s$)') 
ax1.set(xlim=[0,2000],ylim=[0,120])

patch = mpatches.Patch()
lw = 0.55
plt.plot(time, y, linewidth=lw, alpha = 1, color='#ff793f', label='')
ax1.tick_params(axis='y', labelcolor='#000000')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
plt.savefig('Hydrogen bonds_' + str(avg) +'_'+ txt.rstrip('.dat') + '.svg', transparent=True)
plt.show()

for oolala in range(len(time)):
    csv = open("HB vs time . csv", "a")
    csv.write(str(time[oolala]) + ',' + str(y[oolala]) + '\n')
    
data.close()

#2c2c54 #ff793f #227093 #34ace0 #218c74
#474787 #ff5252 #aaa69d #ffb142
#ff5252 - shear #227093 - unzip