from functools import reduce
mylist=[1,12,21,23,45,48,86,10,43]


result = filter(lambda x : x > 10, mylist)
print(result)
print(list(result))

result = map(lambda x : x + 100, mylist)
print(list(result))

result = reduce(lambda x, y: x + y, mylist)
print(result)

data = [('Suraj',50),('Jitendra',100),('Abhimanyu',85),('Ajay',80)]
data.sort(key=lambda d : d[1], reverse=True)
print(data)



squared = lambda x : x ** 2
cubed = lambda y : y ** 3
print('The cube of ' + str(squared(3)) + ' is ' + str(cubed(squared(3))))
