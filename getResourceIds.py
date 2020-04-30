import json
import requests
import secrets
import csv

baseURL = secrets.baseURL
user = secrets.user
password = secrets.password

auth = requests.post(baseURL + '/users/'+user+'/login?password='+password).json()
session = auth["session"]
headers = {'X-ArchivesSpace-Session':session, 'Content_Type':'application/json'}

endpoint = '/repositories/4/resources?all_ids=true'

ids = requests.get(baseURL + endpoint, headers=headers).json()

f=csv.writer(open('output.csv', 'w', newline=''))
f.writerow(['id_0']+['ead_id']+['Published']+['Title']+['URL'])

for id in ids:
    print(id)
    endpoint = '/repositories/4/resources/'+str(id)
    output = requests.get(baseURL + endpoint, headers=headers).json()
    try:
        id_0 = output['id_0']
    except:
        id_0 = ''
    try:
        ead_id = output['ead_id']
    except:
        ead_id = ''
    try:
        published = output['publish']
    except:
        published = ''
    try:
        title = output['finding_aid_title']
    except:
        title = ''
    f.writerow([id_0]+[ead_id]+[published]+[title]+['https://aspace.lib.jmu.edu'+endpoint])
