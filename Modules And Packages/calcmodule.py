def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def fact(number):
    if number == 1:
        return number
    else:
        return number *fact(number-1)

def palinodrome(n):
    n1 = n [::-1]
    if(n1 == n):
        return 'palinodrome'
    else:
        return ' Not palinodrome'

def find_index(mylist,target):
    for i,value in enumerate(mylist):
        if value == target:
            return i
    else:
        return -1