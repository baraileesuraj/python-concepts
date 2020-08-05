class Students:
    ''' Create class student with name and password'''
    def __init__(self,name,password):
        self.name=name
        self.__password=password
    def passwordret(self):
        return self.__password

class Additional(Students):
    '''Class Additional  with language attribute extending Students.'''
    def __init__(self,name,password,language):
        super().__init__(name,password)
        self.language=language

class MoreData(Additional,Students):
    '''Class MoreData with address attribute extending Additional and Students class'''
    def __init__(self,name,password,language,address):
         Additional.__init__(self,name,password,language)
         self.address=address

data=Students('Hari','Hari123')
print(data.name)
print(data.passwordret())

data1=Additional('Ram','Ram123','Python')
print(data1.passwordret())
print(data1.language)

obj1 = MoreData('Suraj','Suraj123','Java','Kathmandu')
print(obj1.address)
print(obj1.name)

    
