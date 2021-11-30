#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:53:17 2019

@author: mzwonton
"""

print(end="Enter n: ")

n = float (input())
i = 1
j = 1

while (i <= n):
    print(j , end=" ")
    i = i + 1
    j = i % 2