import datetime
from asnake.aspace import ASpace

aspace = ASpace()
repo = aspace.repositories(2)

for collection in repo.resources:
    print('====================')
    print(collection.id_0 + '\t' + collection.title + '\t' + collection.uri)
    # print(collection)
    print('Last modified by ' + collection.last_modified_by + '\t' + collection.system_mtime + '\t' + collection.user_mtime)
    print('Published: ' + str(collection.publish))
    print()
