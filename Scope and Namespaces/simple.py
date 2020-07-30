
s='Suraj'
def f():
    global s
    print(s)
    s='Jarus'
    print(s)
f()

x='global'

def foo():
    y='local'
    print('x inside = ', x)
    print('y inside = ', y)

foo()
print('x outside = ', x)
try:
    print('y outside = ', y)
except:
    print('Error y not found')