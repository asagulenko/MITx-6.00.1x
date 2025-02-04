#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 19:38:47 2025

@author: anna
"""
"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' 
occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""
s='azcbobobegghakl'

number_of_bob=0
i=0 #element index in the string

for char in s:
    if s[i:i+3]=="bob":
        number_of_bob+=1
    i+=1
print ("Number of times bob occurs is: " + str (number_of_bob))