data={
    'Suraj':'active',
    'Jarus':'inactive',
    'Urja':'active',
    'Raj':'inactive'
     }

active_users={}
for name, status in data.items():
    if(status == 'active'):
        active_users[name] = status

print(active_users)

print('')

print('')
print('')

for i in range(1,10):
    for j in range(10,i,-1):
        print('*',end='')
    print('')



print('------------------------------------------------------')
#Print Map of Nepal
for i in range(0,6):
    for j in range(0,i):
        print('*',end='')
    if(i != 5):
        print('')
for i in range(0,6):
    for j in range(0,i):
        print('*',end='')
    print('')
print('|')
print('|')
print('|')




print('------------------------------------------------------')


#Print Pyramid

level=10
i=0
level=level+2

while i < level:
    j=0
    while j < level:
        print(' ',end='')
        j += 1
    k=0
    while k < i +1:
        print( '* ',end='') 
        k += 1
    level = level - 1
    print("")
    i += 1