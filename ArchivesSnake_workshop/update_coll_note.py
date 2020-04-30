from asnake.aspace import ASpace
from asnake.client import ASnakeClient
client = ASnakeClient()
client.authorize()

aspace = ASpace()
repo = aspace.repositories(2)

collection = repo.resources(2)
collectJson = collection.json()
print(collectJson)
print()
print()

'''
for note in collectJson['notes']:
    if note['type'] == 'scopecontent':
        for subnote in note['subnotes']:
            print(subnote)
            subnote['content'] = 'My new Note is very, very short.'
            print()
            print()
            print(subnote)

update = client.post(collectJson['uri'], json=collectJson)
print(update.status_code)

'''