#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#won't work with python3
"""
Created on Mon May 04 11∶09∶52 2020 
@author: arventh
Code optimized on 2020June18. 
"""
#Converts 5'-3' text to 3'-5' while encoding to utf-8 for generate-sa.py
import os
os.chdir('/home/arventh/Documents/oxDNAdata/Yuesong')
Seq_in = open('5-3_Seq', 'r')
Seq_out = open('3-5_seq.txt', 'a+')

data = Seq_in.read()#.decode("utf-8-sig").encode("utf-8")
lines = data.splitlines()
for line in lines:
    seq = line.replace(" ","") #Use replace(old, new) for formatting output
    Seq_out.write(seq[::-1] + "\n")
Seq_out.close()
Seq_in.close()
