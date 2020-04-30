import configparser
import json
import requests
import csv

config = configparser.ConfigParser()
config.read('config.ini')

# instance = 'Test'
instance = 'Production'
baseURL = config.get(instance, 'baseURL')
user = config.get(instance, 'user')
password = config.get(instance, 'password')

auth = requests.post(baseURL + '/users/'+user+'/login?password='+password).json()
session = auth['session']
headers = {'X-ArchivesSpace-Session':session, 'Content_Type':'application/json'}

endpoint = '/subjects?all_ids=true'
# print(baseURL + endpoint)

response = requests.get(baseURL + endpoint, headers=headers)
print(response)
ids = response.json()
# print(ids)
# print()
print(str(len(ids)) + ' subjects')

ids.sort()
print('ID list sorted')

print('Creating CSV...')
f=csv.writer(open('output.csv', 'w', newline=''))
f.writerow(['uri']+['title']+['authority_id']+['terms'])

for id in ids:
    # print(id)
    endpoint = '/subjects/'+str(id)
    output = requests.get(baseURL + endpoint, headers=headers).json()
    # print(output)
    # print()
    
    try:
        uri = output['uri']
    except:
        uri = ''
    try:
        title = output['title']
    except:
        title = ''
    try:
        auth_id = output['authority_id']
        print(uri + ' has auth_id')
    except:
        auth_id = ''
    try:
        terms = output['terms']
        
        term = ''
        for t in terms:
            term += t['term']
    except:
        terms = ''
    
    f.writerow([uri]+[title]+[auth_id]+[term])
	
