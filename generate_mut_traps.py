#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:24:08 2020
@author: arventh
"""
#creates a mutual trap force between particles separeted by '&'
import os
os.chdir('/home/arventh/Data/oxDNAdata/TO-TD1/2-4_TD_force_relax_CUDA')
Particle_list = open('MutTrapList.txt', 'r')
Mut_trap = open('input_forces_py-gen.conf', 'a+')
for particle_pair in Particle_list:
    part_no = particle_pair.split('&')
    for i in range(1): 
        Mut_trap.write("{"+"\n"+"type = mutual_trap"+"\n"+"particle = "+part_no[0-i].strip()+"\n"+"ref_particle = "+part_no[1-i].strip()+"\n"+"stiff = 1.0"+"\n"+"r0 = 1.2" 
+"\n"+"PBC = 1"+"\n"+"}"+"\n")
Particle_list.close()
Mut_trap.close()



"""
Sample output
{
type = mutual_trap
particle = 216
ref_particle = 62
stiff = 0.09
r0 = 1.2 
PBC = 1
}

{
type = mutual_trap
particle = 62
ref_particle = 216
stiff = 0.09
r0 = 1.2 
PBC = 1
}

"""