import math
from functools import reduce
#Map Function

#Area Of Circle with radii
radii=[2, 10, 0.9, 4]
areas=list (map(lambda r:math.pi *(r**2) ,radii))
print(areas)

#Filter And Reduce
data=[1.3,2.6,4,5.6,4.1,2.3,3.2]
m=0
total=0
total = reduce(lambda x,y: x + y ,data)
avg = round(total/len(data),3)
filtered=list(filter(lambda x:x < avg,data))
print(filtered)



