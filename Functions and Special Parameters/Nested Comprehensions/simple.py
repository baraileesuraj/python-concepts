
matrix =[[j for j in range(5)] for i in range(5)]
print(matrix)


matrix =tuple([[j for j in range(5)] for i in range(5) if i != 5])
print(matrix)


lister=[1,2,1,1,1,1,1]
matrix =tuple([j for j in lister] for i in range(5))
print(matrix)

lister=[1,2,1,1,1,1,1]
matrix =[{j for j in lister} for i in range(5)]
print(matrix)



s={(i,j) for i in range(6,10) for j in range(8,10)}
print(s)



diction={(x,x + y) : x - y for x in range(5) for y in range(2)}
print(diction)

