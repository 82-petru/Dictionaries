# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:36:58 2019

@author: petru
"""

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dict1.keys())
print(dict1.values())
print(dict1.items())
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)

for (k,v) in dict1.items():
    double_dict = {k:v**2}
print(double_dict)
    