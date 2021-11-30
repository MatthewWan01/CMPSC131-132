#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:21:17 2019

@author: mzwonton
"""

number = int (input("Enter a Three Digit Number: "))

first = number // 100
second = (number - (first * 100)) // 10
third = number % 10

print("The First Digit is: ",first)
print("The Second Digit is: ",second)
print("The Third Digit is: ",third)