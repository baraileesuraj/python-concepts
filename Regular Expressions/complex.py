import re
emails='''
suraj.xyz@gmail.com
+977-9813994844
9813131313
9713485678

'''

pattern= re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z]+\.\w{2,3}')
matches=pattern.finditer(emails)
for match in matches:
    print(match)

pattern= re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z]+\.\w{2,3}')
matches=pattern.finditer(emails)
for match in matches:
    print(match)

pattern= re.compile(r'(\+977-)?(98|97|96)\w{8}')
matches=pattern.finditer(emails)
for match in matches:
    print(match)