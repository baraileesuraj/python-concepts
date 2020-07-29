#List
single = [letter for letter in 'How are you']
print(single)

square = [1,2,3,4,5,6,7,8,9,10]
square = [x ** 2 for x in square]
print(square)


#Tuple
mylist = [1,2,3,4,5,6,7,8,9,10]
square = tuple(x ** 2 for x in square)
print(square)


#Set
myset={d for d in [1, 2, 3, 1, 2, 3, 4]}
print(myset)

myset={d for d in [1, 2, 3, 1, 2, 3, 4] if d % 2 == 0}
print(myset)


#Dictionary

dictionary={x:y for x in ['one','two','three'] for y in [2]}
print(dictionary)

mydict = {'a': 1, 'b': 2, 'c': 3,}
dict2={x : y+200 for (x, y) in mydict.items()}
print(dict2)

dict2={x : y+200 for (x, y) in [('Suraj',1),('Suraj12',112)]}
print(dict2)