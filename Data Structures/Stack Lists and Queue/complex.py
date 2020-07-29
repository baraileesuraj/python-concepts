from collections import deque
from queue import LifoQueue
from queue import Queue
#Stack
#implementation using 

stack = deque()
stack.append('a1')
stack.append('b1')
stack.append('c1')

print(stack.pop())
print(stack)

stacker=LifoQueue(maxsize=5)
print(stacker.qsize())

stacker.put('Hello')
stacker.put('World')
print('Size is ',stacker.qsize())
print(stacker.get())



#Queue

q=Queue(maxsize=4)

q.put('asd')
q.put('sad')
print('Queue maxsize is',q.qsize())
print(' Queue is Full ?',q.full())
