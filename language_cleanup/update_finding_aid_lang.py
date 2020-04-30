from asnake.aspace import ASpace
from asnake.client import ASnakeClient

client = ASnakeClient()
client.authorize()

aspace = ASpace()
repo = aspace.repositories(2)

for collection in repo.resources:
    print('====================')
    print(collection.id_0 + '\t' + collection.title + '\t' + collection.uri)
    print('finding_aid_language: ' + collection.finding_aid_language)
    print('finding_aid_script: ' + collection.finding_aid_script)
    # print('finding_aid_language_note: ' + collection.finding_aid_language_note)
    print()
    
    update = False
    collectJson = collection.json()
    if collectJson['finding_aid_language'] != 'eng':
        print('finding_aid_language will be updated to eng')
        collectJson['finding_aid_language'] = 'eng'
        update = True
    if collectJson['finding_aid_script'] != 'Latn':
        print('finding_aid_script will be updated to Latn')
        collectJson['finding_aid_script'] = 'Latn'
        update = True
    
    if update:
        update = client.post(collectJson['uri'], json=collectJson)
        print(update.status_code)
        print()
        
        num = collectJson['uri'].replace('/repositories/2/resources/', '')
        collection = repo.resources(num)
        print('updated finding_aid_language: ' + collection.finding_aid_language)
        print('updated finding_aid_script: ' + collection.finding_aid_script)
    else:
        print('no changes needed')
    print()
