matrix =[[j for j in range(5) if j !=2 ] for i in range(5) if i != 2 ]
print(matrix)


openmatrix=[x for y in matrix for x in y]
print(openmatrix)

s={(i,j) for i in range(6,10) for j in range(8,10) if i != j}
print(s)

myobj={
        'Students' :[
                        {'names' : ['Suraj', 'Jarus', 'Mercury', 'Earth']},
                        {'names' : ['Gold','Diamond','Suraj']}
                    ]
    }

#List implementation
allnames=set(n for n1 in myobj['Students'] for n in n1['names'])
print(allnames)

#Set Implementation
allnames={x for x1 in myobj['Students'] for x in x1['names'] if x !='Suraj'}
print(allnames)



diction={(x,x + y) : x - y for x in range(5) for y in range(2) if x + y !=1 if x-y != 0}
print(diction)
