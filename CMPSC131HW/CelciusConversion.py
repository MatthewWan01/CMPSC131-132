#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:09:26 2019

@author: mzwonton
"""

print(end="Please Enter the Temperature in Fahrenheit: ")

far = float (input())

cel = float ((far - 32) * 5 / 9)

print("the Temperature in Celcius is: ",cel)
