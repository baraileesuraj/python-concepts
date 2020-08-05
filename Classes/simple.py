class MyClass:
    '''Class Myclass with object variable name and age;and class variable called classvariable''' 
    classvariable=30
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def details(self):
        print('Hello My name is ' + self.name + 'And I am of age ' + self.age)

o1=MyClass('GOD',10000000000000)

o2=MyClass('GODDESS',231524568978)
print(o1.name)
del o1

print(o2.age)
print(o2.classvariable)