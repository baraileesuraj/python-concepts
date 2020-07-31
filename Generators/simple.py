def odds(start,stop):
    for odd in range(start,stop+1,2):
        yield odd

g2=odds(7,21)
print(list(g2))
g1=odds(1,100)
print(list(g1))

odd_values = [odd for odd in odds(10,100)]
print(odd_values)

mynums=(x*x for x in [1,2,3,4,5,6,7])
for nums in  mynums:
    print (nums)
