import glob
import json
import requests
import secrets_local
import csv
from pathlib import Path

baseURL = secrets_local.baseURL
user = secrets_local.user
password = secrets_local.password

auth = requests.post(baseURL + '/users/'+user+'/login?password='+password).json()
session = auth["session"]
headers = {'X-ArchivesSpace-Session':session, 'Content_Type':'application/json'}

endpoint = '/repositories/2/jobs_with_files'
directory = 'files_to_load'
file_list = []
filenames = []

for f in glob.iglob(directory + '/*.xml'):
    filename = Path(f).stem
    file_list.append(('files[]', open(f, 'rb')))
    filenames.append(filename)
print('Files to be imported:')
print(filenames)

job = json.dumps({
                'job_type': 'import_job',
                'job': {
                    'import_type': 'ead_xml',
                    'jsonmodel_type': 'import_job',
                    'filenames': filenames
                }
})
response = requests.post(url=baseURL + endpoint, headers=headers,
                         params={'job': job},
                         files=file_list).json()
print('Import job ' + response['uri'] + ' started.')
