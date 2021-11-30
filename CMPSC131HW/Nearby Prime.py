#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 23:13:29 2019

@author: mzwonton
"""

print(end="Enter n: ")

n = int (input())

if 1 < n < 4:

    print("The prime closest to ",n, "is ",n)

elif n < 1:

    print("The prime closest to ",n, "is ",2)

elif n > 3:

    for num in range(n // 2, n):
    
        for i in range(2, n // 2):
            
            if (num%i) == 0:
                break
        else:
            lowPrime = num
            lowDiff = n - lowPrime     

    for num in range(n, 2 * n):
    
        for i in range(2, n):
            
            if (num%i) == 0:
                break
        else:
            highPrime = num
            highDiff = highPrime - n
            break

    if lowDiff > highDiff:
        
        print("The prime closest to ",n, "is ",highPrime)

    else:

        print("The prime closest to ",n, "is ",lowPrime)

