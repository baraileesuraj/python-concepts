#DEBUG 
#INFO
#WARNING
#ERROR
#CRITICAL
import logging
import employee

logger =logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
fileHandler=logging.FileHandler('./Logging/Logged Files/sample.log')
fileHandler.setFormatter(formatter)
fileHandler.setLevel(logging.ERROR)
logger.addHandler(fileHandler)

def add(x, y):
    '''Add two Values'''
    return x + y

def subtract(x, y):
    '''Subtract two values'''
    return x - y

def divide(x, y):
    '''Divide two values'''

    try:
        x / y
    except ZeroDivisionError:
        logger.error('Tried to Divide by zero')
    else:
        return x/y



num1 = 100
num2 = 45

addition = add (num1,num2)
print('Added {} + {} = {}'.format(num1,num2,addition))

subtraction = subtract (num1,num2)
print('Subtracted {} - {} = {}'.format(num1,num2,subtraction))

num1 = 90
num2 = 50

addition = add (num1,num2)
logger.debug('Added {} + {} = {}'.format(num1,num2,addition))

subtraction = subtract (num1,num2)
logger.debug('Subtracted {} - {} = {}'.format(num1,num2,subtraction))

num1=5
num2=0
division = divide (num1,num2)
logger.debug('Divided{} - {} = {}'.format(num1,num2,division))