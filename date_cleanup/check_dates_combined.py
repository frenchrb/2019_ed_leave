import re
from asnake.aspace import ASpace

aspace = ASpace()
repo = aspace.repositories(2)

for collection in repo.resources:
    for date in collection.dates:
        if '(' in date.expression or 'bulk' in date.expression:
            print('====================')
            print(collection.id_0 + '\t' + collection.title + '\t' + collection.uri)
            print(date.expression + '\t' + date.date_type)
            print()
