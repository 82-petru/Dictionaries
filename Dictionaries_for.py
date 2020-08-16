# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 18:42:02 2019

@author: petru
"""

my_dict = {"petru" : 37, "vera" : 36, "mama" : 65}

print(my_dict.items())
print(my_dict.keys())

for key in my_dict:
    print(key, my_dict[key])
    
for k in 'petru':
    print(k,)
    
even_50 = [i for i in range(51) if i % 2 == 0]
print(even_50)

double = [ x * 2 for x in range(1, 6)]
print(double)
print()
double_3 = [x * 2 for x in range(1, 23) if x % 3 == 0]
print(double_3)
print()
even_square = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(even_square)
print()
cubes_by_four = [x**3 for x in range(1, 10) if x % 4 == 0]
print(cubes_by_four)