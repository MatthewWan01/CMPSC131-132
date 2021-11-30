#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:32:10 2019

@author: mzwonton
"""

n = int (input("Enter Number of Students: "))

minScoreName = ""
minScoreName2 = ""

minScore = 101
minScore2 = 101

i = 0

while (i < n):
    
    print("Please Enter Student ",i+1, " Name :") 
    name = input()
    
    print("Please Enter Student",i+1," Score :")
    score = int(input())

    if (score < minScore):
        
        minScore2 = minScore
        minScoreName2 = minScoreName
        
        minScore = score
        minScoreName = name
        
    elif (score < minScore2):
        
        minScore2 = score
        minScoreName2 = name
    
    i += 1
    
print("Second Lowest Score is ",minScoreName2, " With Score ", minScore2)