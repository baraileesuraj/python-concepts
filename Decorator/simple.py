from datetime import datetime
def notnight(func):
    def wrapper():
        if 3 <=datetime.now().hour < 20 :
            print('You can shout')   
            func()
        else:
            print('Maybe its night time.....SSH! donot shout')
            pass
    return wrapper

@notnight  # shouting=notnight(shouting)
def shouting():
    print('OHHHHHHHHHHHHHHHHHHHHHOOOOOOOOOOHOOOOOOOHO')

shouting()