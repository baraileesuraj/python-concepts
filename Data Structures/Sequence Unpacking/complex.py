(a, b, c), d='axe','max'
print(a,b,c,d)

a, (b, c, d), e='apple','cat','dog'
print(a,b,c,d,e)


for (x,(y,z)) in [(1,(2,4)),(2,(3,6))]:
    print(x, y, z)


animals = ['a', 'b' ,'c', 'd', 'e', 'f']

first,*others=animals
print(first,others)

*others,last=animals
print(others,last)


first, *others, last =animals
print(first,others,last)

first, *others, last ='animals'
print(first,others,last)

first,*others=range(1,20)
print(first,others)



for a, *b, c in (".asd.",".sadasasdasd.",".qweasdasdads."):
    print(b)


a,b={'one':1,'two':2}
print(a,b)