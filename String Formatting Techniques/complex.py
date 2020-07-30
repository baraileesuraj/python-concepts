# Write a format string that will take the following four element tuple:
# ( 2, 123.4567, 10000, 12345.67)
# and produce:
# 'filename : 123.46, 1.00e+04, 1.23e+04'
import sys
mydata = ( 2, 123.4567, 10000, 12345.67)
filepath = sys.argv[0].split('/')
filename = filepath[-1]
message='%s : %.2f %s %s'%(filename,mydata[1],format(mydata[2],'.2e'),format(mydata[3],'.2e'))
print(message)