# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:46:16 2020

@author: petru
"""
from collections import Counter

def values_that_are_keys(my_dictionary):
    value_list = []
    for key in my_dictionary.keys():
        for value in my_dictionary.values():
          if key == value:
            value_list.append(value)
    return value_list
# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

# Write your add_ten function here:
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary
  
# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  even_keys_values = 0
  for key in my_dictionary.keys():
    if key % 2 == 0:
      even_keys_values += my_dictionary[key]
  return even_keys_values
  
# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

# Write your max_key function here:
def max_key(my_dictionary):
    max_value = max(my_dictionary.values())
    max_keys = 0
    for k, v in my_dictionary.items():
      if v == max_value:
        max_keys = k
    return max_keys
# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  words_length = []
  for word in words:
     words_length.append(len(word))
     dictionary = {k:v for k,v in zip(words, words_length)}
  return dictionary
    
# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  dictionary = {} 
  for word in words:
    count = 0
    for word_ in words:
      if word == word_:
        count += 1
    dictionary[word] = count
  return dictionary
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

# Write your unique_values function here:
def unique_values(my_dictionary):
      count = 0
      unique_values = []
      for i in my_dictionary.values():
          if i not in my_dictionary:
            unique_values.append(i)
            count = len(unique_values)
      return count   
# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 

# Write your unique_values function here:
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
    #else:
      #seen_values.append(value)
  return len(seen_values)
      
# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

# Write your count_first_letter function here:
def count_first_letter(names):
  my_dictionary = {}
  for name in names.keys():
    if name[0] not in my_dictionary:
      my_dictionary[name[0]] = len(names[name])
    else:
       my_dictionary[name[0]] += len(names[name])
  return my_dictionary
# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}







