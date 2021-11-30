#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 22:58:30 2019

@author: mzwonton
"""
n = int (input("Please Enter a Number of Elements in list: "))

lst = []

i = 0

while (i < n):
    
    print(end="Enter Element: ")
    
    num = input()
    
    lst.append(num) 
    
    i += 1

print("You Entered: ",lst)

i = int ((n/2))
j = i + 1

while (i < n) and (j < n):
    
    while (j < n):
        
        if lst[i] == lst[j]:
            
            lst[i] = lst[j]
        
        if lst[i] > lst[j]:
        
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

        j += 1
        
    i +=1
    j = i + 1
                
print(lst)
