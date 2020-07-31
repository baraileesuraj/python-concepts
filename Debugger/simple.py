import pdb

z=5
x=520
y= 700


def adder(x,y):
    z = x + y
    print(z)


pdb.set_trace()
adder(x,y)
print('z= ' + str(z))