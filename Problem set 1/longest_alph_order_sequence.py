#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:07:36 2025

@author: anna
"""

"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which 
the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
"""

s=('azcbobobegghakl') #initial string
n_string=s[0] #temporary sequence string for comparison
longest_string=s[0] #longest sequence in alphabetical order

for char in s[1:]:
     if char>=n_string[-1]:
        n_string+=char #if in alph order, adding char to the sequence
        if len(longest_string)<len(n_string): #comparing the length of the sequences
            longest_string=n_string
     else: n_string=char #rewriting the temporary sequence
    
print ("Longest string in alphabetical order is: "+str(longest_string))
