#Stacks
#First In Last Out

bucket=[20,1000]

print('Initialized bucket = ', bucket)
#Push to the bucket
bucket.append(14)
print('After adding an item, bucket =', bucket)
bucket.append(15)
print('After adding an item, bucket =', bucket)
bucket.append(108)
print('After adding an item, bucket =', bucket)

#Take out From the bucket

bucket.pop()
print('After removing an item, bucket =', bucket)
bucket.pop()
print('After removing an item, bucket =', bucket)
bucket.pop()
print('After removing an item, bucket =', bucket)



#Lists
data=['Suraj', 'Raj', 'Jarus', 'Aj', 'Sur']
print(data)
print(data[1],data[-1])
print(data[:-1])
print(data[2:4])
print(data[-2:-1])
data[1]='RAJ'
print(data)
for x in data:
    print(x)


#Queue
queue=[]
queue.append('x')
queue.append('y')
queue.append('z')
print('Initial Queue', queue)
print(queue.pop(0))
print(queue.pop(0))
print(queue)


