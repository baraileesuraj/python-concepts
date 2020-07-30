import sys

randomList=['a',0,2]

for data in randomList:
    try:
        print('The entry is ',data)
        d=1/int(data)
        break
    except:
        print("OPs!")
        print('Next entry')
        print()
    else:
        print('Great Work')

    

try:
    x=int(input('Enter a number'))
    print(1/x)
    
except ValueError:
    print("Wrong input")
except :
    print("Other errors")
else:
    print("WOALA no errors")

