from functools import reduce
mylist=[1,4,2,3,4,78,65,12,11,400,475,84,42]
filtered=filter(lambda x: x <= 20 ,map(lambda x:x*2,mylist))
print(list(filtered))


mylist=[1,4,2,3,4,78,65,12,11,400,475,84,42]
reduced = reduce(lambda x,y : x + y,filter (lambda x : x % 2 ==0,map(lambda x : x + 3,mylist)))
print(reduced)
