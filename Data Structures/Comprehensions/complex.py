#List

mylist=[(x,y) for x in range(5) for y in range(-5,-10,-1)]
print(mylist)

mylist=[x for x in range(50) if x % 2 == 0]
print(mylist)

mylist=[x+y for x in [1,2,3] for y in [ 5, 10] if x + y != 13]
print(mylist)

#Tuple 

mytuple=tuple([(x,y) for x in range(5) for y in range(-5,-10,-1)])
print(mytuple)

mytuple=tuple(i for i in range(100) if i % 3 != 0 and i % 2 != 0)
print(mytuple)

#Set

generator = lambda x, y :{(m,n) for m in x for n in y if m != n }
x = [1, 2, 3]
y = [1, 2, 3]
print(generator(x,y))

#Dictionary

df = {'1': -35,'2': -27,'3': -101,'4': 45}
dc = { x: float((5)/9)*(y-32) for (x,y) in df.items()}
print(dc)


dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print({x:y for (x,y) in dict1.items() if y !=1 if y!=2  })
print({x:('even' if y%2 == 0 else y) for (x,y) in dict1.items()  })

