
user='Suraj'
def a():
    print('inside a :' , user)
def b():
    user='Jarus'
    print('inside b : ' , user)
def c():
    global user
    user='God'
    print('inside c : ' , user)

a()
b()
c()

#Create Non Local Variable
def outer():
    x='local'
    
    def inner():
        nonlocal x  #x should not belong to inner function but outer
        x='nonlocal'
        print('inner x' ,x)
    
    inner()
    print('outer' , x)

outer()