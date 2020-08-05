

class FormulaError(Exception):
    '''Class FormulaError that inherits Exception class'''
    pass

def checker(user1):
    '''Check if there are three user input''' 
    user=user1.split()
    if( len(user) !=3):
        raise FormulaError('Input is wrong you idiot.I need three')
    n1,op,n2=user
    try:
        n1=float(n1)
        n2=float(n2)
    except ValueError:
        raise FormulaError('Bro Seriously you need medicine')
    return n1,op,n2

def calculation(a,o,b):
    '''Calculate two values according to second arguement and return the value'''
    if( o == '+'):
        return a+b
    elif( o == '-'):
        return a-b
    else:
        raise FormulaError('WRONG operator I support + and - only')

while True:
    user=input('Please enter the expression :  ')
    if(user == 'quit'):
        break
    else:
       
        a,o,b=checker(user)
        result=calculation(a,o,b)
        print(result)
