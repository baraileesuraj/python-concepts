import csv
import json

#CSV READER
with open('./resources/data.csv','r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    for line in csvreader:
        print(line) 

#CSV WRITER
with open('./resources/data.csv','r') as csvfile:
    csvreader=csv.reader(csvfile)
    with open('./resources/newrandom.csv','w') as new:
        csvwriter =csv.writer(new,delimiter=' '
        for line in csvreader:
            csvwriter.writerow(line)




#JSON 

json_file=open('./resources/myjson.json','r')
mydata =json.load(json_file)
print(mydata['items'])

value = '''
        {
            "title":"Thinking Fast And Slow",
            "Writer":"Daniel",
            "Price":"500",
            "Delivery":true,
            "Discount":null
        }'''
parsedvalue=json.loads(value)
print(parsedvalue['Delivery'])

unparsedvalue=json.dumps(parsedvalue)
print(unparsedvalue)





        
