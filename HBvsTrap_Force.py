#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 01:20:58 2020

@author: arventh
"""
import matplotlib.pyplot as plt
import os
print('Program plots Hydrogen bonds vs Force for Harmonic trap forces \nInputs in simulation units')
#Output has time in MD units where MD units = steps * dt
folder = '/home/arventh/Data/oxDNAdata/TO-TD1/6-0_TD_force'#raw_input("Enter directory:")
txt = '6-0-0_out_Observables_1.dat'#raw_input("Enter Observables output file:")
k1, k2 = 0.2 , 0.2 #input("Trap stiffness k1 and k2 :").split() #units in  pN
Ext_rate = 1e-6 #input("Extension_rate :") # rate of increase force (simulation units) per simulation step 
dt = 0.005 # simulation time units 
F_units = 48.63 #units in pN 
L_units = 0.8518 #units in nm
t_units = 3.03e-12 #picoseconds
keff = ((k1*k2)/(k1+k2)) * (F_units/L_units) #1 unit of force constant (1 unit force/1 unit length) - 57.09 pN/nm
os.chdir(folder)
data = open(txt, 'r')
x, y, z = [],[],[]
i = 0
j = 0 

fig = plt.figure()       # size in inches
ax = fig.add_subplot(1,1,1)
 
for line in data:
    z = line.split()
    while j == 0:
        init_dist=(float(z[3]))
        j = 1
    ext = (float(z[3]))*L_units #end to end trap length 
    trap_dist = (((float(z[0])/dt))*Ext_rate)*L_units
    force = ((trap_dist - ext)*keff)
    x.append(force)
    y.append(float(z[2]))
    if float(z[2]) == 85 and i < 10:
        print force
        i=i+1

ax.set(title='Hydrogen bonds vs Force',ylabel='Hydrogen bonds',xlabel='Force (pN)')
ax.set(xlim=[0,500],ylim=[60,125])
plt.plot(x,y, color='#218c74', linewidth=1)
Loadrate = (Ext_rate*L_units)/t_units
Loadrate = format(Loadrate, ".2e") + ' nm/s'
ax.legend([Loadrate], loc=3)
plt.savefig('Hydrogen bonds vs Force for ' + txt + '.png', transparent=True)
plt.show()
data.close()
#2c2c54 #ff793f
#474787 #ff5252
#aaa69d #ffb142
#227093 #34ace0
#218c74 #cd6133
