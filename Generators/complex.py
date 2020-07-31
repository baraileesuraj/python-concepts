


def checker(n):
    if( n < 2):
        return False
    elif (n == 2 or n == 3):
        return True
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True
def getPrimes():
    value = 0
    while True:
        if checker(value):
             i=yield value
             
             if( i is not None):
                 value = i
        value += 1

primes = getPrimes()
print(next(primes))
print(next(primes))
print(next(primes))
print(primes.send(100))

for x in primes:
    if(x > 500):
        primes.close()
    print(x)

for x in primes:
    if(x > 1000):
        primes.throw('thulo Vayo')
    print(x)