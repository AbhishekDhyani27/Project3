# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 11:27:09 2021

@author: dhyani
"""

S= input('Please enter a string ')
def most_frequent(string):
    a = dict()
    for key in string:
        if key not in a:
            a[key] = 1
        else:
            a[key] += 1
    return a

print (most_frequent(S))