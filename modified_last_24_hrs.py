from datetime import datetime, timedelta
from asnake.aspace import ASpace

aspace = ASpace()
repo = aspace.repositories(2)

print('MODIFIED WITHIN LAST 24 HOURS:')

d = datetime.now() - timedelta(days=1)
for collection in repo.resources:
    mdate = datetime(int(collection.system_mtime[:4]), int(collection.system_mtime[5:7]), int(collection.system_mtime[8:10]), int(collection.system_mtime[11:13]), int(collection.system_mtime[14:16]), int(collection.system_mtime[17:19]))
    
    if mdate >= d:
        print(collection.id_0 + '\t' + collection.title + '\t' + collection.uri)
        print('Last modified by ' + collection.last_modified_by + ' on ' + collection.system_mtime)
        print('Published: ' + str(collection.publish))
        print()
