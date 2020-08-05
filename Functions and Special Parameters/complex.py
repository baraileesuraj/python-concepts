def combined(pos, pos1, /, standard,standard1, *, kwd_only, kwd_only1):       
    ''' Use Parameters types in combined Format '''
    print(pos, standard, kwd_only, kwd_only1)

combined(1, 2, 2, standard1=123, kwd_only=3, kwd_only1=300)


def arg_function(arg,*args ,**kwargs):          
    ''' Print 1st , add normal ones and print other arguments.'''          
    print('First argument is' ,arg)
    x = 0
    for elements in args:
        x = x + elements
    print(x)
    for x,y in kwargs.items():
        print('key is "' + x + '" and value is "'+ y + '"')

arg_function('asd',1 ,2 ,3 ,4 ,5,hello='asdasdasd',world='asd')





def list_taker(l):                          
    '''Change value of name key to 'Not Suraj' '''
    l['name'] = 'Not Suraj'

my_data={'name':'Suraj'}
list_taker(my_data)

print(my_data)
