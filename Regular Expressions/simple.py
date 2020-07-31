import re

text='''
abcdefghijklmnopqestuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

He HeHe

suraj.com

321-555-4567
123.456-4531

Mr Suraj
Mr. Jarus
Mrs Cool
 ages = 1 ,20, 10
cat 
mat
bat
The fat can ran down the street
'''
sentence ='Start a sentence and I dont know what'

digits=re.findall(r'\d{1,2}',text)
namesprefix =re.findall(r'(Mr|Mrs)',text)
print(namesprefix)
print(digits)


pattern= re.compile(r'abc')
matches=pattern.finditer(text)
for match in matches:
    print(match)

pattern= re.compile(r'what$')
matches=pattern.finditer(sentence)
for match in matches:
    print(match)

pattern= re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
matches=pattern.finditer(text)
for match in matches:
    print(match)


pattern= re.compile(r'[^b]at')
matches=pattern.finditer(text)
for match in matches:
    print(match)

pattern= re.compile(r'(Mr|Mrs)\.?\s[A-Z]\w*')
matches=pattern.finditer(text)
for match in matches:
    print(match)