#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 16:12:57 2022

@author: arventh
"""

import os

folder = '/home/arventh/Documents/oxDNAdata/Yuesong/3-1_YH_anchor_force' #raw_input directory
txt = '3-1_out_last_conf.dat'
os.chdir(folder)
data = open(txt, 'r')
harm_trap = open('3-1_input_forces_py-gen.conf', 'a+')

part_list = [6671,6604,4943,4876,6505,4777,4710,6438,5074]

for linenum, line in enumerate(data, start= -4):
    Zf = line.split()
    if linenum in part_list:
        harm_trap.write("{"+"\n"+"type = trap"+"\n"+"particle = "+str(linenum)+"\n"+"pos0 = "+ Zf[0] +", "+ Zf[1] +", "+ Zf[2] + "\n"+"stiff = 0.2"+"\n"+"rate = 0.0" 
+"\n"+"dir = 0, 1, 0"+"\n"+"}"+"\n")

data.close()
harm_trap.close()

"""
{
type = trap
particle = 207
pos0 = 182.189254760742, 396.799926757812, -120.429077148438
stiff = 0.2
rate = 0.0
dir = 0, 0, 1
}
"""
