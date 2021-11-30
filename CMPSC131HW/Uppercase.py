#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:21:50 2019

@author: mzwonton
"""

lower = input ("Please Enter a Character: ")

if (ord(lower) < 65) or (ord(lower) > 122):
        
        print("You Didnt Enter an Alphabet")
        
        
else:
      
      if (ord(lower) > 65 and ord(lower) < 97):
              
              upper = lower
              
              
      else:
              
              upper = chr(ord(lower) - 32)
      
      print("The Uppercase is ",upper)
           
