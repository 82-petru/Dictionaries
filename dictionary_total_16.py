# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 20:54:49 2019

@author: petru
"""
#calculeaza totalul din cele doua dictionare dupa ficare obiect in parte
prices = {
  "banana" : 4,
  "apple"  : 2,
  "orange" : 1.5,
  "pear"   : 3,
}
stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}
def compute_bill(food):
  total = 0 
  for item in food: 
    if stock[item] > 0:
       total += prices[item]
       stock[item] -= 1
  return total
print(compute_bill(['banana']))

