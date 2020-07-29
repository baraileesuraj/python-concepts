def print_function(a, b):              # Print the arguements passed.
    print(a, b)

print_function(10, 20)   






def add_function(a, b=20, c=30):       # Print sum of all the arguement.
    print(a + b + c)

add_function(100)
add_function(100, 200)
add_function(100, 200, 300)




def multiply(x, y=200, z=5):           # Print multiplication of all the arguements passed.
    print(x * y * z)

multiply(100, z=200, y=100)


def argument_displayer(*args):         # Display the arguements passed
    for elements in args:
        print(elements)

argument_displayer('1','asdasd','hello','world')



def kwargs_displayer(**kwargs):        # Display  key value pair of the arguements passed
    for key, value in kwargs.items():
        print(key,value)


my_dict={"arg1" : "value1", "args2" : "value2"}
kwargs_displayer(**my_dict)


def normal(arg):                       # Normal Parameters
    print(arg)

def position(arg, /):                  # Position Only Parametes that works on 3.8 and above
    print(arg)

def kwd_only( *,args):                  # Keyword Only Arguements
    print(args)

normal(2)
position(5)
kwd_only(arg=2)