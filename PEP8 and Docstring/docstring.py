def squarer(a):
    '''Return square of arguement + 10.'''

    return a *a + 10

print(squarer.__doc__) 


def multiply(number, st):
    '''
    Return repeated number of string concatinated 

        Parameters:
            number(int) :No of repetitions required
            string(st) :Word to be repeated

        Returns:
            repeatedString(str): A repeated concated single word
        
    '''
    return st * number 

print(multiply(20, 'SURAJ'))
print(multiply.__doc__)

