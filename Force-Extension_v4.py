#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:09:07 2021
Updated 2022 July 17
@author: arventh
"""
import os
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Segoe UI']
#Inputfile wtih time, energy, HBs, strand length and x, y, z co-ords for 2 the two traps, i.e. Zf[4:7], Zf[7:10] 
folder = '/home/arventh/Documents/oxDNAdata/AV/TO-TD1/6-x_CPU runs/6-1_TD_force_CPU' #raw_input directory
txt = '6-1-0_out_Observables_1.dat'
os.chdir(folder)
data = open(txt, 'r')
i, x, y, y_peak = 0,[],[],[]

#Constants. Change these parameters to simulation conditons.
dt = 0.005 #simulation time units (Output has time in MD units where MD units = steps * dt)
F_units = 48.63 #units in pN 
l_units = 0.8518 #units in nm 
t_units = 3.03e-12 #seconds
k1,k2 = 0.2,0.2 #simulation units
m_avg = 40 #exponential moving average smoothing of n-points
ext_rate = 0.5e-7 #rate of increase length (simulation units) per simulation step
F_dir = np.array([0,1,1]) #direction of trap movement
t1_init = np.array([132.198608804851, -101.474830202562, 10.7769768873484]) #moving trap
t2_init = np.array([182.189254760742, 396.799926757812, -120.429077148438]) #fixed trap
UnitF_dir = F_dir/np.linalg.norm(F_dir) #unit vector
init_dist = np.dot((t1_init - t2_init), UnitF_dir) #initial distance between two traps along force dir
keff = ((k1*k2)/(k1+k2)) #1 unit of force constant (1 unit force/1 unit length) - 57.09 pN/nm

fig = plt.figure() 
ax = fig.add_subplot(1,1,1)
for line in data:
    Zf = np.array(line.split(), dtype=float)
    l_dna = Zf[3]*l_units #end to end strand length
    trap1_current = t1_init + (Zf[0]/dt)*ext_rate*UnitF_dir #trap1 displacement
    trap_ext1 = trap1_current - Zf[4:7]  #vector subtraction of moving trap1 and its attached nucleotide
    trap_ext2 = Zf[7:10] - t2_init #vector subtraction of fixed trap2 and its attached nucleotide
    force = (np.dot((trap_ext1+trap_ext2),UnitF_dir))*keff*F_units
    overall_ext = trap1_current - t2_init
    trap_ext = (np.dot(overall_ext,UnitF_dir)-init_dist)*l_units
    x.append(trap_ext) #this is extension of traps along force-axis not the DNA strand extension.
    y.append(force)
    if Zf[2] == 110  and i == 0: #Zf[2] is HB count
        Rupture_F = force
        Rupture_ext = trap_ext
        y_peak.append(force)
        i = 1

y_peak = pd.Series(y).rolling(window=m_avg).mean().iloc[m_avg-1:].values # EMA calculation
y_pk = y_peak.tolist()
for loop in range(m_avg-1):
    y_pk.insert(0, 0)

#graph plotting 
ax.set(ylabel='force (pN)', xlabel='trap extension (nm)')
ax.set(xlim=[0,40],ylim=[-2,70])
plt.plot(x,y, color='#90BF2A',linewidth=0.5)
Loadrate = (ext_rate*l_units)/t_units
Loadrate = format(Loadrate, ".2e") + ' nm/s'
Force_label = format(force, ".2f") + ' pN'
plt.plot(x,y_pk, color='#344973',linewidth=0.5, alpha = 1)
ax.legend([Loadrate, 'EMA ('+ str(m_avg)+ ')'], loc=0, frameon=1)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
#D94862 #344973
#90BF2A #144C59

peaks, ht = find_peaks(y_pk, height=40, prominence=2) #finds a list of peaks satisfying the criteria
for peakapeaka in peaks:
    if x[int(peakapeaka)] > Rupture_ext: #Range in which peaks are needed
        anno = str(round(y_pk[int(peakapeaka)], 2)) #+' pN' # peak annotation
        plt.plot(x[int(peakapeaka)],y_pk[int(peakapeaka)],"o", color='#000000', alpha=0.6, fillstyle = 'none')
        ax.annotate(anno,xy=(x[int(peakapeaka)], y_pk[int(peakapeaka)]), 
            xycoords='data', xytext=(5,5), #offset the rupture force annotation
            textcoords='offset points', horizontalalignment='left', verticalalignment='bottom')

#plt.savefig('Force vs trap Extension_1 for ' + txt.rstrip('.dat') + '.png', transparent=True)
plt.show()

for oolala in range(len(x)):
    csv = open("Force_ext_graph_plot.csv", "a")
    csv.write(str(x[oolala]) + ',' + str(y[oolala]) + ',' + str(y_pk[oolala]) + '\n')

csv.close()
data.close()

