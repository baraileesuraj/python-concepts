import logging


logger =logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
fileHandler=logging.FileHandler('./Logging/Logged Files/employee.log')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

class Employee:
    '''Employee sample Class'''
    def __init__(self,first,last):
        self.first = first
        self.last = last
        logger.info('Created Employee :{} {}'.format(self.fullname,self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)


emp_1 = Employee('Suraj','Jarus')