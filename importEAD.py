import json
import requests
import secrets_local
import csv

baseURL = secrets_local.baseURL
user = secrets_local.user
password = secrets_local.password

auth = requests.post(baseURL + '/users/'+user+'/login?password='+password).json()
session = auth["session"]
headers = {'X-ArchivesSpace-Session':session, 'Content_Type':'application/json'}

job = json.dumps({
                "job_type": "import_job",
                "job": {
                    "import_type": "ead_xml",
                    "jsonmodel_type": "import_job",
                    "filenames": ["SC0251"]
                }
})
test = [("files[]", open("SC0251.xml", "rb"))]

endpoint = '/repositories/2/jobs_with_files'

# response = requests.get(baseURL + endpoint, headers=headers).json()
response = requests.post(url=baseURL + endpoint, headers=headers,
                         params={"job": job},
                         files=test).json()
print(response)

