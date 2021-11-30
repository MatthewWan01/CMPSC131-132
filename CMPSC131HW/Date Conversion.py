#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 22:03:38 2019

@author: mzwonton
"""

fRead = open ("dobA.txt" , "r")
fWrite = open ("dobB.txt" , "w")

s = fRead.readline()

while s != "":
    
    s = s.rstrip("\n")
    a = s.split()
    conversion = " "
    
    date = a[len(a) - 1].split("/")

    temp = date[1]
    date[1] = date[0]
    date[0] = temp
    
    a.pop(len(a) - 1)  
    
    nDate = date[0]+"/"+date[1]+"/"+date[2]
    
    a.append(nDate)
    
    conversion = conversion.join(a)

    fWrite.write(conversion + "\n")
    
    s = fRead.readline()
    
fRead.close()
fWrite.close()
