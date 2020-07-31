#DEBUG 
#INFO
#WARNING
#ERROR
#CRITICAL
import logging
logging.basicConfig(filename='./Logging/Logged Files/test.log',
                    level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

import logging

def add(x, y):
    '''Add two Values'''
    return x + y

def subtract(x, y):
    '''Subtract two values'''
    return x - y


num1 = 100
num2 = 45

addition = add (num1,num2)
print('Added {} + {} = {}'.format(num1,num2,addition))

subtraction = subtract (num1,num2)
print('Subtracted {} - {} = {}'.format(num1,num2,subtraction))

num1 = 90
num2 = 50

addition = add (num1,num2)
logging.debug('Added {} + {} = {}'.format(num1,num2,addition))

subtraction = subtract (num1,num2)
logging.debug('Subtracted {} - {} = {}'.format(num1,num2,subtraction))