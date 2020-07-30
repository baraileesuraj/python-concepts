import csv
import requests
import json
import urllib
file=['./resources/data.csv','./resources/new.csv']
line=0
for f in file:
    with open(f,'r') as csvfile:
        csvreader=csv.reader(csvfile)
        with open('./resources/newrandom1234.csv','a') as new:
            csvwriter = csv.writer(new, delimiter=',')
            if (line == 0):
                csvwriter.writerow(["first_name",'last_name','rows'])
                line = 2
            next(csvreader,None)
            for line in csvreader:
                csvwriter.writerow(line)



sample={"key1" : "suraj", "key2" : "jarus", "key3" : "aj"}
formatted=json.dumps(sample,indent=2,separators=(",", " = "))
print(formatted)
