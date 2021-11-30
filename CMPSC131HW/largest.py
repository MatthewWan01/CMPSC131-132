#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 23:10:18 2019

@author: mzwonton
"""

def largest3(x, y, z):
    
    if y > x:
        
        if z > y:
            
            return z
        
        return y
        
    if z > x:
        
        return z
    
    return x
        
print("Enter 3 integers")

num1 = int (input ("Number 1: "))
num2 = int (input ("Number 2: "))
num3 = int (input ("Number 3: "))

largest = largest3(num1, num2, num3)

print("The largest number of the three is:",largest)

