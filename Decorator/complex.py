class decoratorclass(object):
    def __init__(self,original_function):
        self.original_function=original_function
    
    def __call__(self,*args,**kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args,**kwargs)


@decoratorclass
def display(name,age):
    print('display function ran with arguements', name, age)

display('Suraj','34')
