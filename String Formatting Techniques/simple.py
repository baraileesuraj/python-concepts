name='Suraj'
address='Goldhunga'
age=100
print('Hello I am %s.I am from  %s and I am %d years old'%(name,address,age))

subjects=['Science','Math','Geology']
print('My subjects are %s'%subjects)

#Older Method
data=("Abcd","xyz",53.45456456)
greetings='Hello'
message='%s %s %s.Your balance is %.2f'%(greetings,data[0],data[1],data[2])
print(message)

#String.Format

print('{quantity} {item} can cost you about {price}'.format(
    quantity=6,
    item='Apple',
    price='100'))

print('{0} {1}'.format('Amazing','Life'))

print('{0},{1},{y}'.format('x','z',y='y'))

print('{mylist[0]}, {mylist[2]}'.format(mylist=['A','Quick','Brown']))

quantity, item, price = 6, 'bananas', 5
print(f'One item cost is ${price/quantity}')

a=['foo','bar']
print(f'First item in list a = {a[0]}')

b={'f':6,'g':7}
print(f"Value of f in b is {b.get('f')}")