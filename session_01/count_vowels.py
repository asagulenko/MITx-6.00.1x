#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 19:37:30 2025

@author: anna
"""

"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""

s='azcbobobegghakl'

number_of_vowels=0

for char in s:
    if char in ('aeiou'):
        number_of_vowels+=1
        
print ("Number of vowels: " + str (number_of_vowels))