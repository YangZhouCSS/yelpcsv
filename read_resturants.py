"""
This is a small program that transfers the 2017 Yelp dataset from json to csv
sample.json includes 100 lines from the original file
Only resturants and user selected headers will be included in the output file
Created by Yang Zhou 3/7/2017
"""

import json


f=open('sample.json')


headers = ["business_id","name","categories","stars","review_count","longitude","latitude"]  #put in headers that you want to include

f2 = open('data_resturants.csv', "w")

for n in headers:
    f2.write(str(n) + ',')
f2.write('\n')


for i,line in enumerate(f):
    try:
        x = json.loads(line)
        if 'Restaurants' in x['categories']:
            for n in headers:
                f2.write(str(x[n]).replace("]", "").replace("[", "").replace(",", " ") + ',')
            f2.write('\n')
        
    except:
        print ("error occured at #" + str(i)) #cases when catergories = null





f.close()



f2.close()
