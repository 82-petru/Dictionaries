d = {} #empty dictionary 
d['A'] = 67 #code to include key/value into the dictionary 
d['B'] = 89.5
d['F'] = 34
print(len(d))
print("There are " + str(len(d)) + " items in the basket") # len function will count pairs from curly braces

g = {'cat' : 'sireata', 'dog' : 'slave', 'fish' : 'balosi'} #dcitionary key = animal and  value = atribut
del g['dog'] #Removing key, the dog from the list with del funtion: del variable name[key name]
g['cow'] = 'blanda' #include a new key/value into the list
print(len(g)) #check if it is there
print(g['cat']) # to be sure 
#remove a string or item from a list
#In Python Dictionary, items() method is used to return the list with all dictionary keys with values.
beatels = ['gaina', 'harbuz', 'jupiter']
beatels.remove('harbuz')
print(beatels)

#dictionary holds many types of lists
h = { 
'fish' : ['a', 'n', 'v'], # list 1 comma after list
'football' : ['barsa', 'madrid'], #list 2 use comma after list
'money' : -8976} #list 3

print(h['fish'][2]) #dictionary'h'key fish of list 1, value 2(3 in the list )