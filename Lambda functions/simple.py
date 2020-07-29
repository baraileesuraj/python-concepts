myfunction = lambda x, y : x + y 
print(myfunction(10,20))



def myfunc(n):
    return lambda a : a * n

mydoubler=myfunc(2)
mytripler=myfunc(3)

print('After doubling' , mydoubler(10))
print('After Tripling', mytripler(10))


x = 'this is my String value to be returned'
f=lambda x : print (x)
f(x)

print((lambda *args : sum(args))(20,30,40))

print((lambda **kwargs : sum(kwargs.values()))(one=1, two=2, three=3))
